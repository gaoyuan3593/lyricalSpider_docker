#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random
import time
import pandas as pd
import requests
from service.core.utils.http_ import Requester
from service.exception import retry
from service.exception.exceptions import *
from service import logger
from service.micro.utils import ua
from service.micro.utils.cookie_utils import dict_to_cookie_jar, cookie_jar_to_dict
from lxml import etree
from datetime import datetime
from service.micro.utils.threading_ import WorkerThread


class CgtnSpider(object):
    __name__ = 'cgtn spider'

    def __init__(self, keyword):
        self.keyword = keyword
        self.requester = Requester

    def random_num(self):
        return random.uniform(0.1, 1)

    @retry(max_retries=7, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_fox_data(self):
        """
        获取推特的人物首页
        :return: dict
        """
        logger.info('Processing get fox news key word ！')
        url_list = []
        url = "https://api.cgtn.com/website/api/search/news"
        headers = {
            "Connection": "keep-alive",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Content-Type": "application/json",
            "Origin": "https://www.cgtn.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
            "Host": "api.cgtn.com",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Referer": "https://www.cgtn.com/search?keyword={}".format(self.keyword.replace(" ", "%20"))
        }
        data = {
            "keyword": "us china trade war",
            "dateSort": "false",
            "curPage": 0,
            "pageSize": 10
        }
        try:
            resp = self.requester.post(url, header_dict=headers, data_dict=data, submission_type="json")
            print(resp.json())
            if resp.status_code == 200:
                result = resp.json()
                num = result.get("numFound") // 10 + 1
                page = 0
                for i in range(num):
                    url = "https://api.foxnews.com/v1/content/search?q={}&fields=date%2Cdescription%2Ctitle%2Curl%2Cimage%2Ctype%2Ctaxonomy&section.path=fnc&start={}".format(
                        self.keyword.replace(" ", "%20AND%20"), page)
                    url_list.append(url)
                    page += 10
                return url_list
            else:
                raise HttpInternalServerError
        except Exception as e:
            # self.requester.use_proxy()
            raise HttpInternalServerError

    @retry(max_retries=7, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_fox_page_data(self, url):
        headers = {
            'user-Agent': ua(),
            'connection': 'keep-alive',
            "content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-Encoding': 'gzip, deflate',
        }
        try:
            resp = self.requester.get(url, header_dict=headers)
            if resp.status_code == 200:
                resp_dic = resp.json().get("response")
                return resp_dic
        except Exception as e:
            #self.requester.use_proxy()
            raise HttpInternalServerError

    @retry(max_retries=7, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_article_data(self, acticle_data):
        url = acticle_data.get("url")
        headers = {
            'user-Agent': ua(),
            'connection': 'keep-alive',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9'
        }
        try:
            resp = self.requester.get(url, header_dict=headers)
            if resp.status_code == 200:
                x_html = etree.HTML(resp.text)
                content = x_html.xpath('//*[@class="article-body"]/p/text()')
                if not content:
                    print(content)
                content = "".join(content)
                acticle_data.update(contents=content)
                del acticle_data["url"]
            return acticle_data
        except Exception as e:
            #self.requester.use_proxy()
            raise HttpInternalServerError

    def parse_acticle_url(self, data):
        dic_list, img_list = [], []
        for dic in data:
            dosc_list = dic.get("docs")
            for _data in dosc_list:
                if _data.get("type") == "article":
                    _str = _data.get("date")
                    _date = self.parse_date(_str)
                    if not _date:
                        continue
                    title = _data.get("title")
                    _url = _data.get("url")
                    url = "".join(_url[0] if len(_url) > 1 else _url)
                    desc = _data.get("description")
                    old_img_list = _data.get("image")
                    if old_img_list:
                        img_list = [i.get("url") for i in old_img_list if i]
                else:
                    continue
                dic_list.append(dict(
                    title=title,
                    date=_date,
                    url=url,
                    desc=desc,
                    img_list=img_list,
                    keyword=self.keyword
                ))
        return dic_list

    def parse_date(self, _str):
        if not _str:
            return False
        date = datetime.strptime(_str, "%Y-%m-%dT%H:%M:%SZ")  #
        if date.year >= 2018 and date.month >= 1 and date.day >= 1:
            return date.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return False


def save_data_to_excel(data_list):
    print("Being data save to excel..")
    excel_title = ["title", "date", "contents", "keyword", "img"]
    _list = []
    for data_dic in data_list:
        _list.append([
            data_dic.get("title", None),
            data_dic.get("date", None),
            data_dic.get("contents", None),
            data_dic.get("keyword", None),
            data_dic.get("img_list", None),
        ])

    df = pd.DataFrame(_list, columns=excel_title)
    _time = str(time.time())
    df.to_excel("{}.xlsx".format("fox_news"), encoding="utf-8", index=False)
    print("保存成功...")


if __name__ == '__main__':
    keyword_list = [
        'us china trade war',
        'us china trade conflict',
        'us china trade dispute',
        'US China trade negotiations',
        'us china trade talks',
        'us china trade agreement',
        'us China trade truce',
        'us china trade ceasefire',
        'us china trade spat',
        'Sino US tariffs',
        'huawei china',
        'rare earth china',
        'Forced technology issues china',
        'forced technology transfer'
    ]
    data_list = []
    page_data_list, acticle_list, threads = [], [], []
    for keyword in keyword_list:
        cgtn = CgtnSpider(keyword)
        url_list = cgtn.get_fox_data()
        for url in url_list:
            dic = cgtn.get_fox_page_data(url)
            page_data_list.append(dic)
        #     worker = WorkerThread(page_data_list, cgtn.get_fox_page_data, (url, ))
        #     worker.start()
        #     threads.append(worker)
        # for work in threads:
        #     work.join(1)
        #     if work.isAlive():
        #         logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
        #         threads.append(work)
        threads = []
        acticle_url_list = cgtn.parse_acticle_url(page_data_list)
        for acticle_dic in acticle_url_list:
            data = cgtn.get_article_data(acticle_dic)
            acticle_list.append(data)
        #     worker = WorkerThread(acticle_list, fox.get_article_data, (acticle_dic,))
        #     worker.start()
        #     threads.append(worker)
        # for work in threads:
        #     work.join(1)
        #     if work.isAlive():
        #         logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
        #         threads.append(work)

        save_data_to_excel(acticle_list)
