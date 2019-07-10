#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random
import time
import json
import re
import requests
from lxml import etree
from datetime import datetime, timedelta
from service.exception import retry
from service.exception.exceptions import *
from service import logger
from service.micro.utils import ua
from service.micro.utils.math_utils import china_news_str_to_format_time
from service.micro.news import K618_NEWS, NEWS_ES_TYPE
from service.db.utils.elasticsearch_utils import ElasticsearchClient, NEWSDETAIL


class K618Spider(object):
    __name__ = 'k 618 news'

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
                            [
                                {"term": _dic}
                            ],
                        "must_not": [],
                        "should": []}},
            "from": 0,
            "size": 10,
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
        logger.info('Processing get gmw news list!')
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
            response.encoding = "gbk"
            if "未来网" in response.text:
                for url in K618_NEWS:
                    parms = r"{}\w+/\d+/\w+.html".format(url)
                    _url_list = re.findall(parms, response.text)
                    url_list.extend(_url_list)
            else:
                raise InvalidResponseError
            return list(set(url_list))
        except Exception as e:
            time.sleep(1)
            raise InvalidResponseError

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_news_detail(self, url):
        logger.info('Processing get k 618 news details !!!')
        headers = {
            'User-Agent': ua(),
            'Proxy-Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        try:
            response = self.s.get(url, headers=headers, verify=False)
            if response.status_code == 200:
                if 'charset=utf-8"' in response.text:
                    response.encoding = "utf-8"
                else:
                    response.encoding = "gbk"
                logger.info("get k 618  news detail success url: {}".format(url))
                article_id = url.split("/")[-1].split(".")[0]
                return dict(article_id=article_id, resp=response.text, news_url=url)
            elif response.status_code == 403:
                pass
            else:
                logger.error("get k 618  news detail failed")
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
        _content, _editor, _source = "", "", "未来网"
        _publish_time = (datetime.now() + timedelta(minutes=-10)).strftime("%Y-%m-%d %H:%M")
        try:
            x_html = etree.HTML(resp)
            title = x_html.xpath(self.title_xpath) or \
                    x_html.xpath('//*[@class="yxzhzwtt fm01 fs22 text-333"]/text()')
            _title = str(title[0]).strip() if title else ""
            content = x_html.xpath(self.content_xpath)
            if not content:
                _str = ""
                content = x_html.xpath('//*[@class="Custom_UnionStyle"]/p/text()') or \
                          x_html.xpath('//*[@class="fck_uploadpics"]/p/span/text()') or \
                          x_html.xpath('//*[@class="TRS_Editor"]/div/font/text()')
                _content = "".join(content).strip()
            else:
                _content = "".join(content).strip()
            if not title or not content:
                return
            publish_time = x_html.xpath(self.publish_time_xpath) or \
                           x_html.xpath('//*[@id="pubtime_baidu"]/text()')
            _publish_time = china_news_str_to_format_time(publish_time)
            source = x_html.xpath('//*[@class="news_time_source"]/span/text()') or \
                     x_html.xpath('//*[@id="source_baidu"]/a/text()')
            if source:
                source = "".join(source).strip()
                try:
                    if "来源" not in source:
                        _source = source
                    else:
                        _source = re.findall(r"来源.(.*)", "".join(source.split()))[0]
                except:
                    pass
            editor = x_html.xpath('//*[@class="news_ep_source"]/text()') or \
                     x_html.xpath('//*[@class="yxzh-bj fs12 text-666"]/text()')
            if editor:
                editor = "".join("".join(editor).split())
                try:
                    if "作者" in editor:
                        _editor = re.findall(r"编辑：(.*)", editor)[0]
                    else:
                        _editor = re.findall(r"编辑：(.*)】", editor)[0]
                except:
                    pass
            data = dict(
                title=_title,  # 标题
                article_id=article_id,  # 文章id
                date=_publish_time,  # 发布时间
                source=_source,  # 来源
                editor=_editor,  # 责任编辑
                news_url=news_url,  # url连接
                type=NEWS_ES_TYPE.k618_news,
                content=_content,  # 内容
            )
            dic = {"article_id.keyword": article_id}
            self.save_one_data_to_es(data, dic)
        except Exception as e:
            logger.exception(e)


if __name__ == '__main__':
    from service.micro.utils.threading_parse import WorkerThreadParse

    detail_list = []
    threads = []
    data = {
        "siteName": "未来网",
        "domain": "http://www.k618.cn/",
        "startURL": [
            "http://www.k618.cn/"
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
        "titleXPath": '//*[@class="news_content_left"]/h1/text()',
        "categoryReg": "",
        "categoryXPath": "",
        "defaultCategory": "",
        "urlReg": "http://\\w+\\.people.com.cn/\d+/\d+-\d+/\d+.shtml",
        "charset": "",
        "publishTimeXPath": '//*[@class="news_time_source"]/text()',
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
    china = K618Spider(data)
    news_url_list = china.get_news_all_url()
    for dic in news_url_list:
        try:
            detail_list.append(china.get_news_detail(dic))
        except:
            continue
    for _data in detail_list:
        china.parse_news_detail(_data)
