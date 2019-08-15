#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random
import time
import json
import re
import requests
from lxml import etree
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from service.exception import retry
from service.exception.exceptions import *
from service import logger
from service.micro.utils import ua
from service.micro.utils.math_utils import china_news_str_to_format_time
from service.micro.news import NEWS_ES_TYPE
from service.micro.news.utils.search_es import SaveDataToEs


class CctvWorldSpider(object):
    __name__ = 'cctv world news'

    def __init__(self, data):
        self.domain = data.get("domain")
        self.s = requests.session()

    def random_num(self):
        return random.uniform(0.1, 0.5)

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_news_all_url(self):
        logger.info('Processing get cctv world news list!')
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
            if "央视国际网" in response.text:
                soup = BeautifulSoup(response.text, "lxml")
                _url_list = soup.find("center").find_all("table")[3].contents[1::2]
                for tr in _url_list:
                    _url = "http://www.cctv.com"
                    if tr.find("td", attrs={"class": True}):
                        if _url in tr.contents[2].find("a").attrs.get("href"):
                            detail_url = tr.contents[2].find("a").attrs.get("href")
                        else:
                            detail_url = _url + tr.contents[2].find("a").attrs.get("href")
                        url_list.append(
                            dict(
                                url=detail_url,
                                title=tr.contents[2].text.strip()
                            )
                        )
            return url_list
        except Exception as e:
            raise InvalidResponseError

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_news_detail(self, dic):
        logger.info('Processing get cctv world news details !!!')
        url = dic.get("url")
        title = dic.get("title")
        headers = {
            'User-Agent': ua(),
            'Proxy-Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 'www.cctv.com'
        }
        try:
            response = self.s.get(url, headers=headers, verify=False)
            response.encoding = "gb2312"
            if response.status_code == 200:
                logger.info("get cctv world news detail success url: {}".format(url))
                article_id = url.split("ttxw/")[-1].split(".")[0]
                return dict(article_id=article_id, resp=response.text, news_url=url, title=title)
            else:
                logger.error("get cctv world news detail failed")
                raise InvalidResponseError
        except Exception as e:
            raise InvalidResponseError

    def parse_news_detail(self, _data):
        if not _data:
            return
        resp = _data.get("resp")
        news_url = _data.get("news_url")
        article_id = _data.get("article_id")
        _content, _editor, _source = "", "", "央视国际网"
        _publish_time = datetime.now() + timedelta(minutes=-10)
        try:
            x_html = etree.HTML(resp)
            _title = _data.get("title")
            content = x_html.xpath("//*[@class='setfont14']/text()")
            if not content:
                content = x_html.xpath('//*[@class="setfont14"]/text()')
            _content = "".join(content).strip().replace("\r\n", "")
            if not content:
                return
            try:
                publish_time = re.findall(r"(\d+年\d+月\d+日)", resp)[0]
                _publish_time = china_news_str_to_format_time(publish_time)
            except:
                pass
            data = dict(
                title=_title,  # 标题
                article_id=article_id,  # 文章id
                date=_publish_time,  # 发布时间
                source=_source,  # 来源
                editor=_editor,  # 责任编辑
                news_url=news_url,  # url连接
                type=NEWS_ES_TYPE.cctv_word,
                contents=_content,  # 内容
                crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")  # 爬取时间
            )
            dic = {"article_id": article_id}
            SaveDataToEs.save_one_data_to_es(data, dic)
        except Exception as e:
            logger.exception(e)


def cctv_worl_run():
    detail_list = []
    data = {
        "siteName": "央视国际网",
        "domain": "http://www.cctv.com/news/ttxw/wrtt.html",
        "startURL": [
            "http://www.cctv.com/news/ttxw/wrtt.html"
        ],
        "id": "",
        "thread": "1",
        "retry": "2",
        "sleep": "0",
        "maxPageGather": "10",
        "timeout": "5000",
        "contentReg": "",
        "contentXPath": "//*[@class='setfont14']/text()",
        "titleReg": "",
        "titleXPath": '//html/body/div/h1/text()',
        "categoryReg": "",
        "categoryXPath": "",
        "defaultCategory": "",
        "urlReg": "http://\\w+\\.people.com.cn/\d+/\d+-\d+/\d+.shtml",
        "charset": "",
        "publishTimeXPath": "//*[@id='pubtime_baidu']/text()",
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
    cctv = CctvWorldSpider(data)
    try:
        news_url_list = cctv.get_news_all_url()
    except Exception as e:
        logger.exception(e)
        return
    for dic in news_url_list:
        try:
            detail_list.append(cctv.get_news_detail(dic))
        except:
            continue
    for _data in detail_list:
        cctv.parse_news_detail(_data)


if __name__ == '__main__':
    cctv_worl_run()
