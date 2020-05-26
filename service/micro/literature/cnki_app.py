#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random
import time
import json
import re
import threadpool

from urllib import parse

from bs4 import BeautifulSoup
from service.core.utils.http_ import Requester
from service.exception import retry
from service.exception.exceptions import *
from service import logger
from service.micro.utils import ua
from service.micro.utils.cookie_utils import dict_to_cookie_jar

from service.db.utils.elasticsearch_utils import es_client
from datetime import datetime


class CnkiSpider(object):
    __name__ = 'cnki app'

    def __init__(self, keyword):
        self.cookie = self.next_cookie()
        self.keyword = keyword
        self.requester = Requester(cookie=dict_to_cookie_jar(json.dumps(self.cookie)), timeout=20)
        self.es = es_client

    def random_num(self):
        return random.uniform(0.1, 0.3)

    def next_cookie(self):
        cookie = {'Ecp_notFirstLogin': 'YdAMsE', ' Ecp_ClientId': '4190506120301434846',
                  ' ASP.NET_SessionId': 'rh5z0bxeca1co002gitqyddj', ' SID_kns': '123123', ' SID_klogin': '125141',
                  ' SID_crrs': '125133', ' SID_krsnew': '125134',
                  ' cnkiUserKey': '722bbac3-44d6-75c4-10d1-661db9fc2e4b', ' SID_kcms': '124115',
                  ' SID_kinfo': '125102', ' Ecp_lout': '1', ' IsLogin': '', ' RsPerPage': '50',
                  ' SID_kxreader_new': '011124', ' SID_kns_kdoc': '015011122', ' Ecp_session': '1',
                  ' SID_knsdelivery': '125122', ' DisplaySave': '6', ' KNS_SortType': '',
                  ' ASPSESSIONIDCCSDABAR': 'JIJDJGJAIDLMHFACDKDLPFPP',
                  ' UM_distinctid': '16a95e3bb6152e-0d84e69961763-7a1b34-1fa400-16a95e3bb62673',
                  ' _pk_ref': "",
                  ' _pk_ses': '*', ' UserAMID': 'wap_8a20120f-6089-4faa-912c-53b4391abf60',
                  ' LID': 'WEEvREcwSlJHSldRa1FhcEE0QVRBZ1RKK0lFZktpYlAyYVRPcWJybTV5az0', ' SID_kredis': '125143',
                  ' Ecp_LoginStuts': '%7B%22IsAutoLogin%22%3Afalse%2C%22UserName%22%3A%22dx0752%22%2C%22ShowName%22%3A%22%25E5%25A4%25A9%25E6%25B4%25A5%25E5%25A4%25A7%25E5%25AD%25A6%22%2C%22UserType%22%3A%22bk%22%2C%22r%22%3A%22YdAMsE%22%7D',
                  ' c_m_LinID': 'LinID', ' c_m_expire': '2019-05-08 14:45:02'}
        now = '%5B%22%22%2C%22%22%2C{}%2C%22http%3A%2F%2Fwww.cnki.net%2F%22%5D'.format(time.time())
        cookie.update(_pk_ref=now)
        self.requester = Requester(cookie=dict_to_cookie_jar(json.dumps(cookie)), timeout=20)
        return cookie

    def thread_get_page_data(self, page):
        data_list = []

        def callback(raw_data_list, data):
            data_list.append(data)

        page_list = [i for i in range(2, page)]
        pool = threadpool.ThreadPool(10)
        tasks = threadpool.makeRequests(self.get_cnki_page_data, page_list, callback)
        for task in tasks:
            pool.putRequest(task)
        pool.wait()

        return data_list

    @retry(max_retries=7, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_cnki_page_data(self, page_num):
        """
        获取微博关键词首页的每条html
        :return: dict
        """
        logger.info('Processing get weibo key word ！')
        url = "http://wap.cnki.net/touch/web/Article/Search"
        headers = {
            'User-Agent': ua(),
            'Connection': 'keep-alive',
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'wap.cnki.net',
            "Origin": "http://wap.cnki.net",
            "Referer": "http://wap.cnki.net/touch/web/Article/Search",
            "X-Requested-With": "XMLHttpRequest"
        }
        data = {
            "searchtype": 1,
            "dbtype": "",
            "pageindex": page_num,
            "pagesize": 50,
            "source_kw": self.keyword,
            "fieldtype": 0,
            "sorttype": 1,
            "articletype": 0,
            "screentype": 0,

        }

        try:
            time.sleep(self.random_num())
            resp = self.requester.post(url, header_dict=headers, data_dict=data).text
            if "条" in resp:
                logger.info("count: {} , get_cnki_page_data sussess！！！！ ".format(page_num))
                return resp
            else:
                self.next_cookie()
                raise HttpInternalServerError
        except Exception as e:
            time.sleep(5)
            self.next_cookie()
            raise HttpInternalServerError

    @retry(max_retries=7, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_cnki_dtail(self, url_dic):
        """
        获取微博关键词首页的每条html
        :return: dict
        """
        logger.info('Processing get detail ！')
        try:
            url = url_dic.get("url")
            headers = {
                'User-Agent': ua(),
                'Connection': 'keep-alive',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'Accept-Encoding': 'gzip, deflate',
                "Accept-Language": "zh-CN,zh;q=0.9",
                'Host': 'wap.cnki.net',
                "Referer": "http://wap.cnki.net/touch/web/Article/Search"
            }
            time.sleep(self.random_num())
            resp = self.requester.get(url, header_dict=headers).text
            if "手机知网" in resp:
                url_dic.update(resp=resp)
                del url_dic["url"]
                return url_dic
            else:
                raise HttpInternalServerError
        except Exception as e:
            self.next_cookie()
            raise HttpInternalServerError

    @retry(max_retries=7, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_cnki_begin(self):

        resp_list = []
        try:
            url = "http://wap.cnki.net/touch/web/Article/Search"
            headers = {
                'User-Agent': ua(),
                'Connection': 'keep-alive',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'Accept-Encoding': 'gzip, deflate, br',
                'Host': 'wap.cnki.net',
            }
            data = {
                "searchtype": 1,
                "dbtype": "",
                "pageindex": 1,
                "pagesize": 50,
                "source_kw": self.keyword,
                "fieldtype": 0,
                "sorttype": 1,
                "articletype": 0,
                "screentype": 0,

            }
            resp = self.requester.post(url, header_dict=headers, data_dict=data).text
            if "搜索结果" in resp:
                count = int(re.findall(r'<span id="totalcount" style="display:none;">(\d+?)</span>', resp)[0])
                page_num = count // 10 + 1
                page_num = 30
                page_resp_list = self.thread_get_page_data(page_num)
                resp_list.extend(page_resp_list)
                resp_list.append(resp)
                return resp_list
            else:
                raise HttpInternalServerError
        except Exception as e:
            time.sleep(5)
            raise HttpInternalServerError

    def parse_detail_url_list(self, data):
        if not data:
            return
        url_list = []
        resp_obj = BeautifulSoup(data, "lxml")
        data_table = resp_obj.find_all("div", attrs={"class": "c-company__body-item"})
        for tag in data_table:
            try:
                is_source = tag.find("span", attrs={"class": "color-green"})
                title = tag.contents[1].contents[1].text.replace("\r\n", "").strip()  # 标题
                author = tag.contents[1].contents[3].text.replace("\r\n\r\n", "").strip()  # 作者
                source = is_source.text.split(" ")[0].strip()  # 来源
                is_issuing_time = is_source.text.split(" ")
                issuing_time = is_issuing_time[1] if len(is_issuing_time) == 2 else is_issuing_time[2]  # 发表时间
                download_flag = re.findall(r"下载：(\d+)?", tag.contents[3].text)
                download = download_flag[0] if download_flag else 0  # 下载数
                cited_flag = re.findall(r"被引：(\d+)?", tag.contents[3].text)  # 被引用
                cited = cited_flag[0] if cited_flag else 0  # 下载数

                url = "http:{}".format(tag.find("a", attrs={"class": "c-company-top-link"}).attrs.get("href"))

                url_list.append(
                    dict(title=title, url=url, author=author, source=source, issuing_time=issuing_time, cited=cited,
                         download=download))
            except Exception as e:
                print(e)
        return url_list

    def parse_cnki_detail(self, data):

        contents, fund, keyword, doi, institution, field = "", "", "", "", "", ""
        resp = data.get("resp")
        resp_obj = BeautifulSoup(resp, "lxml")
        try:
            detail = resp_obj.find("div", attrs={"class": "c-card__paper__info"}).contents
            contents = resp_obj.find("div", attrs={"class": "c-card__aritcle"}).text.replace("\r\n", "").strip()  # 内容
            for i in detail:
                if isinstance(i, str):
                    continue
                if "机　构" in i.text:
                    institution = i.text.replace("\n", "").replace("\r", "").split(":")[1].strip()
                elif "领　域" in i.text:
                    field = i.text.replace("\n", "").replace("\r", "").split(":")[1].strip()
                elif "关键词" in i.text:
                    keyword_list = i.text.replace("\n", "").replace("\r", "").strip().split("关键词:")[1].split("；")
                    keyword = ", ".join([j.strip() for j in keyword_list])

            del data["resp"]
            data.update(contents=contents, field=field, keyword=keyword, institution=institution)
        except Exception as e:
            raise e

        return data

    def save_data_to_excel(self, data_list):
        import pandas as pd
        _list = []
        detail_type_list = ["标题", "作者", "发布时间", "机构", "领域", "内容", "来源", "下载数", "引用数", "关键字"]

        for dic in data_list:
            _list.append([
                dic.get("title"),
                dic.get("author"),
                dic.get("issuing_time"),
                dic.get("institution"),
                dic.get("field"),
                dic.get("contents"),
                dic.get("source"),
                dic.get("download"),
                dic.get("cited"),
                dic.get("keyword"),
            ])
        logger.info("开始存储时间 ：{}".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        df = pd.DataFrame(_list, columns=detail_type_list)
        file_name = r"C:\Users\dell\Desktop\{}{}.xlsx".format(self.keyword, str(int(time.time())))
        df.to_excel(file_name, index=False)
        logger.info("存储完成时间 ：{}".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))


if __name__ == '__main__':
    for key_word in ["国际新闻界", "新闻与传播研究", "新闻大学", "现代传播"]:
        cn = CnkiSpider(key_word)
        url_list, threads = [], []
        resp_list = cn.get_cnki_begin()
        for resp in resp_list:
            data = cn.parse_detail_url_list(resp)
            url_list.extend(data)

        detail_list, threads = [], []


        def callback(raw_data_list, data):
            detail_list.append(data)


        pool = threadpool.ThreadPool(20)
        tasks = threadpool.makeRequests(cn.get_cnki_dtail, url_list, callback)
        for task in tasks:
            pool.putRequest(task)
        pool.wait()
        data_list = []
        for resp in detail_list:
            try:
                detail = cn.parse_cnki_detail(resp)
                data_list.append(detail)
            except Exception as e:
                continue
        cn.save_data_to_excel(data_list)
