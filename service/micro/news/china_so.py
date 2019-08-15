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
from service.micro.news.utils.proxies_util import get_proxies
from service.micro.news import NEWS_ES_TYPE
from service.micro.news.utils.search_es import SaveDataToEs
from service.micro.utils.threading_parse import WorkerThreadParse


class ChinaSoSpider(object):
    __name__ = 'china so suo news'

    def __init__(self, data):
        self.domain = data.get("domain")
        self.s = requests.session()

    def random_num(self):
        return random.uniform(0.1, 0.5)

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_news_all_url(self):
        logger.info('Processing get china sou suo news list!')
        headers = {
            'User-Agent': ua(),
            'Connection': 'keep-alive',
            'Accept': 'text/html, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 'www.chinaso.com',
            'Referer': 'http://www.chinaso.com/'
        }
        url_list = []
        try:
            for i in range(2, 21):
                url = "{}in/tabtoutiao/index_{}.shtml".format(self.domain, i)
                response = self.s.get(url, headers=headers, verify=False)
                response.encoding = "utf-8"
                if "内容列表" in response.text:
                    logger.info("get_news_all_url success url : {}".format(url))
                    soup = BeautifulSoup(response.text, "lxml")
                    div_list = soup.find_all("div", attrs={"class": "all_list toutiao_l_list"})
                    div_list2 = soup.find_all("div", attrs={"class": "news-sum-div clearb toutiao_l_list"})
                    if div_list2:
                        div_list.extend(div_list2)
                    url_list.extend([tag.find("a").attrs.get("href") for tag in div_list if
                                     "image_detail" not in tag.find("a").attrs.get("href")])
                else:
                    continue
            return list(set(url_list))
        except Exception as e:
            time.sleep(1)
            # self.use_proxies()
            raise InvalidResponseError

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_news_detail(self, url):
        logger.info('Processing get china so news details !!!')
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
                logger.info("get china so news detail success url: {}".format(url))
                article_id = url.split("/")[-1].split(".")[0]
                return dict(article_id=article_id, resp=response.text, news_url=url)
            else:
                logger.error("get china sou suo news detail failed")
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
        _content, _editor, _source = "", "", "中国搜索"
        _publish_time = datetime.now() + timedelta(minutes=-10)
        try:
            x_html = etree.HTML(resp)
            title = x_html.xpath('//*[@class="detail-title"]/text()') or \
                    x_html.xpath('//*[@class="t_newsinfo"]/text()') or \
                    x_html.xpath('//*[@class="xwzx_wname01"]/text()') or \
                    x_html.xpath('//*[@class="h-title"]/text()')
            _title = str(title[0]).strip() if title else ""
            content = x_html.xpath("//*[@class='detail-main']/p/text()")
            if not content:
                _str = ""
                soup = BeautifulSoup(resp, "lxml"). \
                    find("div", attrs={"class": "news_part news_part_limit"})
                if soup:
                    content = soup.text.split("责任编辑：")[0].strip()
                else:
                    content = x_html.xpath('//*[@class="xwzx_wname02"]/p/text()') or \
                              x_html.xpath('//*[@id="p-detail"]/p/text()')

                _content = "".join(content).strip()
            else:
                _content = "".join("".join(content).strip().split())
            if not title or not content:
                return
            publish_time = x_html.xpath('//*[@class="detail-time"]/span/text()') or \
                           x_html.xpath('//*[@class="h-time"]/text()')
            if publish_time:
                publish_time = "".join(publish_time).strip()
                try:
                    _publish_time = re.findall(r"\d+-\d+-\d+ \d+:\d+", publish_time)[0]
                except Exception as e:
                    pass
            source = x_html.xpath('//*[@class="detail-time"]/span[2]/a/text()') or \
                     x_html.xpath('//*[@class="about_news"]/text()') or \
                     x_html.xpath('//*[@class="h-info"]/span[2]/text()')
            if source:
                source = "".join(source)
                try:
                    if "来源" not in source:
                        _source = source
                    else:
                        _source = re.findall(r"来源.(.*)", source)[0].strip()
                except:
                    pass
            editor = x_html.xpath('//*[@class="editor"]/text()') or \
                     x_html.xpath('//*[@class="infor_item"]/text()')
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
                type=NEWS_ES_TYPE.china_so,
                contents=_content,  # 内容
                crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")  # 爬取时间
            )
            dic = {"article_id": article_id}
            SaveDataToEs.save_one_data_to_es(data, dic)
        except Exception as e:
            logger.exception(e)


def china_so_run():
    detail_list = []
    threads = []
    data = {
        "siteName": "中国搜索",
        "domain": "http://www.chinaso.com/",
        "startURL": [
            "http://www.chinaso.com/"
        ],
        "id": "",
        "thread": "1",
        "retry": "2",
        "sleep": "0",
        "maxPageGather": "10",
        "timeout": "5000",
        "contentReg": "",
        "contentXPath": "//*[@class='detail-main']/p/text()",
        "titleReg": "",
        "titleXPath": '//*[@class="detail-title"]/text()',
        "categoryReg": "",
        "categoryXPath": "",
        "defaultCategory": "",
        "urlReg": "http://\\w+\\.people.com.cn/\d+/\d+-\d+/\d+.shtml",
        "charset": "",
        "publishTimeXPath": '//*[@class="detail-time"]/span/text()',
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
    china = ChinaSoSpider(data)
    try:
        news_url_list = china.get_news_all_url()
    except Exception as e:
        logger.exception(e)
        return
    for url in news_url_list:
        #detail_list.append(china.get_news_detail(url))
        worker = WorkerThreadParse(detail_list, china.get_news_detail, (url,))
        worker.start()
        threads.append(worker)
    for work in threads:
        work.join(1)
        if work.isAlive():
            logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
            threads.append(work)
    threads = []
    for _data in detail_list:
        # china.parse_news_detail(_data)
        worker = WorkerThreadParse([], china.parse_news_detail, (_data,))
        worker.start()
        threads.append(worker)
    for work in threads:
        work.join(1)
        if work.isAlive():
            logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
            threads.append(work)


if __name__ == '__main__':
    china_so_run()
