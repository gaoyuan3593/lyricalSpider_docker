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
from service.micro.news import NEWS_ES_TYPE
from service.micro.news.utils.search_es import SaveDataToEs


class LegalDailySpider(object):
    __name__ = 'inewsweek news'

    def __init__(self, data):
        self.domain = data.get("domain")
        self.s = requests.session()

    def random_num(self):
        return random.uniform(0.1, 0.5)

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_news_all_url(self):
        logger.info('Processing get inewsweek news list!')
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
            if "中国新闻周刊" in response.text:
                for i in range(1, 100):
                    data_list = self.get_page_data(i)
                    url_list.extend(data_list)
            else:
                raise InvalidResponseError
            return url_list
        except Exception as e:
            time.sleep(1)
            raise InvalidResponseError

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_page_data(self, num):
        url = "http://channel.inewsweek.chinanews.com/u/zk.shtml?pager={}&pagenum=20".format(num)
        headers = {
            'User-Agent': ua(),
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9'
        }
        _list = []
        try:
            resp = self.s.get(url, headers=headers, verify=False).text
            if "specialcnsdata" in resp:
                logger.info("get page data success url : {}".format(url))
                r = re.findall(r"specialcnsdata = (.*);", resp)[0]
                data = json.loads(r).get("docs")
                for dic in data:
                    _list.append(
                        dict(
                            pubtime=dic.get("pubtime"),
                            article_id=dic.get("id"),
                            title=dic.get("title"),
                            news_url=dic.get("url")
                        )
                    )
        except Exception as e:
            raise InvalidResponseError
        return _list

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_news_detail(self, dic):
        logger.info('Processing get inewsweek news details !!!')
        headers = {
            'User-Agent': ua(),
            'Proxy-Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': "www.inewsweek.cn"
        }
        url = dic.get("news_url")
        try:
            response = self.s.get(url, headers=headers, verify=False)
            if response.status_code == 200:
                response.encoding = "gb2312"
                logger.info("get inewsweek news detail success url: {}".format(url))
                dic.update(resp=response.text)
                return dic
            else:
                logger.error("get inewsweek news detail failed")
                raise InvalidResponseError
        except Exception as e:
            time.sleep(1)
            self.s.proxies = get_proxies()
            raise InvalidResponseError

    def parse_news_detail(self, _data):
        if not _data:
            return
        resp = _data.get("resp")
        _content, _editor, _source = "", "", "中国新闻周刊"
        try:
            x_html = etree.HTML(resp)
            if not x_html:
                return
            title = _data.get("title")
            content = x_html.xpath("//*[@class='contenttxt']/p/text()")
            if not content:
                _str = ""
                content = x_html.xpath('//*[@class="contenttxt"]/p/span/text()') or \
                          x_html.xpath('//*[@class="contenttxt"]/div/text()')
                _content = "".join(content).strip()
            else:
                _content = "".join("".join(content).strip().split())
            if not title or not content:
                return
            editor = re.findall(r"责任编辑：(.*)", resp)
            if editor:
                _str = "".join(editor)
                if "</p>" in _str:
                    _editor = _str.split("</p>")[0]
                else:
                    _editor = editor[0]
            article_id = _data.get("article_id")
            date_time = _data.get("pubtime")
            try:
                _publish_time = datetime.strptime(date_time[:-3], "%Y-%m-%d %H:%M")
            except:
                _publish_time = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")
            data = dict(
                title=title,  # 标题
                article_id=article_id,  # 文章id
                date=_publish_time,  # 发布时间
                source=_source,  # 来源
                editor=_editor,  # 责任编辑
                news_url=_data.get("news_url"),  # url连接
                type=NEWS_ES_TYPE.inewsweek,
                contents=_content,  # 内容
                crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")  # 爬取时间
            )
            dic = {"article_id": article_id}
            SaveDataToEs.save_one_data_to_es(data, dic)
        except Exception as e:
            logger.exception(e)


def inewsweek_run():
    from service.micro.utils.threading_ import WorkerThread
    detail_list = []
    data = {
        "siteName": "中国新闻周刊",
        "domain": "http://www.inewsweek.cn/",
        "startURL": [
            "http://www.inewsweek.cn/"
        ],
        "id": "",
        "thread": "1",
        "retry": "2",
        "sleep": "0",
        "maxPageGather": "10",
        "timeout": "5000",
        "contentReg": "",
        "contentXPath": "//*[@class='contenttxt']/p/text()",
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
    threads = []
    china = LegalDailySpider(data)
    try:
        news_url_list = china.get_news_all_url()
    except Exception as e:
        logger.exception(e)
        return
    for dic in news_url_list:
        # try:
        #     detail_list.append(china.get_news_detail(dic))
        # except:
        #     continue
        worker = WorkerThread(detail_list, china.get_news_detail, (dic,))
        worker.start()
        threads.append(worker)
    for work in threads:
        work.join(1)
        if work.isAlive():
            logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
            threads.append(work)
    threads = []
    for _data in detail_list:
        worker = WorkerThread([], china.parse_news_detail, (_data,))
        worker.start()
        threads.append(worker)
    for work in threads:
        work.join(1)
        if work.isAlive():
            logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
            threads.append(work)


if __name__ == '__main__':
    inewsweek_run()
