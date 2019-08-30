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
from service.micro.news.utils.proxies_util import get_proxies
from service.micro.news import DANG_JIAN, NEWS_ES_TYPE
from service.micro.news.utils.search_es import SaveDataToEs


class DangJianSpider(object):
    __name__ = 'dang jian news'

    def __init__(self, data):
        self.domain = data.get("domain")
        self.s = requests.session()
        self.es_index = data.get("website_index")

    def use_proxies(self):
        self.s.proxies = get_proxies()

    def random_num(self):
        return random.uniform(0.1, 0.5)

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_news_all_url(self):
        logger.info('Processing get dang jian news list!')
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
            if "党建网 - 中宣部主管全国性党建网站" in response.text:
                for url in DANG_JIAN:
                    parms = r"{}\d+/\w+_\d+.shtml".format(url)
                    _url_list = re.findall(parms, response.text)
                    url_list.extend(["http://www.dangjian.cn" + i for i in _url_list])
            else:
                raise InvalidResponseError
            return list(set(url_list))
        except Exception as e:
            time.sleep(1)
            self.use_proxies()
            raise InvalidResponseError

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_news_detail(self, url):
        logger.info('Processing get dang jian news details !!!')
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
                response.encoding = "utf-8"
                logger.info("get dang jian news detail success url: {}".format(url))
                article_id = url.split("/")[-1].split(".")[0]
                return dict(article_id=article_id, resp=response.text, news_url=url)
            else:
                logger.error("get dang jian news detail failed")
                raise InvalidResponseError
        except Exception as e:
            time.sleep(1)
            self.use_proxies()
            raise InvalidResponseError

    def parse_news_detail(self, _data):
        if not _data:
            return
        resp = _data.get("resp")
        news_url = _data.get("news_url")
        article_id = _data.get("article_id")
        _content, _editor, _source = "", "", "党建网"
        _publish_time = datetime.now() + timedelta(minutes=-10)
        try:
            x_html = etree.HTML(resp)
            title = x_html.xpath('//*[@id="title_tex"]/text()') or \
                    x_html.xpath('//*[@id="title_tex"]/strong/text()')
            _title = str(title[0]).strip() if title else ""
            content = x_html.xpath("//*[@class='TRS_Editor']/p/text()")
            if not content:
                _str = ""
                content = x_html.xpath('//*[@class="Custom_UnionStyle"]/p/text()') or \
                          x_html.xpath('//*[@class="Custom_UnionStyle"]/div/p/span/text()') or \
                          x_html.xpath('//*[@id="tex"]/div/div/div/span/div/p/text()') or \
                          x_html.xpath('//*[@id="article_inbox"]/p/text()')
                _content = "".join(content).strip()
            else:
                _content = "".join("".join(content).strip().split())
            if not title or not content:
                return
            publish_time = x_html.xpath('//*[@id="time_tex"]/text()') or \
                           x_html.xpath('//*[@id="apublishtime"]/text()')
            if publish_time:
                _time = "".join(publish_time)
                publish_time = re.findall(r"\d+-\d+-\d+", _time)[0]
                _publish_time = publish_time + datetime.now().strftime(" %H:%M")
                _publish_time = datetime.strptime(_publish_time, "%Y-%m-%d %H:%M")
            source = x_html.xpath('//*[@id="time_ly"]/text()')
            if source:
                source = "".join(source)
                try:
                    if "来源" not in source:
                        _source = source
                    else:
                        _source = re.findall(r"来源.(.*)", source)[0].strip()
                except:
                    pass
            editor = x_html.xpath('//*[@class="bj"]/text()')
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
                contents=_content,  # 内容
                crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")  # 爬取时间
            )
            SaveDataToEs.save_one_data_to_es(self.es_index, data, article_id)
        except Exception as e:
            logger.exception(e)


def get_handler(*args, **kwargs):
    return DangJianSpider(*args, **kwargs)


def dangjian_run():
    detail_list = []
    data = {
        "siteName": "党建网",
        "domain": "http://www.dangjian.cn/",
        "startURL": [
            "http://www.dangjian.cn/"
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
        "titleXPath": '//*[@id="title_tex"]/text()',
        "categoryReg": "",
        "categoryXPath": "",
        "defaultCategory": "",
        "urlReg": "http://\\w+\\.people.com.cn/\d+/\d+-\d+/\d+.shtml",
        "charset": "",
        "publishTimeXPath": '//*[@id="time_tex"]/text()',
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
    china = DangJianSpider(data)
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
    dangjian_run()
