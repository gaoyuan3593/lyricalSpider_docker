#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random
import time
import json
import hashlib
from bs4 import BeautifulSoup
from service.core.utils.http_ import Requester
from service.exception import retry
from service.exception.exceptions import *
from service import logger
from service.micro.utils import ua
from service.db.utils.es_mappings import HOT_SEARCH_KEYWORD_MAPPING
from service.db.utils.elasticsearch_utils import es_client, h_es_client, HOT_SEARCH_BAIDU
from datetime import datetime, timedelta


class BaiDuHotSeachSpider(object):
    __name__ = 'bai du hot search'

    def __init__(self):
        self.requester = Requester(timeout=20)
        self.es = es_client
        self.h_es = h_es_client
        self.create_index()

    def create_index(self):
        _index_mapping = {
            "index_type":
                {
                    "properties": HOT_SEARCH_KEYWORD_MAPPING
                },
        }
        self.es.create_index(HOT_SEARCH_BAIDU, _index_mapping)
        self.h_es.create_index(HOT_SEARCH_BAIDU, _index_mapping)

    def filter_keyword(self, id, _type, data):
        try:
            result = self.es.get(HOT_SEARCH_BAIDU, _type, id)
            if result.get("found"):
                data_list = []
                raw_data = result.get("_source")
                raw_heat = raw_data.get("result")
                current_heat = data.get("result")
                if current_heat[0].get("heat") != raw_heat[-1].get("heat"):
                    data_list.append(current_heat[0])
                    raw_heat.extend(data_list)
                    self.es.update(HOT_SEARCH_BAIDU, data.get("type"), id=id, body=raw_data)
                    self.h_es.update(HOT_SEARCH_BAIDU, data.get("type"), id=id, body=raw_data)
                return True
            return False
        except Exception as e:
            logger.exception(e)
            raise e

    def save_one_data_to_es(self, data, id=None):
        """
        将为爬取的数据存入es中
        :param data_list: 数据
        :return:
        """
        try:
            _type = data.get("type")
            if self.filter_keyword(id, _type, data):
                logger.info("{} Data update success id: {}".format(self.__name__, id))
                return
            self.es.insert(HOT_SEARCH_BAIDU, _type, data, id)
            self.h_es.insert(HOT_SEARCH_BAIDU, _type, data, id)
            logger.info("{} save to es success [ index : {}, data={}]！".format(self.__name__, HOT_SEARCH_BAIDU, data))
        except Exception as e:
            logger.exception(e)
            raise e

    def random_num(self):
        return random.uniform(0.1, 0.5)

    def retrun_md5(self, s):
        m = hashlib.md5()
        m.update(s.encode("utf-8"))
        return m.hexdigest()

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_baidu_hot_seach(self):
        logger.info('Processing get baidu hot search list!')
        url = 'http://top.baidu.com/buzz?b=1&fr=20811'
        headers = {
            'User-Agent': ua(),
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 'top.baidu.com'
        }
        try:
            response = self.requester.get(url=url, header_dict=headers)
            response.encoding = "gbk"
            if "实时热点排行榜--百度搜索风云榜" in response.text:
                soup = BeautifulSoup(response.text, "lxml")
                data_list = soup.find("table", attrs={"class": "list-table"}).find_all("tr")
                for data in data_list:
                    if not data.find("td", attrs={"class": "keyword"}):
                        continue
                    text = data.find("td", attrs={"class": "keyword"}).text.strip()
                    if "\n" in text:
                        keyword = text.strip().split("\n")[0]
                    else:
                        keyword = text
                    _id = self.retrun_md5(keyword)
                    index = data.find("td", attrs={"class": "first"}).text.strip()
                    time = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                    #time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    heat = int(data.find("td", attrs={"class": "last"}).text.strip())
                    dic = dict(
                        id=_id,
                        index=index,
                        result=[
                            dict(
                                heat=heat,
                                time=time
                            )
                        ],
                        b_keyword=keyword,
                        type="index_type",
                        text=keyword,
                    )
                    self.save_one_data_to_es(dic, _id)
            else:
                raise HttpInternalServerError
        except Exception as e:
            self.requester.use_proxy()
            raise HttpInternalServerError


if __name__ == '__main__':
    def run():
        spider = BaiDuHotSeachSpider()
        spider.get_baidu_hot_seach()


    run()
    # from apscheduler.schedulers.blocking import BlockingScheduler
    # sched = BlockingScheduler({'apscheduler.job_defaults.max_instances': '5000'})
    #
    # sched.add_job(run, 'interval', minutes=10)
    #
    # sched.start()
