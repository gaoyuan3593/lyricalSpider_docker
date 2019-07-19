#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random
import time
import json
import re
import requests
from lxml import etree
from service.exception import retry
from service.exception.exceptions import *
from service import logger
from service.micro.utils import ua
from service.micro.utils.math_utils import china_news_str_to_format_time
from service.micro.news import YOUTH_NEWS, NEWS_ES_TYPE
from service.db.utils.elasticsearch_utils import ElasticsearchClient, NEWSDETAIL


class YouThSpider(object):
    __name__ = 'china your th news'

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
        logger.info('Processing get china your th search list!')
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
            response.encoding = "gb2312"
            if "中国青年网_青年温度、青春靓度、青网态度" in response.text:
                for url in YOUTH_NEWS:
                    parms = r"{}\w+/\d+\d+/\w+.htm|{}\w+/\w+/\d+\d+/\w+.htm".format(url, url)
                    _url_list = re.findall(parms, response.text)
                    url_list.extend(_url_list)
            return list(set(url_list))
        except Exception as e:
            raise InvalidResponseError

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_news_detail(self, news_url):
        logger.info('Processing get china your th news details !!!')
        headers = {
            'User-Agent': ua(),
            'Proxy-Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            "Host": news_url.split("/")[2],
            "Connection": "keep-alive",
        }
        try:
            response = self.s.get(news_url, headers=headers, verify=False)
            if response.status_code == 200:
                if "charset=gb2312" in response.text or '<meta charset="gb2312">' in response.text:
                    response.encoding = "gb2312"
                else:
                    response.encoding = "utf-8"
                logger.info("get china your th news success url: {}".format(news_url))
                article_id = news_url.split("/")[-1].split(".")[0]
                return dict(article_id=article_id, resp=response.text, news_url=news_url)
            else:
                logger.error("get china your th detail failed")
                raise InvalidResponseError
        except Exception as e:
            time.sleep(1)
            raise InvalidResponseError

    def parse_news_detail(self, _data):
        if not _data:
            return
        resp = _data.get("resp")
        news_url = _data.get("news_url")
        article_id = _data.get("article_id")
        _content, _editor, _source = "", "", "中国青年网"
        try:
            x_html = etree.HTML(resp)
            title = x_html.xpath(self.title_xpath) or \
                    x_html.xpath('//*[@class="pbt"]/text()') or \
                    x_html.xpath('//*[@class="top_biao"]/p/text()') or \
                    x_html.xpath('//*[@class="page_title"]/h1/text()')
            _title = str(title[0]).strip() if title else ""
            content = x_html.xpath(self.content_xpath)
            _content = "".join(content).strip()
            if not _title or not _content:
                return
            _publish_time = re.findall(r"(\d+-\d+-\d+ \d+:\d+)", resp)[0]
            source = x_html.xpath('//*[@class="la_t_b"]/a/text()') or \
                     x_html.xpath('//*[@class="pwz"]/a/text()') or \
                     x_html.xpath('//*[@class="www"]/span[3]/text()')
            if source:
                _source = "".join(source).strip()
            editor = re.findall(r"责编：(\w+)", resp) or \
                     re.findall(r"责任编辑：(\w+)", resp) or \
                     re.findall(r"编辑：(\w+)", resp)
            if editor:
                _editor = editor[0]
            data = dict(
                title=_title,  # 标题
                article_id=article_id,  # 文章id
                date=_publish_time,  # 发布时间
                source=_source,  # 来源
                editor=_editor,  # 责任编辑
                news_url=news_url,  # url连接
                type=NEWS_ES_TYPE.youth_news,
                content=_content,  # 内容
            )
            dic = {"article_id.keyword": article_id}
            self.save_one_data_to_es(data, dic)
            return data
        except Exception as e:
            logger.exception(e)


if __name__ == '__main__':
    from service.micro.utils.threading_parse import WorkerThreadParse

    detail_list = []
    threads = []
    data = {
        "siteName": "中国青年网",
        "domain": "http://www.youth.cn/",
        "startURL": [
            "http://www.youth.cn/"
        ],
        "id": "",
        "thread": "1",
        "retry": "2",
        "sleep": "0",
        "maxPageGather": "10",
        "timeout": "5000",
        "contentReg": "",
        "contentXPath": "//*[@class='TRS_Editor']/p/text()",
        "titleReg": "",
        "titleXPath": '//*[@class="con_biao"]/text()',
        "categoryReg": "",
        "categoryXPath": "",
        "defaultCategory": "",
        "urlReg": "http://\\w+\\.people.com.cn/\\w+/\\d+\\/\\d+\\/\\w+\\-\\d+\\.html",
        "charset": "",
        "publishTimeXPath": '//*[@class="con_tim"]/span[1]/text()',
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
    spider = YouThSpider(data)
    news_url_list = spider.get_news_all_url()
    for dic in news_url_list:
        try:
            detail_list.append(spider.get_news_detail(dic))
        except:
            continue
    for _data in detail_list:
        spider.parse_news_detail(_data)
