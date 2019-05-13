#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random
import time
import json
import re
from urllib import parse

from bs4 import BeautifulSoup
from service.core.utils.http_ import Requester
from service.exception import retry
from service.exception.exceptions import *
from service import logger
from service.micro.utils import ua
from service.micro.utils.cookie_utils import dict_to_cookie_jar
from service.micro.utils.math_utils import str_to_format_time
from service.micro.utils.threading_ import WorkerThread
from service.db.utils.elasticsearch_utils import ElasticsearchClient
from datetime import datetime


class CnkiSpider(object):
    __name__ = 'Weibo hot search'

    def __init__(self, keyword, number):
        self.number = number
        self.cookie = {'Ecp_notFirstLogin': 'YdAMsE', ' Ecp_ClientId': '4190506120301434846',
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
        self.cookie.update(_pk_ref=now)
        self.keyword = keyword
        self.requester = Requester(cookie=dict_to_cookie_jar(json.dumps(self.cookie)))
        self.es = ElasticsearchClient()

    def random_num(self):
        return random.uniform(0.1, 1)

    @retry(max_retries=5, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_cnki_page_data(self, url):
        """
        获取微博关键词首页的每条html
        :return: dict
        """
        logger.info('Processing get weibo key word ！')
        try:
            headers = {
                'User-Agent': ua(),
                'Connection': 'keep-alive',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'Accept-Encoding': 'gzip, deflate',
                #'Referer': 'http://kns.cnki.net/kns/brief/brief.aspx?curpage=2&RecordsPerPage=50&QueryID=38&ID=&turnpage=1&tpagemode=L&dbPrefix=SCDB&Fields=&DisplayMode=listmode&PageName=ASP.brief_default_result_aspx&isinEn=1&',
                'Host': 'kns.cnki.net',
            }


            #query_string = parse.urlencode(data)
            #time.sleep(0.5)
            resp = self.requester.get(url, header_dict=headers).text
            if "找到" in resp:
                return [resp]
            else:
                raise HttpInternalServerError
        except Exception as e:
            self.requester.use_proxy()
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
                'Accept-Encoding': 'gzip, deflate, br',
                'Host': 'kns.cnki.net'
            }
            resp = self.requester.get(url, header_dict=headers).text
            if "中国知网" in resp and "摘要" in resp:
                url_dic.update(resp=resp)
                del url_dic["url"]
                return url_dic
            else:
                raise HttpInternalServerError
        except Exception as e:
            self.requester.use_proxy()
            raise HttpInternalServerError

    @retry(max_retries=7, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_cnki_begin(self):

        try:
            url = "http://kns.cnki.net/kns/request/SearchHandler.ashx"
            headers = {
                'User-Agent': ua(),
                'Connection': 'keep-alive',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'Accept-Encoding': 'gzip, deflate, br',
                'Host': 'kns.cnki.net',
                "Referer": "http://kns.cnki.net/kns/brief/default_result.aspx"
            }
            data = {
                "PageName": "ASP.brief_default_result_aspx",
                "parentdb": "SCDB",
                "txt_1_sel": "SU$%=|",
                "txt_1_value1": self.keyword,
                "txt_1_special1": "%",
                "ConfigFile": "SCDBINDEX.xml",
                "dbPrefix": "SCDB",
                "db_opt": "CJFQ,CDFD,CMFD,CPFD,IPFD,CCND,CCJD",
                "his": 0,
                "action": "",
                "ua": "1.11",
                "DbCatalog": "中国学术文献网络出版总库",
                "__": time.strftime('%a %b %d %Y %H:%M:%S') + ' GMT+0800 (中国标准时间)'
            }
            resp = self.requester.post(url, header_dict=headers, data_dict=data)
            if resp.status_code == 200:
                return True
            else:
                raise HttpInternalServerError
        except Exception as e:
            self.requester.use_proxy()
            raise HttpInternalServerError

    def parse_detail_url_list(self, data):
        if not data:
            return
        url_list = []
        resp_obj = BeautifulSoup(data, "html")
        data_table = resp_obj.find("table", attrs={"class": "GridTableContent"}).find_all("tr")[1:]
        for tag in data_table:
            old_str = tag.find("a", attrs={"class": "fz14"}).attrs.get("href")
            r_data = tag.find_all("td")[1:-2]
            author = r_data[1].text.strip()  # 作者
            source = r_data[2].text.strip()  # 来源
            issuing_time = r_data[3].text.strip()  # 发表时间
            sql = r_data[4].text.strip()  # 数据库
            cited = r_data[5].text.strip()  # 被引用
            download = r_data[6].text.strip()  # 下载数

            db_name = re.findall("DbName=(\w+)?", old_str)[0]
            db_code = re.findall("DbCode=(\w+)?", old_str)[0]
            file_name = re.findall("FileName=(\w+)?", old_str)[0]
            url = "http://kns.cnki.net/KCMS/detail/detail.aspx?dbcode={}&dbname={}&filename={}".format(db_code, db_name,
                                                                                                       file_name)

            url_list.append(dict(url=url, author=author, source=source, issuing_time=issuing_time, sql=sql, cited=cited,
                                 download=download))
        return url_list

    def parse_cnki_detail(self, data):

        unit, contents, fund, kryword, doi, sort_num = "", "", "", "", "", ""
        resp = data.get("resp")
        resp_obj = BeautifulSoup(resp, "html")
        try:
            title_data = resp_obj.find("div", attrs={"class": "wxTitle"})
            detail = resp_obj.find("div", attrs={"class": "wxInfo"})
            title = title_data.contents[1].text.strip()  # 标题
            unit_flag = resp_obj.find("div", attrs={"class": "orgn"})
            if unit_flag:
                for tag in unit_flag.contents:
                    unit += "{},".format(tag.text.strip())
            contents_flag = detail.find("label", attrs={"id": "catalog_ABSTRACT"})  # 内容
            if contents_flag:
                contents = detail.contents[1].contents[1].text.strip("更多还原")  # 内容
            fund_flag = detail.find("label", attrs={"id": "catalog_FUND"})  # 基金
            if fund_flag:
                fund = detail.contents[1].contents[3].text.strip()  # 基金
            for i in detail.contents[1].contents:
                if "\n" in i:
                    continue
                if "关键词" in i.text:
                    keyword = i.text.replace("\r\n                ", "")
                elif "DOI" in i.text:
                    doi = i.text
                elif "分类号"in i.text:
                    sort_num = i.text
            #
            # kryword_flag = detail.find("label", attrs={"id": "catalog_KEYWORD"})  # 关键字
            # if kryword_flag:
            #     kryword = detail.contents[1].contents[5].text.replace("\r\n                ", "")  # 关键字
            # doi_flag = detail.find("label", attrs={"id": "catalog_ZCDOI"})  # DOI
            # if doi_flag:
            #     doi = detail.contents[1].contents[7].text  # DOI
            # sort_num_flag = detail.find("label", attrs={"id": "catalog_ZTCLS"})  # 分类号
            # if sort_num_flag:
            #     sort_num = detail.contents[1].contents[9].text  # 分类号
            del data["resp"]
            data.update(title=title, unit=unit, contents=contents, fund=fund, keyword=keyword, doi=doi,
                        sort_num=sort_num)
        except Exception as e:
            raise e

        return data

    def retrun_url_list(self):
        url_list = []
        data = {
            'pagename': 'ASP.brief_default_result_aspx',
            'isinEn': '1',
            'dbPrefix': 'SCDB',
            'dbCatalog': '中国学术期刊网络出版总库',
            'ConfigFile': 'SCDBINDEX.xml',
            'research': 'off',
            't': int(time.time()),
            'keyValue': self.keyword,
            'sorttype': '',
            'S': '1',
            #"recordsperpage": 50,
        }
        for i in range(1, self.number):

            # data = {
            #     'pagename': 'ASP.brief_default_result_aspx',
            #     'isinEn': '1',
            #     'dbPrefix': 'SCDB',
            #     'curpage': i,
            #     'Fields': '',
            #     'QueryID': 38,
            #     'sorttype': '',
            #     'tpagemode': "L",
            #     "RecordsPerPage": 50,
            # }
            query_string = parse.urlencode(data)
            url = "http://kns.cnki.net/kns/brief/brief.aspx?curpage={}&{}".format(i, query_string)
            #url = "http://kns.cnki.net/kns/brief/brief.aspx?{}".format(query_string)
            url_list.append(url)
        return url_list

    def save_data_to_excel(self, data_list):
        import pandas as pd
        _list = []
        detail_type_list = ["标题", "作者", "发布时间", "单位", "内容", "来源", "基金", "下载数", "引用数", "关键字",
                            "doi", "分类号", "sql"]

        for dic in data_list:
            _list.append([
                dic.get("title"),
                dic.get("author"),
                dic.get("issuing_time"),
                dic.get("unit"),
                dic.get("contents"),
                dic.get("source"),
                dic.get("fund"),
                dic.get("download"),
                dic.get("cited"),
                dic.get("keyword"),
                dic.get("doi"),
                dic.get("sort_num"),
                dic.get("sql"),
            ])
        print("开始存储时间 ：{}".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        df = pd.DataFrame(_list, columns=detail_type_list)
        file_name = r"C:\Users\dell\Desktop\{}.xlsx".format(self.keyword)
        df.to_excel(file_name, index=False)
        print("存储完成时间 ：{}".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))


if __name__ == '__main__':
    cn = CnkiSpider("国际新闻界",121)
    #cn = CnkiSpider("新闻与传播研究", 44)
    #cn = CnkiSpider("新闻大学", 88)
    #cn = CnkiSpider("现代传播", 121)
    begin_url_list = cn.retrun_url_list()
    resp_list, url_list, threads = [], [], []
    # for url in begin_url_list:
    #     try:
    #         resp = cn.get_cnki_page_data(url)
    #         resp_list.append(resp)
    #     except Exception as e:
    #         continue
    if cn.get_cnki_begin():
        for url in begin_url_list:
            resp = cn.get_cnki_page_data(url)
            resp_list.extend(resp)
    #     worker = WorkerThread(resp_list, cn.get_cnki_page_data, (url,))
    #     time.sleep(0.4)
    #     worker.start()
    #     threads.append(worker)
    #
    # for work in threads:
    #     work.join(1)
    #     if work.isAlive():
    #         logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
    #         threads.append(work)
    # threads = []
    for resp in resp_list:
        url_list.extend(cn.parse_detail_url_list(resp))
    #print(url_list)
    detail_list, threads = [], []
    for url_dic in url_list:
        # data = cn.get_cnki_dtail(url_dic)
        # detail_list.append(data)
        worker = WorkerThread(detail_list, cn.get_cnki_dtail, (url_dic,))
        time.sleep(0.4)
        worker.start()
        threads.append(worker)

    for work in threads:
        work.join(1)
        if work.isAlive():
            logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
            threads.append(work)

    data_list = []
    for resp in detail_list:
        try:
            detail = cn.parse_cnki_detail(resp)
            data_list.append(detail)
        except Exception as e:
            continue
    cn.save_data_to_excel(data_list)
    print(data_list)

