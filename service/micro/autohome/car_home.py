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


class AutoHomeSpider(object):
    __name__ = 'auto home '

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
                logger.info("count: {} , get_cnki_page_data sussess！！！！ ")
                return resp
            else:
                self.next_cookie()
                raise HttpInternalServerError
        except Exception as e:
            time.sleep(5)
            self.next_cookie()
            raise HttpInternalServerError

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_koubei_html(self, car_num_list):
        """
        获取微博关键词首页的每条html
        :return: dict
        """
        all_url_list = []
        for car_num in car_num_list:
            if car_num is "0": continue
            logger.info('Processing get koubei ！')
            try:
                url = "https://k.autohome.com.cn/{}".format(car_num)
                headers = {
                    'User-Agent': ua(),
                    'Connection': 'keep-alive',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                    'Accept-Encoding': 'gzip, deflate',
                    "Accept-Language": "zh-CN,zh;q=0.9",
                }
                resp = self.requester.get(url, header_dict=headers).text
                if "全部口碑" in resp:
                    logger.info("get page data success")
                    url_list = self.parse_page_url_list(car_num, resp)
                    # car_num_list.pop(car_num_list.index(car_num))
                    if url_list:
                        all_url_list.extend(url_list)
                    else:
                        logger.info("is not data")
                else:
                    raise HttpInternalServerError
            except Exception as e:
                self.requester.use_proxy()
                raise HttpInternalServerError
        return all_url_list

    @retry(max_retries=5, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_one_koubei_data(self, url):
        """
        获取每页内容
        :return: dict
        """
        logger.info('Processing get_one_koubei_data ！')
        try:
            headers = {
                'User-Agent': ua(),
                'Connection': 'keep-alive',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'Accept-Encoding': 'gzip, deflate',
                "Accept-Language": "zh-CN,zh;q=0.9",
            }
            resp = self.requester.get(url, header_dict=headers)
            if "全部口碑" in resp.text:
                logger.info("get page data success")
                return resp.text
            elif "用户访问安全认证V2" in resp.text:
                time.sleep(1)
                raise HttpInternalServerError
        except Exception as e:
            self.requester.use_proxy()
            raise HttpInternalServerError

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_car_number(self):
        logger.info("Begin get car number..")
        try:
            headers = {
                'User-Agent': ua(),
                "Referer": "https://www.autohome.com.cn/beijing/",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                "Connection": "keep-alive",
                "Host": "sou.autohome.com.cn"
            }
            url = "https://sou.autohome.com.cn/Api/Suggest/search?q={}&plat=pc&chl=zonghe".format(
                self.keyword.encode("unicode_escape").decode("utf-8").replace("\\", "%"))
            resp = self.requester.get(url, header_dict=headers)
            if "Sou.Autocomplate.bindAutocomplate" in resp.text:
                logger.info("get car number success resp : {}".format(resp.text))
                car_num = self.parse_car_number(resp.text)
                return car_num
            else:
                raise HttpInternalServerError
        except Exception as e:
            time.sleep(1)
            self.requester.use_proxy()
            raise HttpInternalServerError

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_detail_html(self, url):
        logger.info("Begin get car detail data..")
        try:
            headers = {
                'User-Agent': ua(),
            }
            resp = self.requester.get(url, header_dict=headers).text
            if "购买车型" in resp and "购买时间" in resp:
                logger.info("get car number success resp : {}".format(resp))
                return resp
            else:
                raise HttpInternalServerError
        except Exception as e:
            time.sleep(1)
            raise HttpInternalServerError

    def parse_car_number(self, resp):
        # num_obj = re.search(r":(\d+):", resp)
        # car_num = num_obj.group(1)
        num_obj = re.findall(r":(\d+):", resp)
        return list(set(num_obj))

    def parse_page_url_list(self, car_num, resp):
        resp_obj = BeautifulSoup(resp, "lxml")
        page_num_tag = resp_obj.find("span", attrs={"class": "page-item-info"})
        if not page_num_tag:
            return []
        page_num_obj = re.search(r"(\d+)", page_num_tag.text)
        page_num = page_num_obj.group(1)
        url_list = []
        if page_num:
            for i in range(1, int(page_num)):
                url = "https://k.autohome.com.cn/{}/index_{}.html".format(car_num, i)
                url_list.append(url)
        else:
            url = "https://k.autohome.com.cn/{}/index_{}.html".format(car_num, 1)
            url_list.append(url)
        return url_list

    def parse_detail_data(self, data):
        if not data:
            return []
        data_list = []

        resp_obj = BeautifulSoup(data, "lxml")
        data_table = resp_obj.find_all("div", attrs={"class": "mouthcon"})
        for data_tag in data_table:
            try:
                detail = data_tag.find("div", attrs={"class": "choose-con mt-10"}).find_all("dl")
                text = data_tag.find("div", attrs={"class": "text-con "}).text.strip()
                resp_data = self.parse_evaluatio_data(detail)
                if resp_data:
                    resp_data.update(text=text)
                    data_list.append(resp_data)
                    logger.info("parse data success data : {}".format(resp_data))
            except Exception as e:
                continue
        return data_list

    def parse_evaluatio_data(self, detail):
        buy_model, buy_location, buy_dealer, buy_date, bare_car_price, oil = "", "", "", "", "", ""
        travel, space, power, manipulation, oil_consumption, comfort = "", "", "", "", "", ""
        exterior, interior, value_for_money, buy_car_purpose = "", "", "", ""
        for tag in detail:
            if "购买车型" in tag.text:
                if self.keyword not in tag.text:
                    return
                buy_model = tag.contents[3].text.strip().replace("\n", " ")
            elif "购买地点" in tag.text:
                buy_location = tag.contents[3].text.strip()
            elif "购车经销商" in tag.text:
                buy_dealer = tag.contents[3].text.strip()
            elif "购买时间" in tag.text:
                buy_date = tag.contents[3].text.strip()
            elif "裸车购买价" in tag.text:
                bare_car_price = tag.contents[3].text.strip()
            elif "目前行驶" in tag.text:
                try:
                    if len(tag.contents[3].contents) == 3:
                        travel = tag.contents[3].contents[1].text.strip()
                        oil = ""
                    else:
                        oil = tag.contents[3].contents[1].text.strip()  # 百公里油耗
                        if len(tag.contents[3].contents) == 5:
                            travel = tag.contents[3].contents[3].text.strip()
                        else:
                            travel = tag.contents[3].contents[2].text.strip()
                except Exception as e:
                    oil, travel = "", ""
            elif "空间" in tag.text:
                space = tag.contents[3].text.strip()
            elif "动力" in tag.text:
                power = tag.contents[3].text.strip()
            elif "操控" in tag.text:
                manipulation = tag.contents[3].text.strip()
            elif "油耗" in tag.text:
                oil_consumption = tag.contents[3].text.strip()
            elif "舒适性" in tag.text:
                comfort = tag.contents[3].text.strip()
            elif "外观" in tag.text:
                exterior = tag.contents[3].text.strip()
            elif "内饰" in tag.text:
                interior = tag.contents[3].text.strip()
            elif "性价比" in tag.text:
                value_for_money = tag.contents[3].text.strip()
            elif "购车目的" in tag.text:
                buy_car_purpose = tag.contents[3].text.strip().replace("\n", ",")
        resp_data = dict(buy_model=buy_model, buy_location=buy_location, buy_dealer=buy_dealer,
                         buy_date=buy_date,
                         bare_car_price=bare_car_price, oil=oil, travel=travel, space=space, power=power,
                         manipulation=manipulation,
                         oil_consumption=oil_consumption, comfort=comfort, exterior=exterior, interior=interior,
                         value_for_money=value_for_money, buy_car_purpose=buy_car_purpose
                         )
        return resp_data

    def save_data_to_excel(self, data_list):
        import pandas as pd
        _list = []
        detail_type_list = ["购买车型", "购买地点", "购买时间", "裸车购买价", "百公里油耗", "目前行驶", "空间 *", "动力 *", "操控 *", "油耗 *", "舒适性 *",
                            "外观 *", "内饰 *", "性价比 *", "购车目的", "评价"]

        for dic in data_list:
            _list.append([
                dic.get("buy_model"),
                dic.get("buy_location"),
                # dic.get("buy_dealer"),
                dic.get("buy_date"),
                dic.get("bare_car_price"),
                dic.get("oil"),
                dic.get("travel"),
                dic.get("space"),
                dic.get("power"),
                dic.get("manipulation"),
                dic.get("oil_consumption"),
                dic.get("comfort"),
                dic.get("exterior"),
                dic.get("interior"),
                dic.get("value_for_money"),
                dic.get("buy_car_purpose"),
                dic.get("text"),
            ])
        logger.info("开始存储时间 ：{}".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        df = pd.DataFrame(_list, columns=detail_type_list)
        file_name = r"C:\Users\dell\Desktop\{}{}.xlsx".format(self.keyword, str(int(time.time())))
        df.to_excel(file_name, index=False)
        logger.info("存储完成时间 ：{}".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))


if __name__ == '__main__':
    resp_list = []
    detail_list = []
    detail_data_list = []
    for key_word in ["上汽大通", "雅阁", "迈腾", ]:
        ah = AutoHomeSpider(key_word)
        car_number = ah.get_car_number()
        url_list = ah.get_koubei_html(car_number)


        def callback(obj, data):
            resp_list.append(data)


        pool = threadpool.ThreadPool(5)
        tasks = threadpool.makeRequests(ah.get_one_koubei_data, url_list, callback)
        for task in tasks:
            pool.putRequest(task)
        pool.wait()

        for resp in resp_list:
            detail_list.extend(ah.parse_detail_data(resp))
        if detail_list:
            ah.save_data_to_excel(detail_list)
            detail_list.clear(), resp_list.clear()
