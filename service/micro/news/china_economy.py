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
from service.micro.news.utils.proxies_util import get_proxies
from service.micro.utils import ua
from service.micro.utils.math_utils import china_news_str_to_format_time
from service.micro.news import CHINA_ECONOMY, NEWS_ES_TYPE
from service.db.utils.elasticsearch_utils import ALL_NEWS_DETAILS, NEWS_DETAIL_MAPPING
from service.micro.news.utils.search_es import SaveDataToEs

_index_mapping = {
    NEWS_ES_TYPE.china_economy:
        {
            "properties": NEWS_DETAIL_MAPPING
        }
}


class ChinaEconomySpider(object):
    __name__ = 'china economy news'

    def __init__(self, data):
        self.domain = data.get("domain")
        self.s = requests.session()
        SaveDataToEs.create_index(ALL_NEWS_DETAILS, _index_mapping)

    def random_num(self):
        return random.uniform(0.1, 0.5)

    def use_proxies(self):
        self.s.proxies = get_proxies()

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_news_all_url(self):
        logger.info('Processing get china economy news list!')
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
            if "中国经济网――国家经济门户" in response.text:
                for url in CHINA_ECONOMY:
                    parms = r"{}\d+/\d+/\w+_\d+.shtml|{}\w+/\d+/\d+/\w+_\d+.shtml|{}\w+/\w+/\d+/\d+/\w+_\d+.shtml".format(
                        url, url, url)
                    _url_list = re.findall(parms, response.text)
                    url_list.extend(_url_list)
            else:
                raise InvalidResponseError
            return list(set(url_list))
        except Exception as e:
            time.sleep(1)
            self.use_proxies()
            raise InvalidResponseError

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_news_detail(self, url):
        logger.info('Processing get china economy news details !!!')
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
                if "charset=utf-8" in response.text:
                    response.encoding = "utf-8"
                else:
                    response.encoding = "gb2312"
                logger.info("get china economy news detail success url: {}".format(url))
                article_id = url.split("/")[-1].split(".")[0]
                return dict(article_id=article_id, resp=response.text, news_url=url)
            else:
                logger.error("get china economy news detail failed")
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
        _content, _editor, _source = "", "", "中国经济网"
        _publish_time = (datetime.now() + timedelta(minutes=-10)).strftime("%Y-%m-%d %H:%M")
        try:
            x_html = etree.HTML(resp)
            title = x_html.xpath('//*[@id="articleTitle"]/text()') or \
                    x_html.xpath('//*[@id="artBox"]/h1/text()')
            _title = str(title[0]).strip() if title else ""
            content = x_html.xpath("//*[@class='TRS_Editor']/p/text()")
            if not content:
                _str = ""
                content = x_html.xpath('//*[@class="Custom_UnionStyle"]/p/text()')
                _content = "".join(content).strip()
            else:
                _content = "".join(content).strip()
            if not title or not content:
                return
            publish_time = x_html.xpath("//*[@id='articleTime']/text()")
            _publish_time = china_news_str_to_format_time(publish_time)
            source = x_html.xpath('//*[@id="articleSource"]/text()')
            if source:
                source = "".join(source)
                try:
                    _source = re.findall(r"来源.(.*)", source)[0].strip()
                except:
                    pass
            editor = x_html.xpath('//*[@id="articleText"]/p/text()')
            if editor:
                editor = "".join(editor)
                try:
                    _editor = re.findall(r"责任编辑：(.*)）", editor)[0]
                except:
                    pass
            data = dict(
                title=_title,  # 标题
                id=article_id,  # 文章id
                time=_publish_time,  # 发布时间
                source=_source,  # 来源
                author=_editor,  # 责任编辑
                link=news_url,  # url连接
                type=NEWS_ES_TYPE.china_economy,
                contents=_content,  # 内容
                crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")  # 爬取时间
            )
            SaveDataToEs.save_one_data_to_es(ALL_NEWS_DETAILS, data, article_id)
        except Exception as e:
            logger.exception(e)


def get_handler(*args, **kwargs):
    return ChinaEconomySpider(*args, **kwargs)


def china_economy_run():
    detail_list = []
    data = {
        "siteName": "中国经济网",
        "domain": "http://www.ce.cn/",
        "startURL": [
            "http://www.ce.cn/"
        ],
        "website_index": "all_news_details",
        "id": "",
        "thread": "1",
        "retry": "2",
        "sleep": "0",
        "maxPageGather": "10",
        "timeout": "5000",
        "contentReg": "",
        "contentXPath": "//*[@class='TRS_Editor']/p/text()",
        "titleReg": "",
        "titleXPath": '//*[@id="articleTitle"]/text()',
        "categoryReg": "",
        "categoryXPath": "",
        "defaultCategory": "",
        "urlReg": "http://\\w+\\.people.com.cn/\d+/\d+-\d+/\d+.shtml",
        "charset": "",
        "publishTimeXPath": "//*[@id='articleTime']/text()",
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
    china = ChinaEconomySpider(data)
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
    china_economy_run()
