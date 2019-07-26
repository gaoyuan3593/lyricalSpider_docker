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
from service.micro.news import CRI_NEWS, NEWS_ES_TYPE
from service.db.utils.elasticsearch_utils import ElasticsearchClient, NEWSDETAIL


class CyolSpider(object):
    __name__ = 'cyol news'

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
            self.es.insert("test", _type, data)
            logger.info(" save to es success data= {}！".format(data))
        except Exception as e:
            raise e

    def random_num(self):
        return random.uniform(0.1, 0.5)

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_news_all_url(self):
        logger.info('Processing get cyol news list!')
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
            if "国际在线：向世界报道中国，向中国报道世界_中国国际广播电台" in response.text:
                for url in CRI_NEWS:
                    parms = r"{}\d+/\w+-\w+-\w+-\w+-\w+.html|{}\w+/\d+/\w+-\w+-\w+-\w+-\w+.html".format(url, url)
                    _url_list = re.findall(parms, response.text)
                    url_list.extend(["http:" + i for i in _url_list])
            else:
                raise InvalidResponseError
            return list(set(url_list))
        except Exception as e:
            time.sleep(1)
            raise InvalidResponseError

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_news_detail(self, url):
        logger.info('Processing get cyol news details !!!')
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
                logger.info("get cyol news detail success url: {}".format(url))
                article_id = url.split("/")[-1].split(".")[0]
                return dict(article_id=article_id, resp=response.text, news_url=url)
            else:
                logger.error("get cyol news detail failed")
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
        _content, _editor, _source = "", "", "国际在线网"
        _publish_time = (datetime.now() + timedelta(minutes=-10)).strftime("%Y-%m-%d %H:%M")
        try:
            x_html = etree.HTML(resp)
            title = x_html.xpath(self.title_xpath) or \
                    x_html.xpath('//*[@class="Atitle"]/text()') or \
                    x_html.xpath('//*[@class="con-title clearfix"]/h3/text()') or \
                    x_html.xpath('//*[@id="atitle"]/text()') or \
                    x_html.xpath('//*[@class="caption marginTop15"]/p/text()') or \
                    x_html.xpath('//*[@class="caption marginTop30"]/p/text()')
            _title = str(title[0]).strip() if title else ""
            content = x_html.xpath(self.content_xpath)
            if not content:
                _str = ""
                content = x_html.xpath('//*[@class="u-mainText"]/p/font/text()') or \
                          x_html.xpath('//*[@class="h-contentMain"]/p/text()')
                _content = "".join(content).strip()
            else:
                _content = "".join("".join(content).strip().split())
            if not title or not content:
                return
            publish_time = x_html.xpath(self.publish_time_xpath) or \
                           x_html.xpath('//*[@id="apublishtime"]/text()')
            _publish_time = china_news_str_to_format_time(publish_time) or \
                            x_html.xpath('//*[@class="sign left"]/span[1]/text()')
            source = x_html.xpath('//*[@id="asource"]/a/text()') or \
                     x_html.xpath('//*[@class="info"]/span[2]/a/text()') or \
                     x_html.xpath('//*[@id="asource"]/text()') or \
                     x_html.xpath('//*[@class="sign left"]/span[3]/a/text()')
            if source:
                source = "".join(source)
                try:
                    if "来源" not in source:
                        _source = source
                    else:
                        _source = re.findall(r"来源.(.*)", source)[0].strip()
                except:
                    pass
            editor = x_html.xpath('//*[@id="aeditor"]/text()') or \
                     x_html.xpath('//*[@class="info"]/span[3]/text()') or \
                     x_html.xpath('//*[@class="sign left"]/span[5]/text()')
            # x_html.xpath('//*[@class="liability"]/text()')
            if editor:
                editor = "".join(editor)
                try:
                    editor = re.findall(r"编辑：(.*)", editor)
                    _editor = editor[0]
                except:
                    pass
            data = dict(
                title=_title,  # 标题
                article_id=article_id,  # 文章id
                date=_publish_time,  # 发布时间
                source=_source,  # 来源
                editor=_editor,  # 责任编辑
                news_url=news_url,  # url连接
                type=NEWS_ES_TYPE.gmw_news,
                content=_content,  # 内容
                crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")  # 爬取时间
            )
            dic = {"article_id.keyword": article_id}
            self.save_one_data_to_es(data, dic)
        except Exception as e:
            logger.exception(e)


def cyol_news_run():
    detail_list = []
    data = {
        "siteName": "中青在线",
        "domain": "http://www.cri.cn/",
        "startURL": [
            "http://www.cri.cn/"
        ],
        "id": "",
        "thread": "1",
        "retry": "2",
        "sleep": "0",
        "maxPageGather": "10",
        "timeout": "5000",
        "contentReg": "",
        "contentXPath": "//*[@id='abody']/p/text()",
        "titleReg": "",
        "titleXPath": '//*[@id="goTop"]/text()',
        "categoryReg": "",
        "categoryXPath": "",
        "defaultCategory": "",
        "urlReg": "http://\\w+\\.people.com.cn/\d+/\d+-\d+/\d+.shtml",
        "charset": "",
        "publishTimeXPath": '//*[@id="acreatedtime"]/text()',
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
    china = CyolSpider(data)
    try:
        news_url_list = china.get_news_all_url()
    except Exception as e:
        logger.exception(e)
        return
    for dic in news_url_list:
        try:
            detail_list.append(china.get_news_detail(dic))
        except:
            continue
    for _data in detail_list:
        china.parse_news_detail(_data)


if __name__ == '__main__':
    cyol_news_run()
