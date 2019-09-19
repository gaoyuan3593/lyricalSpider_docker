#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random
import re
import pandas as pd
from bs4 import BeautifulSoup
from service.core.utils.http_ import Requester
from service.exception import retry
from service.exception.exceptions import *
from service import logger
from service.micro.utils import ua
from service.micro.utils.cookie_utils import dict_to_cookie_jar, cookie_jar_to_dict
from lxml import etree
from datetime import datetime
from service.micro.utils.threading_ import WorkerThread


class GlobalTimesSpider(object):
    __name__ = 'global times spider'

    def __init__(self, keyword, begin_date, end_date):
        self.keyword = keyword
        self.begin_date = begin_date
        self.end_date = end_date
        self.requester = Requester(timeout=15)

    def random_num(self):
        return random.uniform(0.1, 1)

    @retry(max_retries=7, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_global_data(self):
        logger.info('Processing get global times news key word ！')
        resp_list = []
        url = "http://search.globaltimes.cn/SearchCtrl"
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'search.globaltimes.cn',
            'Referer': 'http://search.globaltimes.cn/SearchCtrl'
        }
        data = {
            "page_no": "",
            "title": "",
            "column": "0",
            "sub_column": "0",
            "author": "",
            "source": "",
            "textPage": self.keyword,
            "begin_date": self.begin_date,
            "end_date": self.end_date,
        }
        try:
            resp = self.requester.post(url, header_dict=headers, data_dict=data)
            if resp.status_code == 200:
                resp_list.append(resp)
                result = re.findall(r"Total:(\d+) records", resp.text)[0]
                num = int(result) // 10 + 1
                return num
            else:
                raise HttpInternalServerError
        except Exception as e:
            self.requester.use_proxy()
            raise HttpInternalServerError

    @retry(max_retries=7, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_global_page_data(self, num):
        url = "http://search.globaltimes.cn/SearchCtrl"
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'search.globaltimes.cn',
            'Referer': 'http://search.globaltimes.cn/SearchCtrl'
        }
        try:
            art_list = []
            a_url_list = []
            for i in range(num):
                if i >= 1:
                    data = {
                        "page_no": i,
                        "title": "",
                        "column": "0",
                        "sub_column": "0",
                        "author": "",
                        "source": "",
                        "textPage": self.keyword,
                        "begin_date": self.begin_date,
                        "end_date": self.end_date,
                    }
                    print(i)
                    resp = self.requester.post(url, header_dict=headers, data_dict=data)
                    if resp.status_code == 200:
                        soup = BeautifulSoup(resp.text, "lxml")
                        data_list = soup.find_all("div", attrs={"class": "row-fluid"})[4:-3]
                        for div in data_list:
                            a_url = div.find("div", attrs={"class": "span9"}).find("a").attrs.get("href")
                            if a_url in a_url_list:
                                continue
                            a_url_list.append(a_url)
                            title = div.find("div", attrs={"class": "span9"}).find("a").find("h4").text.strip()
                            try:
                                author = div.find("small").text.split("Author:")[1].split("|")[0].strip()
                                section = div.find("small").text.split("Column:")[1].strip()
                            except:
                                author, section = "", ""
                            dic = dict(
                                a_url=a_url,
                                title=title,
                                author=author,
                                section=section
                            )
                            print(dic)
                            art_list.append(dic)
            return art_list
        except Exception as e:
            self.requester.use_proxy()
            raise HttpInternalServerError

    @retry(max_retries=7, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_article_data(self, acticle_data):
        url = acticle_data.get("a_url")
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 'www.globaltimes.cn'
        }
        try:
            resp = self.requester.get(url, header_dict=headers)
            if resp.status_code == 200:
                logger.info("get artacle detail success")
                artcle_date = re.findall(r"\d+/\d+/\d+ \d+:\d+:\d+", resp.text)[0]
                x_html = etree.HTML(resp.text)
                content = x_html.xpath('//*[@class="span12 row-content"]/text()')
                content = "".join(content).strip()
                if not content:
                    content = x_html.xpath('//*[@class="span12 row-content"]/span/text()') or \
                              x_html.xpath('//*[@class="span12 row-content"]/p/text()') or \
                              x_html.xpath('//*[@class="span12 row-content"]/div/div/text()')
                content = "".join(content).strip()
                if not content:
                    soup = BeautifulSoup(resp.text, "lxml")
                    content = soup.find("div", attrs={"class": "span12 row-content"}).text.strip()
                if not content:
                    print(content)
                content = "".join(content).strip()

                acticle_data.update(
                    content=content,
                    date=artcle_date,
                    keyword=self.keyword
                )
                del acticle_data["a_url"]
                return acticle_data
        except Exception as e:
            self.requester.use_proxy()
            raise HttpInternalServerError

    def save_data_to_excel(self, data_list):
        print("Being data save to excel..")
        _list = []
        excel_title = ["title", "date", "author", "section", "keyword", "content"]
        for data_dic in data_list:
            if not data_dic:
                continue
            _list.append([
                data_dic.get("title", None),
                data_dic.get("date", None),
                data_dic.get("author", None),
                data_dic.get("section", None),
                data_dic.get("keyword", None),
                data_dic.get("content", None),
            ])

        df = pd.DataFrame(_list, columns=excel_title)
        df.drop_duplicates(subset=["title"], keep='first', inplace=True)
        # df2 = df.sort_values(by="date", ascending=False)
        df.to_excel(r"C:\Users\dell\Desktop\global_times\{}.xlsx".format(self.keyword), encoding="utf-8", index=False)
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
        spider = GlobalTimesSpider(keyword, begin_date, end_date)
        num = spider.get_global_data()
        # num = 10
        url_list = spider.get_global_page_data(num)
        for url in url_list:
            try:
                data = spider.get_article_data(url)
                acticle_list.append(data)
            except:
                continue
        spider.save_data_to_excel(acticle_list)
