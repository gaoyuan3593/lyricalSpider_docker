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
from service.micro.utils.math_utils import xinhua_str_to_format_time
from service.micro.news import CNR_NEWS, NEWS_ES_TYPE
from service.db.utils.elasticsearch_utils import ALL_NEWS_DETAILS, NEWS_DETAIL_MAPPING
from service.micro.news.utils.search_es import SaveDataToEs

_index_mapping = {
    NEWS_ES_TYPE.cnr_news:
        {
            "properties": NEWS_DETAIL_MAPPING
        }
}


class CnrSpider(object):
    __name__ = 'cnr news'

    def __init__(self, data):
        self.domain = data.get("domain")
        self.s = requests.session()
        SaveDataToEs.create_index(ALL_NEWS_DETAILS, _index_mapping)

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
            result = self.es.dsl_search("test1", _type, mapping)
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
        logger.info('Processing get cnr news search list!')
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
            if "央广网・中央人民广播电台" in response.text:
                for url_tuble in CNR_NEWS:
                    url, host = url_tuble
                    parms = r"{}\d+/\w+.shtml".format(url)
                    _url_list = re.findall(parms, response.text)
                    _list = [(_url, host) for _url in _url_list]
                    url_list.extend(_list)
            return list(set(url_list))
        except Exception as e:
            raise InvalidResponseError

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_news_detail(self, data):
        logger.info('Processing get cnr news details !!!')
        news_url, host = data
        self.s.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
            'Proxy-Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            "Host": host,
            "Connection": "keep-alive",
        }
        try:
            response = self.s.get(news_url)
            if response.status_code == 200:
                response.encoding = "gb2312"
                logger.info("get cnr news success url: {}".format(news_url))
                article_id = news_url.split("/")[-1].split(".")[0]
                return dict(article_id=article_id, resp=response.text, news_url=news_url)
            else:
                logger.error("get cnr detail failed")
                raise InvalidResponseError
        except Exception as e:
            if "Exceeded 30 redirects." in e.args[0]:
                return
            time.sleep(1)
            raise InvalidResponseError

    def parse_news_detail(self, _data):
        if not _data:
            return
        resp = _data.get("resp")
        news_url = _data.get("news_url")
        article_id = _data.get("article_id")
        _content, _editor, _source = "", "", "参考消息网"
        try:
            x_html = etree.HTML(resp)
            title = x_html.xpath(self.title_xpath)
            if not title:
                title = x_html.xpath('//*[@class="h2 fz-23 YH"]/text()')
            _title = str(title[0]).strip() if title else ""
            content = x_html.xpath(self.content_xpath)
            if not content:
                content = x_html.xpath('//*[@id="ctrlfscont"]/p/text()')
                _content = "".join(content).strip()
            else:
                _content = "".join(content).strip()
            if not title and not content:
                return
            publish_time = x_html.xpath(self.publish_time_xpath)
            if not publish_time:
                publish_time = x_html.xpath('//*[@id="pubtime_baidu"]/text()')
            _publish_time = xinhua_str_to_format_time(publish_time)
            source = x_html.xpath('//*[@id="source_baidu"]/text()') or \
                     x_html.xpath('//*[@id="source_baidu"]/a/text()')
            if source:
                source = "".join(source).strip()
                source = re.findall(r"来源.(.*)", source)
                if source:
                    _source = source[0]
            editor = re.findall(r"责任编辑：(\w+)", resp)
            if editor:
                _editor = editor[0]
            data = dict(
                title=_title,  # 标题
                id=article_id,  # 文章id
                time=_publish_time,  # 发布时间
                source=_source,  # 来源
                author=_editor,  # 责任编辑
                link=news_url,  # url连接
                type=NEWS_ES_TYPE.cnr_news,
                content=_content,  # 内容
                crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")  # 爬取时间
            )
            dic = {"article_id.keyword": article_id}
            self.save_one_data_to_es(data, dic)
            return data
        except Exception as e:
            logger.exception(e)


def cnr_news_run():
    detail_list = []
    data = {
        "siteName": "央广网",
        "domain": "http://www.cnr.cn/",
        "startURL": [
            "http://www.cnr.cn/"
        ],
        "id": "",
        "thread": "1",
        "retry": "2",
        "sleep": "0",
        "maxPageGather": "10",
        "timeout": "5000",
        "contentReg": "",
        "contentXPath": "//*[@class='articleText']/p/text()",
        "titleReg": "",
        "titleXPath": "//*[@class='articleHead']/text()",
        "categoryReg": "",
        "categoryXPath": "",
        "defaultCategory": "",
        "urlReg": "http://\\w+\\.people.com.cn/\\w+/\\d+\\/\\d+\\/\\w+\\-\\d+\\.html",
        "charset": "",
        "publishTimeXPath": "//*[@if='pubtime_baidu']/text()",
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
    spider = CnrSpider(data)
    news_url_list = spider.get_news_all_url()
    for dic in news_url_list:
        try:
            detail_list.append(spider.get_news_detail(dic))
        except:
            continue
    for _data in detail_list:
        spider.parse_news_detail(_data)


if __name__ == '__main__':
    ########   暂时有问题
    cnr_news_run()
