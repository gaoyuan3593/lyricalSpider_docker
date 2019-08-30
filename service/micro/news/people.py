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
from service.micro.utils.math_utils import people_str_to_format_time
from service.micro.news import PEOPLE, NEWS_ES_TYPE
from service.micro.news.utils.search_es import SaveDataToEs
from service.micro.news.utils.proxies_util import get_proxies


class PeopleSpider(object):
    __name__ = 'people news'

    def __init__(self, data):
        self.domain = data.get("domain")
        self.s = requests.session()
        self.es_index = data.get("website_index")

    def random_num(self):
        return random.uniform(0.1, 0.5)

    @retry(max_retries=5, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_news_all_url(self):
        logger.info('Processing get people network search list!')
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
            response.encoding = "gb2312"
            if "人民网" in response.text:
                for url in PEOPLE:
                    _url_list = re.findall(r"{}\w+/\d+/\d+/\w+-\d+.html".format(url), response.text)
                    url_list.extend(_url_list)
            return list(set(url_list))
        except Exception as e:
            raise InvalidResponseError

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_news_detail(self, news_url):
        logger.info('Processing get news details !!!')
        headers = {
            'User-Agent': ua(),
            'Proxy-Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        try:
            response = self.s.get(news_url, headers=headers, verify=False)
            response.encoding = "gb2312"
            if "热点推荐" in response.text or "新闻微信公号" in response.text or "人民网" in response.text:
                logger.info("get news detail success url: {}".format(news_url))
                article_id = news_url.split("/")[-1].split(".")[0]
                return dict(article_id=article_id, resp=response.text, news_url=news_url)
            else:
                logger.error("get news detail failed")
                raise InvalidResponseError
        except Exception as e:
            time.sleep(2)
            raise InvalidResponseError

    def parse_news_detail(self, _data):
        if not _data:
            return
        resp = _data.get("resp")
        news_url = _data.get("news_url")
        article_id = _data.get("article_id")
        _content = ""
        try:
            x_html = etree.HTML(resp)
            title = x_html.xpath("//div[contains(@class,'text_title')]/h1/text()")
            if not title:
                title = x_html.xpath('/html/body/div[4]/div[1]/h1/text()') or \
                        x_html.xpath('/html/body/div[7]/div[1]/div/h1/text()') or \
                        x_html.xpath('//*[@class="title"]/h2/text()') or \
                        x_html.xpath('/html/body/div/h1/text()')
            _title = str(title[0]).strip() if title else ""
            content = x_html.xpath("//*[@id='rwb_zw']/p/text()")
            if not content:
                _str = ""
                content = x_html.xpath('/html/body/div[7]/div[1]/div/div[2]/p/text()') or \
                          x_html.xpath('/html/body/div[4]/div[1]/div[2]/p/img/@src') or \
                          x_html.xpath('/html/body/div[4]/div[1]/div[1]/p/text()') or \
                          x_html.xpath('/html/body/div[3]/p/text()') or \
                          x_html.xpath('//*[@class="artDet"]/p/text()') or \
                          x_html.xpath('//*[@id="picG"]/p/text()')
                if not content:
                    pass
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
            publish_time = x_html.xpath("//div[contains(@class,'text_title')]/div/div[1]/text()")
            if not publish_time:
                publish_time = x_html.xpath('/html/body/div[7]/div[1]/div/p[2]/text()') or \
                               x_html.xpath('//div[@class="artOri"]/text()') or \
                               x_html.xpath('/html/body/div[4]/div[1]/h2/text()') or \
                               x_html.xpath('/html/body/div[4]/div[1]/div[1]/h5/text()') or \
                               x_html.xpath('//*[@id="picG"]/div[2]/div[2]/text()[2]') or \
                               x_html.xpath('/html/body/div[3]/h2/text()[2]')
            _publish_time = people_str_to_format_time(publish_time)
            source = x_html.xpath("/html/body/div[4]/div/div[1]/a/text()") or \
                     x_html.xpath('/html/body/div[7]/div[1]/div/p[2]/a/text()') or \
                     x_html.xpath('//div[@class="artOri"]/a/text()') or \
                     x_html.xpath('/html/body/div[4]/div[1]/h2/a/text()') or \
                     x_html.xpath('/html/body/div[4]/div[1]/div[1]/h5/a/text()') or \
                     x_html.xpath('//*[@id="picG"]/div[2]/div[2]/a/text()') or \
                     x_html.xpath('/html/body/div/h2/a/text()')
            _source = str(source[0]).strip() if source else ""
            editor = x_html.xpath('//*[@id="rwb_zw"]/div[4]/text()')
            _editor = editor[0].split("：")[1].split(")")[0] if editor else ""
            data = dict(
                title=_title,  # 标题
                article_id=article_id,  # 文章id
                date=_publish_time,  # 发布时间
                source=_source,  # 来源
                editor=_editor,  # 责任编辑
                news_url=news_url,  # url连接
                type=NEWS_ES_TYPE.people,
                contents=_content,  # 内容
                crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")  # 爬取时间
            )
            SaveDataToEs.save_one_data_to_es(self.es_index, data, article_id)
            return data
        except Exception as e:
            logger.exception(e)


def get_handler(*args, **kwargs):
    return PeopleSpider(*args, **kwargs)


def people_run():
    from service.micro.utils.threading_parse import WorkerThreadParse

    detail_list = []
    threads = []
    data = {
        "siteName": "人民网",
        "domain": "http://www.people.com.cn/",
        "startURL": [
            "http://www.people.com.cn/"
        ],
        "website": "all_news_details",
        "id": "",
        "thread": "1",
        "retry": "2",
        "sleep": "0",
        "maxPageGather": "10",
        "timeout": "5000",
        "contentReg": "",
        "contentXPath": "//*[@id='rwb_zw']/p/text()",
        "titleReg": "",
        "titleXPath": "//div[contains(@class,'text_title')]/h1/text()",
        "categoryReg": "",
        "categoryXPath": "",
        "defaultCategory": "",
        "urlReg": "http://\\w+\\.people.com.cn/\\w+/\\d+\\/\\d+\\/\\w+\\-\\d+\\.html",
        "charset": "",
        "publishTimeXPath": "//div[contains(@class,'text_title')]/div/div[1]/text()",
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
    people = PeopleSpider(data)
    try:
        news_url_list = people.get_news_all_url()
    except Exception as e:
        logger.exception(e)
        return
    for news_url in news_url_list:
        worker = WorkerThreadParse(detail_list, people.get_news_detail, (news_url,))
        worker.start()
        threads.append(worker)
    for _data in detail_list:
        worker = WorkerThreadParse([], people.parse_news_detail(_data, ))
        worker.start()
        threads.append(worker)

    for work in threads:
        work.join(1)
        if work.isAlive():
            logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
            threads.append(work)


if __name__ == '__main__':
    people_run()
