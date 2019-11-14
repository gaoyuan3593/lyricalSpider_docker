#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random
import time
import json
import re
import requests
from lxml import etree
from datetime import datetime
from service.exception import retry
from service.exception.exceptions import *
from service import logger
from service.micro.utils import ua
from service.micro.utils.math_utils import xinhua_str_to_format_time
from service.micro.news import XINHUA, NEWS_ES_TYPE
from service.micro.news.utils.search_es import SaveDataToEs


class XinHuaSpider(object):
    __name__ = 'xinhua news'

    def __init__(self, data):
        self.domain = data.get("domain")
        self.s = requests.session()
        self.es_index = data.get("website_index")

    def random_num(self):
        return random.uniform(0.1, 0.5)

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_news_all_url(self):
        logger.info('Processing get xin hua network list!')
        headers = {
            'User-Agent': ua(),
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9'
        }
        url_list = []
        try:
            response = self.s.get(self.domain, headers=headers, verify=False)
            response.encoding = "utf-8"
            if "首页" in response.text and "滚动" in response.text:
                for url in XINHUA:
                    _url_list = re.findall(r"{}\d+-\d+/\d+/\w+.htm".format(url), response.text)
                    url_list.extend(_url_list)
            return list(set(url_list))
        except Exception as e:
            raise InvalidResponseError

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_news_detail(self, news_url):
        logger.info('Processing get china news details !!!')
        headers = {
            'User-Agent': ua(),
            'Proxy-Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 'www.xinhuanet.com'
        }
        try:
            response = self.s.get(news_url, headers=headers, verify=False)
            response.encoding = "utf-8"
            if "客户端" in response.text or "新华网" in response.text:
                logger.info("get xin hua news detail success url: {}".format(news_url))
                article_id = news_url.split("/")[-1].split(".")[0]
                return dict(article_id=article_id, resp=response.text, news_url=news_url)
            else:
                logger.error("get news detail failed")
                raise InvalidResponseError
        except Exception as e:
            raise InvalidResponseError

    def parse_news_detail(self, _data):
        if not _data:
            return
        resp = _data.get("resp")
        news_url = _data.get("news_url")
        article_id = _data.get("article_id")
        _content, _editor = "", ""
        try:
            x_html = etree.HTML(resp)
            title = x_html.xpath("/html/body/div[2]/div[3]/div/div/text()") or \
                    x_html.xpath('//*[@class="h-title"]/text()') or \
                    x_html.xpath('//*[@id="title"]/text()') or \
                    x_html.xpath('//*[@id="conTit"]/h1/text()')
            _title = str(title[0]).strip() if title else ""
            content = x_html.xpath("//*[@id='p-detail']/p/text()")
            if not content:
                _str = ""
                content = x_html.xpath('//*[@id="article"]/div/p/text()') or \
                          x_html.xpath('//*[@id="content"]/p/text()') or \
                          x_html.xpath('//*[@id="p-detail"]/div/p/text()')
                for i in content:
                    if "\n\t" == i: continue
                    if ".jpg" in i or ".png" in i:
                        _str += news_url.split("cn")[0] + "cn" + i + ","
                if not _str:
                    _content = "".join(content).strip()
                else:
                    _content = _str
            else:
                _content = "".join(content).strip()
            publish_time = x_html.xpath("/html/body/div[2]/div[3]/div/div[2]/span[1]/text()") or \
                           x_html.xpath('//*[@id="pubtime"]/text()') or \
                           x_html.xpath('//*[@id="conTit"]/div/span[1]/span/text()') or \
                           x_html.xpath('//*[@class="h-time"]/text()') or \
                           x_html.xpath('//*[@class="time"]/text()')
            _publish_time = xinhua_str_to_format_time(publish_time)
            source = x_html.xpath("//*[@id='source']/text()")
            _source = str(source[0]).strip() if source else "新华网"
            is_editor = x_html.xpath('//*[@id="p-detail"]/div/span/text()') or \
                        x_html.xpath('//*[@id="articleEdit"]/span/text()') or \
                        x_html.xpath('/html/body/div[1]/div[4]/div[1]/div[3]/div/text()') or \
                        x_html.xpath('//*[@class="edit"]/text()')
            is_editor = "".join(is_editor).strip()
            if is_editor:
                if "\n" in is_editor:
                    _editor = is_editor.split("\n")[1].strip()
                elif "[" in is_editor or "]" in is_editor:
                    _editor = re.findall(r"编辑:(.*?)]", is_editor)[0].strip()
            data = dict(
                title=_title,  # 标题
                article_id=article_id,  # 文章id
                date=_publish_time,  # 发布时间
                source=_source,  # 来源
                editor=_editor,  # 责任编辑
                news_url=news_url,  # url连接
                news_type=NEWS_ES_TYPE.xinhua,
                type="detail_type",
                contents=_content,  # 内容
                crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")  # 爬取时间
            )
            SaveDataToEs.save_one_data_to_es(self.es_index, data, article_id)
        except Exception as e:
            logger.exception(e)


def get_handler(*args, **kwargs):
    return XinHuaSpider(*args, **kwargs)


def xinhua_run():
    from service.micro.utils.threading_parse import WorkerThreadParse

    detail_list = []
    threads = []
    data = {
        "siteName": "新华网",
        "domain": "http://www.xinhuanet.com/",
        "startURL": [
            "http://www.xinhuanet.com/"
        ],
        "website_index": "website_xin_hua_wang_2810373291",
        "id": "",
        "thread": "1",
        "retry": "2",
        "sleep": "0",
        "maxPageGather": "10",
        "timeout": "5000",
        "contentReg": "",
        "contentXPath": "//*[@id='p-detail']/p/text()",
        "titleReg": "",
        "titleXPath": '/html/body/div[2]/div[3]/div/div/text()',
        "categoryReg": "",
        "categoryXPath": "",
        "defaultCategory": "",
        "urlReg": "http://\\w+\\.people.com.cn/\d+/\d+-\d+/\d+.shtml",
        "charset": "",
        "publishTimeXPath": "/html/body/div[2]/div[3]/div/div[2]/span[1]/text()",
        "publishTimeReg": "",
        "publishTimeFormat": "yyyy年MM月dd日HH:mm",
        "lang": "",
        "country": "",
        "userAgent": "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
        "proxyHost": "",
        "proxyPort": "0",
        "proxyUsername": "",
        "proxyPassword": "",
        "doNLP": True,
        "needPublishTime": True,
        "saveCapture": True,
        "gatherFirstPage": False,
        "needTitle": False,
        "needContent": False,
        "autoDetectPublishDate": False,
        "ajaxSite": False,
        "dynamicFields": [

        ],
        "staticFields": [

        ]
    }
    xinhua = XinHuaSpider(data)
    try:
        news_url_list = xinhua.get_news_all_url()
    except Exception as e:
        logger.exception(e)
        return
    for news_url in news_url_list:
        worker = WorkerThreadParse(detail_list, xinhua.get_news_detail, (news_url,))
        worker.start()
        threads.append(worker)

    for _data in detail_list:
        worker = WorkerThreadParse([], xinhua.parse_news_detail, (_data,))
        worker.start()
        threads.append(worker)

    for work in threads:
        work.join(1)
        if work.isAlive():
            logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
            threads.append(work)


if __name__ == '__main__':
    xinhua_run()
