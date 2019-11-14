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
from service.micro.utils.math_utils import china_news_str_to_format_time
from service.micro.news import CHINA_NEWS, NEWS_ES_TYPE
from service.micro.news.utils.search_es import SaveDataToEs


class ChinaNewsSpider(object):
    __name__ = 'china news'

    def __init__(self, data):
        self.domain = data.get("domain")
        self.s = requests.session()
        self.es_index = data.get("website_index")

    def random_num(self):
        return random.uniform(0.1, 0.5)

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_news_all_url(self):
        logger.info('Processing get china news list!')
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
                for url in CHINA_NEWS:
                    _url_list = re.findall(r"{}\d+/\d+-\d+/\d+.shtml".format(url), response.text)
                    url_list.extend(["http://{}".format(i) for i in _url_list])
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
        }
        try:
            response = self.s.get(news_url, headers=headers, verify=False)
            response.encoding = "utf-8"
            if "中国新闻网" in response.text or "首页" in response.text:
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
        _content = ""
        try:
            x_html = etree.HTML(resp)
            title = x_html.xpath("//*[@id='cont_1_1_2']/h1/text()")
            _title = str(title[0]).strip() if title else ""
            content = x_html.xpath("//*[@id='cont_1_1_2']/div/p/text()")
            if not content:
                _str = ""
                content = x_html.xpath('//*[@id="cont_1_1_2"]/div[6]/div/img/@src')
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
            publish_time = x_html.xpath("//*[@id='cont_1_1_2']/div[4]/div[2]/text()")
            _publish_time = china_news_str_to_format_time(publish_time)
            source = x_html.xpath("//*[@id='cont_1_1_2']/div[4]/div[2]/text()")
            _source = str(source[0]).split("来源：")[1].strip() if source else "中国新闻网"
            is_editor = "".join(x_html.xpath('//*[@id="cont_1_1_2"]/div/div/text()'))
            _editor = re.findall(r"编辑:(.*?)】", is_editor)[0] if "编辑" in is_editor else ""
            data = dict(
                title=_title,  # 标题
                article_id=article_id,  # 文章id
                date=_publish_time,  # 发布时间
                source=_source,  # 来源
                editor=_editor,  # 责任编辑
                news_url=news_url,  # url连接
                new_type=NEWS_ES_TYPE.china_news,
                type="detail_type",
                contents=_content,  # 内容
                crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")  # 爬取时间
            )
            SaveDataToEs.save_one_data_to_es(self.es_index, data, article_id)
            return data
        except Exception as e:
            logger.exception(e)


def get_handler(*args, **kwargs):
    return ChinaNewsSpider(*args, **kwargs)


def china_news_run():
    from service.micro.utils.threading_parse import WorkerThreadParse

    detail_list = []
    threads = []
    data = {
        "siteName": "人民网",
        "domain": "http://www.chinanews.com/",
        "startURL": [
            "http://www.chinanews.com/"
        ],
        "website_index": "all_news_details",
        "id": "",
        "thread": "1",
        "retry": "2",
        "sleep": "0",
        "maxPageGather": "10",
        "timeout": "5000",
        "contentReg": "",
        "contentXPath": "//*[@id='cont_1_1_2']/div/p/text()",
        "titleReg": "",
        "titleXPath": "//*[@id='cont_1_1_2']/h1/text()",
        "categoryReg": "",
        "categoryXPath": "",
        "defaultCategory": "",
        "urlReg": "http://\\w+\\.people.com.cn/\d+/\d+-\d+/\d+.shtml",
        "charset": "",
        "publishTimeXPath": "//*[@id='cont_1_1_2']/div[4]/div[2]/text()",
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
    china_news = ChinaNewsSpider(data)

    try:
        news_url_list = china_news.get_news_all_url()
    except Exception as e:
        logger.exception(e)
        return
    for news_url in news_url_list:
        detail_list.append(china_news.get_news_detail(news_url))

    for _data in detail_list:
        china_news.parse_news_detail(_data)


if __name__ == '__main__':
    china_news_run()
