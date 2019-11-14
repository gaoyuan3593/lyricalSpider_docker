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
from service.micro.utils.math_utils import chinadaily_str_to_format_time
from service.micro.news import CHINA_DAILY, NEWS_ES_TYPE
from service.micro.news.utils.search_es import SaveDataToEs


class ChinaDailySpider(object):
    __name__ = 'china daily news'

    def __init__(self, data):
        self.domain = data.get("domain")
        self.s = requests.session()
        self.es_index = data.get("website_index")

    def random_num(self):
        return random.uniform(0.1, 0.5)

    def use_proxies(self):
        self.s.proxies = get_proxies()

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_news_all_url(self):
        logger.info('Processing get china daily news list!')
        headers = {
            'User-Agent': ua(),
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9'
        }
        url_list = []
        try:
            response = self.s.get(self.domain, headers=headers)
            if "中国日报网-传播中国，影响世界" in response.text:
                for url in CHINA_DAILY:
                    _url_list = re.findall(r"{}\d+/\d+/\w+.html".format(url), response.text)
                    url_list.extend(["http:" + i for i in _url_list])
            return list(set(url_list))
        except Exception as e:
            raise InvalidResponseError

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_news_detail(self, url):
        logger.info('Processing get china daily news details !!!')
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
            'Proxy-Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 'cn.chinadaily.com.cn'
        }
        try:
            response = self.s.get(url, headers=headers, verify=False)
            if response.status_code == 200:
                logger.info("get china daily news detail success url: {}".format(url))
                article_id = url.split("/")[-1].split(".")[0]
                return dict(article_id=article_id, resp=response.text, news_url=url)
            elif response.status_code in [503, 504, 403, 502, 404]:
                return
            else:
                logger.error("get china daily news detail failed")
                raise InvalidResponseError
        except Exception as e:
            raise InvalidResponseError

    def parse_news_detail(self, _data):
        if not _data:
            return
        resp = _data.get("resp")
        news_url = _data.get("news_url")
        article_id = _data.get("article_id")
        _content, _editor, _source = "", "", "中国日报网"
        _publish_time = (datetime.now() + timedelta(minutes=-10)).strftime("%Y-%m-%d %H:%M")
        try:
            x_html = etree.HTML(resp)
            title = x_html.xpath('//*[@class="dabiaoti"]/text()') or \
                    x_html.xpath('//*[@id="artBox"]/h1/text()')
            _title = str(title[0]).strip() if title else ""
            content = x_html.xpath("//*[@id='Content']/p/text()")
            if not content:
                _str = ""
                content = x_html.xpath('//*[@class="article"]/p/text()')
                _content = "".join(content).strip()
            else:
                _content = "".join(content).strip()
            if not title or not content:
                return
            publish_time = x_html.xpath("//*[@class='xinf-le']/text()")
            _publish_time = chinadaily_str_to_format_time(publish_time)
            fenx = ",".join(publish_time)
            if "来源" in fenx:
                try:
                    _source = re.findall(r"来源.(.*),", fenx)[0].strip()
                except:
                    pass
            if "作者" in fenx:
                try:
                    _editor = re.findall(r"作者.(.*)", fenx)[0].strip()
                except:
                    pass
            data = dict(
                title=_title,  # 标题
                article_id=article_id,  # 文章id
                date=_publish_time,  # 发布时间
                source=_source,  # 来源
                editor=_editor,  # 责任编辑
                news_url=news_url,  # url连接
                new_type=NEWS_ES_TYPE.china_daily,
                type="detail_type",
                contents=_content,  # 内容
                crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")  # 爬取时间
            )
            SaveDataToEs.save_one_data_to_es(self.es_index, data, article_id)
        except Exception as e:
            logger.exception(e)


def get_handler(*args, **kwargs):
    return ChinaDailySpider(*args, **kwargs)


def china_daily_run():
    detail_list = []
    data = {
        "siteName": "中国日报网",
        "domain": "http://cn.chinadaily.com.cn/",
        "startURL": [
            "http://cn.chinadaily.com.cn/"
        ],
        "website_index": "all_news_details",
        "id": "",
        "thread": "1",
        "retry": "2",
        "sleep": "0",
        "maxPageGather": "10",
        "timeout": "5000",
        "contentReg": "",
        "contentXPath": "//*[@id='Content']/p/text()",
        "titleReg": "",
        "titleXPath": '//*[@class="dabiaoti"]/text()',
        "categoryReg": "",
        "categoryXPath": "",
        "defaultCategory": "",
        "urlReg": "http://\\w+\\.people.com.cn/\d+/\d+-\d+/\d+.shtml",
        "charset": "",
        "publishTimeXPath": "//*[@class='xinf-le']/text()",
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
    china = ChinaDailySpider(data)
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
    china_daily_run()
