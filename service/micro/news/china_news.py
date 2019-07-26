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
from service.db.utils.elasticsearch_utils import ElasticsearchClient, NEWSDETAIL


class ChinaNewsSpider(object):
    __name__ = 'china news'

    def __init__(self, data):
        self.start_url = data.get("startURL")[0]
        self.title_xpath = data.get("titleXPath")
        self.content_xpath = data.get("contentXPath")
        self.publish_time_xpath = data.get("publishTimeXPath")
        self.s = requests.session()
        self.es = ElasticsearchClient()

    def filter_keyword(self, _type, _dic, data=None):
        mapping = {
            "query": {
                "bool":
                    {
                        "must":
                            [{
                                "term": _dic}],
                        "must_not": [],
                        "should": []}},
            "sort": [],
            "aggs": {}
        }
        try:
            result = self.es.dsl_search(NEWSDETAIL, _type, mapping)
            if result.get("hits").get("hits"):
                logger.info("dic : {} is existed".format(_dic))
                return True
            return False
        except Exception as e:
            return False

    def save_one_data_to_es(self, data, dic):
        """
        将为爬取的数据存入es中
        :param data_list: 数据
        :return:
        """
        try:
            _type = data.get("type")
            if self.filter_keyword(_type, dic, data):
                logger.info("is existed  dic: {}".format(dic))
                return
            self.es.insert(NEWSDETAIL, _type, data)
            logger.info(" save to es success data= {}！".format(data))
        except Exception as e:
            raise e

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
            response = self.s.get(self.start_url, headers=headers, verify=False)
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
            title = x_html.xpath(self.title_xpath)
            _title = str(title[0]).strip() if title else ""
            content = x_html.xpath(self.content_xpath)
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
            publish_time = x_html.xpath(self.publish_time_xpath)
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
                type=NEWS_ES_TYPE.china_news,
                content=_content,  # 内容
                crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")  # 爬取时间
            )
            dic = {"article_id.keyword": article_id}
            self.save_one_data_to_es(data, dic)
            return data
        except Exception as e:
            logger.exception(e)


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
        worker = WorkerThreadParse(detail_list, china_news.get_news_detail, (news_url,))
        worker.start()
        threads.append(worker)
    for _data in detail_list:
        worker = WorkerThreadParse([], china_news.parse_news_detail(_data, ))
        worker.start()
        threads.append(worker)

    for work in threads:
        work.join(1)
        if work.isAlive():
            logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
            threads.append(work)


if __name__ == '__main__':
    china_news_run()
