#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random
import time
import pandas as pd
from service.core.utils.http_ import Requester
from service.exception import retry
from service.exception.exceptions import *
from service import logger
from service.micro.utils import ua
from service.micro.utils.cookie_utils import dict_to_cookie_jar, cookie_jar_to_dict
from lxml import etree
from datetime import datetime
from service.micro.utils.threading_ import WorkerThread


class FoxNewsSpider(object):
    __name__ = 'fox news spider'

    def __init__(self, keyword):
        self.keyword = keyword
        self.requester = Requester(timeout=15)

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
        url = "https://api.foxnews.com/v1/content/search?q={}&fields=date,description,title,url,image,type,taxonomy&section.path=fnc&start=0".format(
            self.keyword.replace(" ", "%20AND%20"))
        headers = {
            'user-Agent': ua(),
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-Encoding': 'gzip, deflate',
        }
        try:
            resp = self.requester.get(url, header_dict=headers)
            if resp.status_code == 200:
                result = resp.json().get("response")
                num = result.get("numFound") // 10 + 1
                if num > 1000:
                    num = 1000
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
            self.requester.use_proxy()
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
                if resp_dic.get("docs"):
                    # resp_dic.update(url=url)
                    return resp_dic.get("docs")
        except Exception as e:
            self.requester.use_proxy()
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
                source = x_html.xpath('//*[@class="author-byline"]/span/span/text()') or \
                         x_html.xpath('//*[@class="author-byline"]/span/span/a/text()') or \
                         x_html.xpath('//*[@class="author-byline opinion"]/span/span/a/text()')
                source = "".join(source).strip() if source else ""
                acticle_data.update(
                    contents=content,
                    editor=source
                )
                del acticle_data["url"]
            return acticle_data
        except Exception as e:
            self.requester.use_proxy()
            raise HttpInternalServerError

    def parse_acticle_url(self, data):
        dic_list, img_list = [], []
        _list = []
        _ = []
        _adtag_list = []
        for _data in data:
            if isinstance(_data, dict):
                if _data.get("type") == "article":
                    _str = _data.get("date")
                    _date = self.parse_date(_str)
                    if not _date:
                        continue
                    title = _data.get("title")
                    if title in _:
                        continue
                    _.append(title)
                    tag_list = _data.get("taxonomy")
                    if tag_list:
                        for i in tag_list:
                            tag = i.get("adTag")
                            if tag:
                                _adtag_list.append(tag)
                else:
                    continue
                _url = _data.get("url")
                url = "".join(_url[0] if len(_url) > 1 else _url)
                section = ",".join(_adtag_list) if _adtag_list else ""
                dic_list.append(dict(
                    title=title,
                    date=_date,
                    section=section,
                    keyword=self.keyword,
                    url=url
                ))
                _adtag_list = []
            else:
                continue
        return dic_list

    def parse_date(self, _str):
        if not _str:
            return False
        date = datetime.strptime(_str, "%Y-%m-%dT%H:%M:%SZ")  #
        if date.year >= 2018 and date.month >= 1 and date.day >= 1:
            return date.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return False

    def save_data_to_excel(self, data_list):
        print("Being data save to excel..")
        _list = []
        excel_title = ["title", "date", "editor",  "section", "keyword", "contents"]
        for data_dic in data_list:
            _list.append([
                data_dic.get("title", None),
                data_dic.get("date", None),
                data_dic.get("editor", None),
                data_dic.get("section", None),
                data_dic.get("keyword", None),
                data_dic.get("contents", None),
            ])

        df = pd.DataFrame(_list, columns=excel_title)
        df.drop_duplicates(subset=["title"], keep='first', inplace=True)
        #df2 = df.sort_values(by="date", ascending=False)
        df.to_excel(r"C:\Users\dell\Desktop\fox\{}.xlsx".format(self.keyword), encoding="utf-8", index=False)
        print("保存成功...")


if __name__ == '__main__':
    keyword_list = [
        # 'US China trade war',
        # 'US China trade conflict',
        # 'US China trade dispute',
        # 'US China trade negotiation',
        # 'US China trade talk',
        # 'US China trade agreement',
        # 'US China trade truce',
        # 'US China trade ceasefire',
        'US China trade spat',
        # 'US China trade tariff',
        # 'huawei US China trade',
        # 'rare earth US China trade',
        # 'forced technology transfer US China trade',
        # 'G20 US china trade',
    ]

    for keyword in keyword_list:
        page_data_list, acticle_list, threads = [], [], []
        fox = FoxNewsSpider(keyword)
        url_list = fox.get_fox_data()
        for url in url_list:
            try:
                dic = fox.get_fox_page_data(url)
                page_data_list.extend(dic)
            except:
                continue
        #     worker = WorkerThread(page_data_list, fox.get_fox_page_data, (url,))
        #     worker.start()
        #     threads.append(worker)
        # for work in threads:
        #     work.join(1)
        #     if work.isAlive():
        #         logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
        #         threads.append(work)
        # threads = []
        acticle_url_list = fox.parse_acticle_url(page_data_list)
        for acticle_dic in acticle_url_list:
            try:
                data = fox.get_article_data(acticle_dic)
                acticle_list.append(data)
            except Exception as e:
                continue
        #     worker = WorkerThread(acticle_list, fox.get_article_data, (acticle_dic,))
        #     worker.start()
        #     threads.append(worker)
        # for work in threads:
        #     work.join(1)
        #     if work.isAlive():
        #         logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
        #         threads.append(work)

        fox.save_data_to_excel(acticle_list)
        threads = []