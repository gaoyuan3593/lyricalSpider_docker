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
from service.micro.news import HAI_WAI_NET, NEWS_ES_TYPE
from service.micro.news.utils.search_es import SaveDataToEs


class HaiWaiNetSpider(object):
    __name__ = 'hai wai net news'

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
        logger.info('Processing get hai wai net news list!')
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
            if "海外网_人民日报海外版官方网站_全球华人的网上家园" in response.text:
                for url in HAI_WAI_NET:
                    parms = r"{}n/\d+/\d+/\w+-\w+.html".format(url)
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
        logger.info('Processing get hai wai net news details !!!')
        headers = {
            'User-Agent': ua(),
            'Proxy-Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': url.split("/")[2]
        }
        try:
            response = self.s.get(url, headers=headers, verify=False)
            if response.status_code == 200:
                response.encoding = "utf-8"
                logger.info("get hai wai net news detail success url: {}".format(url))
                article_id = url.split("/")[-1].split(".")[0]
                return dict(article_id=article_id, resp=response.text, news_url=url)
            else:
                logger.error("get hai wai net news detail failed")
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
        _content, _editor, _source = "", "", "海外网"
        _publish_time = datetime.now() + timedelta(minutes=-10)
        try:
            x_html = etree.HTML(resp)
            if not x_html:
                return
            title = x_html.xpath('//*[@class="show_wholetitle"]/text()') or \
                    x_html.xpath('/html/body/div/h1/text()')
            _title = str(title[0]).strip() if title else ""
            content = x_html.xpath("//*[@class='contentMain']/p/text()")
            if not content:
                _str = ""
                content = x_html.xpath('//*[@class="des"]/p[1]/text()') or \
                          x_html.xpath('//*[@class="des"]/text()')
                _content = "".join(content).strip()
            else:
                _content = "".join("".join(content).strip().split())
            if not title or not content:
                return
            publish_time = x_html.xpath('//*[@class="first"]/text()') or \
                           x_html.xpath('//*[@class="newsMess"]/span[1]/text()')
            if publish_time:
                _time = "".join(publish_time)
                _publish_time = re.findall(r"\d+-\d+-\d+ \d+:\d+", _time)[0]
                _publish_time = datetime.strptime(_publish_time, "%Y-%m-%d %H:%M")
            source = x_html.xpath('//*[@class="contentExtra"]/span[2]/text()') or \
                     x_html.xpath('//*[@class="newsMess"]/span[2]/text()')
            if source:
                source = "".join(source)
                try:
                    if "来源" not in source:
                        _source = source
                    else:
                        _source = re.findall(r"来源.(.*)", source)[0].strip()
                except:
                    _source = re.findall(r"来自.(.*)", source)[0].strip()
            editor = x_html.xpath('//*[@class="writer"]/text()') or \
                     x_html.xpath('//*[@class="des"]/p[2]/text()')
            if editor:
                editor = "".join(editor).strip()
                try:
                    editor = re.findall(r"责编：(.*)", editor)
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
                type=NEWS_ES_TYPE.haiwai_net,
                contents=_content,  # 内容
                crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")  # 爬取时间
            )
            SaveDataToEs.save_one_data_to_es(self.es_index, data, article_id)
        except Exception as e:
            logger.exception(e)


def get_handler(*args, **kwargs):
    return HaiWaiNetSpider(*args, **kwargs)


def haiwai_net_run():
    detail_list = []
    data = {
        "siteName": "海外网",
        "domain": "http://www.haiwainet.cn/",
        "startURL": [
            "http://www.haiwainet.cn/"
        ],
        "website_index": "all_news_details",
        "id": "",
        "thread": "1",
        "retry": "2",
        "sleep": "0",
        "maxPageGather": "10",
        "timeout": "5000",
        "contentReg": "",
        "contentXPath": "//*[@class='contentMain']/p/text()",
        "titleReg": "",
        "titleXPath": '//*[@class="show_wholetitle"]/text()',
        "categoryReg": "",
        "categoryXPath": "",
        "defaultCategory": "",
        "urlReg": "http://\\w+\\.people.com.cn/\d+/\d+-\d+/\d+.shtml",
        "charset": "",
        "publishTimeXPath": '//*[@class="first"]/text()',
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
    china = HaiWaiNetSpider(data)
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
    haiwai_net_run()
