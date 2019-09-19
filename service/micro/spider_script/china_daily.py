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


class ChinaDailySpider(object):
    __name__ = 'china daily spider'

    def __init__(self, keyword, begin_date, end_date):
        self.keyword = keyword
        self.begin_date = begin_date
        self.end_date = end_date
        self.requester = Requester(timeout=15)

    def random_num(self):
        return random.uniform(0.1, 1)

    @retry(max_retries=7, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_page_data(self):
        logger.info('Processing get china daily key word ！')
        url_list = []
        keyword = self.keyword.replace(" ", "+")
        url = "http://newssearch.chinadaily.com.cn/rest/search?publishedDateFrom={}&publishedDateTo={}&fullMust={}&sort=dp&duplication=off&page=0&type=&channel=&source=".format(self.begin_date, self.end_date, keyword)
        headers = {
            'User-Agent': ua(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
        }
        try:
            resp = self.requester.get(url, header_dict=headers)
            if resp.status_code == 200:
                result = resp.json()
                num = result.get("totalElements") // 10
                page = 0
                for i in range(num):
                    url = "http://newssearch.chinadaily.com.cn/rest/search?publishedDateFrom={}&publishedDateTo={}&fullMust={}&sort=dp&duplication=off&page={}&type=&channel=&source=".format(self.begin_date, self.end_date, keyword, page)
                    url_list.append(url)
                    page += 1
                return url_list
            else:
                raise HttpInternalServerError
        except Exception as e:
            self.requester.use_proxy()
            raise HttpInternalServerError

    @retry(max_retries=7, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_all_page_data(self, url):
        headers = {
            'User-Agent': ua(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
        }
        try:
            resp = self.requester.get(url, header_dict=headers)
            if resp.status_code == 200:
                resp_list = resp.json().get("content")
                if resp_list:
                    return resp_list
            else:
                raise HttpInternalServerError
        except Exception as e:
            self.requester.use_proxy()
            raise HttpInternalServerError

    def parse_acticle(self, data):
        if not data:
            return
        print(data)
        authors = data.get("authors")
        author = ",".join(authors)
        dic = dict(
            title=data.get("title"),
            author=author,
            editor=data.get("editor"),
            date=data.get("pubDateStr"),
            section=data.get("columnName"),
            keyword=self.keyword,
            content=data.get("plainText"),
        )
        return dic

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
        excel_title = ["title", "date", "author", "editor",  "section", "keyword", "content"]
        for data_dic in data_list:
            _list.append([
                data_dic.get("title", None),
                data_dic.get("date", None),
                data_dic.get("author", None),
                data_dic.get("editor", None),
                data_dic.get("section", None),
                data_dic.get("keyword", None),
                data_dic.get("content", None),
            ])

        df = pd.DataFrame(_list, columns=excel_title)
        df.drop_duplicates(subset=["content"], keep='first', inplace=True)
        #df2 = df.sort_values(by="date", ascending=False)
        df.to_excel(r"C:\Users\dell\Desktop\china_daily\{}.xlsx".format(self.keyword), encoding="utf-8", index=False)
        print("保存成功...")


if __name__ == '__main__':
    keyword_list = [
        'US China trade war',
        'US China trade conflict',
        'US China trade dispute',
        'US China trade negotiation',
        'US China trade talk',
        'US China trade agreement',
        'US China trade truce',
        'US China trade ceasefire',
        'US China trade spat',
        'US China trade tariff',
        'huawei US China trade',
        'rare earth US China trade',
        'forced technology transfer US China trade',
        'G20 US china trade',
    ]
    begin_date, end_date = "2019-07-10", "2019-08-01"
    for keyword in keyword_list:
        page_data_list, acticle_list = [], []
        spider = ChinaDailySpider(keyword, begin_date, end_date)
        url_list = spider.get_page_data()
        for url in url_list:
            try:
                dic = spider.get_all_page_data(url)
                page_data_list.extend(dic)
            except:
                continue

        for acticle_dic in page_data_list:
            try:
                data = spider.parse_acticle(acticle_dic)
                acticle_list.append(data)
            except Exception as e:
                continue

        spider.save_data_to_excel(acticle_list)