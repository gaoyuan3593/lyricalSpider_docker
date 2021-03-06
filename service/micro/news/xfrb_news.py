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
from service.micro.news import XFRB_NEWS, NEWS_ES_TYPE
from service.db.utils.elasticsearch_utils import ALL_NEWS_DETAILS, NEWS_DETAIL_MAPPING
from service.micro.news.utils.search_es import SaveDataToEs

_index_mapping = {
    NEWS_ES_TYPE.xfrb_news:
        {
            "properties": NEWS_DETAIL_MAPPING
        }
}


class XFRBSpider(object):
    __name__ = 'xiao fei ri bao news'

    def __init__(self, data):
        self.domain = data.get("domain")
        self.s = requests.session()
        SaveDataToEs.create_index(ALL_NEWS_DETAILS, _index_mapping)

    def random_num(self):
        return random.uniform(0.1, 0.5)

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_news_all_url(self):
        logger.info('Processing get xiao fei ri bao news list!')
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
            if "消费日报网--贴近民生 服务百姓" in response.text:
                for url in XFRB_NEWS:
                    parms = r"{}\d+.html".format(url, url, url)
                    _url_list = re.findall(parms, response.text)

                    url_list.extend(["http://www.xfrb.com.cn" + _str for _str in _url_list])
            else:
                raise InvalidResponseError
            return list(set(url_list))
        except Exception as e:
            time.sleep(1)
            raise InvalidResponseError

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_news_detail(self, url):
        logger.info('Processing get xiao fei ri bao news details !!!')
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
                logger.info("get xiao fei ri bao news detail success url: {}".format(url))
                article_id = url.split("/")[-1].split(".")[0]
                return dict(article_id=article_id, resp=response.text, news_url=url)
            elif response.status_code == 403:
                pass
            else:
                logger.error("get xiao fei ri bao news detail failed")
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
        _content, _editor, _source = "", "", "消费日报网"
        _publish_time = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")
        try:
            x_html = etree.HTML(resp)
            title = x_html.xpath('//*[@class="margin-top-15"]/text()')
            if not title:
                title = x_html.xpath('//*[@class="margin-top-15"]/text()')
            _title = "".join(title).strip()
            content = x_html.xpath('//*[@class="cont"]/p/text()')
            if not "".join(content).split():
                content = x_html.xpath('//*[@class="cont"]/p/span/text()')
                _content = "".join(content).strip()
            else:
                _content = "".join(content).strip()
            if not title or not _content:
                return
            publish_time = x_html.xpath('//*[@class="cite"]/cite/text()')
            if publish_time:
                publish_time = "".join(publish_time).strip()
                try:
                    _publish_time = re.findall(r"(\d+-\d+-\d+ \d+:\d+)", publish_time)[0]
                    _publish_time = datetime.strptime(_publish_time, "%Y-%m-%d %H:%M")
                except:
                    pass
            try:
                _source = "".join(x_html.xpath('//*[@class="cite"]/cite/text()')[1])
            except:
                pass
            editor = x_html.xpath('//*[@class="label_editor"]/span/text()')
            if editor:
                _editor = "".join(editor).strip()
            data = dict(
                title=_title,  # 标题
                id=article_id,  # 文章id
                time=_publish_time,  # 发布时间
                source=_source,  # 来源
                author=_editor,  # 责任编辑
                link=news_url,  # url连接
                type=NEWS_ES_TYPE.xfrb_news,
                contents=_content,  # 内容
                crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")  # 爬取时间
            )
            SaveDataToEs.save_one_data_to_es(ALL_NEWS_DETAILS, data, article_id)
        except Exception as e:
            logger.exception(e)


def get_handler(*args, **kwargs):
    return XFRBSpider(*args, **kwargs)


def xfrb_news_run():
    detail_list = []
    data = {
        "siteName": "消费日报网",
        "domain": "http://www.xfrb.com.cn/",
        "startURL": [
            "http://www.xfrb.com.cn/"
        ],
        "website_index": "all_news_details",
        "id": "",
        "thread": "1",
        "retry": "2",
        "sleep": "0",
        "maxPageGather": "10",
        "timeout": "5000",
        "contentReg": "",
        "contentXPath": "//*[@class='content_div']/p/text()",
        "titleReg": "",
        "titleXPath": '//*[@class="title"]/text()',
        "categoryReg": "",
        "categoryXPath": "",
        "defaultCategory": "",
        "urlReg": "http://\\w+\\.people.com.cn/\d+/\d+-\d+/\d+.shtml",
        "charset": "",
        "publishTimeXPath": '/html/body/div/div/h3/text()',
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
    spider = XFRBSpider(data)
    try:
        news_url_list = spider.get_news_all_url()
    except Exception as e:
        logger.exception(e)
        return
    for dic in news_url_list:
        try:
            detail_list.append(spider.get_news_detail(dic))
        except:
            continue
    for _data in detail_list:
        spider.parse_news_detail(_data)


if __name__ == '__main__':
    xfrb_news_run()
