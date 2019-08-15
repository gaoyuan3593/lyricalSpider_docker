#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random
import time
import json
import re
import requests
from datetime import datetime
from lxml import etree
from service.exception import retry
from service.exception.exceptions import *
from service import logger
from service.micro.utils import ua
from service.micro.utils.math_utils import china_str_to_format_time
from service.micro.news import CHINA, NEWS_ES_TYPE
from service.micro.news.utils.search_es import SaveDataToEs


class ChinaSpider(object):
    __name__ = 'china network'

    def __init__(self, data):
        self.domain = data.get("domain")
        self.s = requests.session()

    def random_num(self):
        return random.uniform(0.1, 0.5)

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_news_all_url(self):
        logger.info('Processing get china list!')
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
            if "中国网" in response.text:
                for url in CHINA:
                    _url_list = re.findall(r"{}\d+-\d+/\d+/\w+_\w+.htm".format(url), response.text)
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
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': re.findall(r'http://(\w+.china.com.cn)', news_url)[0]
        }
        try:
            response = self.s.get(news_url, headers=headers, verify=False)
            response.encoding = "utf-8"
            if response.status_code == 200:
                logger.info("get china news detail success url: {}".format(news_url))
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
        _content, _editor, _source = "", "", "中国网"
        try:
            x_html = etree.HTML(resp)
            title = x_html.xpath("//html/body/div/h1/text()") or \
                    x_html.xpath('//*[@id="artBox"]/h1/text()') or \
                    x_html.xpath('/html/body/div[1]/div/h1/text()') or \
                    x_html.xpath('/html/body/div/div/h1/text()') or \
                    x_html.xpath('//*[@class="artTitle"]/text()') or \
                    x_html.xpath('//*[@class="center_title"]/h1/text()') or \
                    x_html.xpath('/html/body/div[1]/div[3]/div[1]/h1/text()')
            _title = str(title[0]).strip() if title else ""
            content = x_html.xpath("//*[@id='articleBody']/p/text()")
            if not content:
                _str = ""
                content = x_html.xpath('//*[@id="artbody"]/p/text()') or \
                          x_html.xpath('//*[@class="center_box"]/p/text()') or \
                          x_html.xpath('//*[@class="content"]/p/text()') or \
                          x_html.xpath('//*[@id="artiContent"]/p/text()') or \
                          x_html.xpath('//*[@id="c_body"]/p/text()') or \
                          x_html.xpath('//*[@class="d3_left_text"]/p/text()') or \
                          x_html.xpath('//*[@id="artiContent"]/p/span/text()')
                _content = "".join(content).strip()
            else:
                _content = "".join(content).strip()
            if not title or not content:
                return
            publish_time = x_html.xpath("//*[@id='pubtime_baidu']/text()") or \
                           x_html.xpath('//*[@id="pubtime"]/text()') or \
                           x_html.xpath("/html/body/div/div/h2/text()") or \
                           x_html.xpath("//*[@class='span']/text()") or \
                           x_html.xpath("//*[@class='source']/text()")
            _publish_time = china_str_to_format_time(publish_time)
            source = x_html.xpath("//*[@id='source_baidu']/a/text()") or \
                     x_html.xpath('//*[@id="source_baidu"]/text()') or \
                     x_html.xpath("//*[@class='span']/text()") or \
                     x_html.xpath('//*[@class="source"]/text()')
            source = "".join(source).strip()
            if source:
                if "来源" in source and "作者" not in source:
                    _source = source.split("来源：")[1]
                elif "内容来源" in source:
                    _source = source.split(":")[1].strip()
                elif "来源" in source and "作者" in source:
                    _ = re.findall(r"来源：(.*)", source)
                    _source = _[0].split("|")[0].strip() if _ else ""
                elif "发布时间" not in source and "来源" not in source and "作者":
                    pass
                else:
                    _source = str(source[0]).strip() if source else "中国网"
            is_editor = x_html.xpath('//*[@id="author_baidu"]/text()') or \
                        x_html.xpath('/html/body/div/h2/text()')
            is_editor = "".join(is_editor).strip()
            if is_editor:
                if "作者" in is_editor and "来源" not in is_editor:
                    _editor = is_editor.split("作者：")[1].strip()
                elif "来源" in is_editor or "责任编辑" in is_editor:
                    _editor = re.findall(r'作者:(.*)?', _editor)
                    _editor = _editor[0].split("|")[0] if _editor else ""
            data = dict(
                title=_title,  # 标题
                article_id=article_id,  # 文章id
                date=_publish_time,  # 发布时间
                source=_source,  # 来源
                editor=_editor,  # 责任编辑
                news_url=news_url,  # url连接
                type=NEWS_ES_TYPE.china,
                contents=_content,  # 内容
                crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")  # 爬取时间
            )
            dic = {"article_id": article_id}
            SaveDataToEs.save_one_data_to_es(data, dic)
        except Exception as e:
            logger.exception(e)


def china_spider_run():
    detail_list = []
    data = {
        "siteName": "新华网",
        "domain": "http://www.china.com.cn/",
        "startURL": [
            "http://www.china.com.cn/"
        ],
        "id": "",
        "thread": "1",
        "retry": "2",
        "sleep": "0",
        "maxPageGather": "10",
        "timeout": "5000",
        "contentReg": "",
        "contentXPath": "//*[@id='articleBody']/p/text()",
        "titleReg": "",
        "titleXPath": '//html/body/div/h1/text()',
        "categoryReg": "",
        "categoryXPath": "",
        "defaultCategory": "",
        "urlReg": "http://\\w+\\.people.com.cn/\d+/\d+-\d+/\d+.shtml",
        "charset": "",
        "publishTimeXPath": "//*[@id='pubtime_baidu']/text()",
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
    china = ChinaSpider(data)
    try:
        news_url_list = china.get_news_all_url()
    except Exception as e:
        logger.exception(e)
        return
    for news_url in news_url_list:
        try:
            detail_list.append(china.get_news_detail(news_url))
        except:
            continue
    for _data in detail_list:
        china.parse_news_detail(_data)


if __name__ == '__main__':
    china_spider_run()
