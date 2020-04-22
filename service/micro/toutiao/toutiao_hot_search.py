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
from service.db.utils.elasticsearch_utils import es_client, h_es_client, HOT_SEARCH_TOUTIAO
from datetime import datetime, timedelta


class TouTiaoSeachSpider(object):
    __name__ = 'jin ri tou tiao hot search'

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
        self.es.create_index(HOT_SEARCH_TOUTIAO, _index_mapping)
        self.h_es.create_index(HOT_SEARCH_TOUTIAO, _index_mapping)

    def filter_keyword(self, id, _type, data):
        try:
            result = self.es.get(HOT_SEARCH_TOUTIAO, _type, id)
            if result.get("found"):
                data_list = []
                raw_data = result.get("_source")
                raw_heat = raw_data.get("result")
                current_heat = data.get("result")
                if current_heat[0].get("heat") != raw_heat[-1].get("heat"):
                    data_list.append(current_heat[0])
                    raw_heat.extend(data_list)
                    self.es.update(HOT_SEARCH_TOUTIAO, data.get("type"), id=id, body=raw_data)
                    self.h_es.update(HOT_SEARCH_TOUTIAO, data.get("type"), id=id, body=raw_data)
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
                logger.info("{} Data update success id: {}, text: {}".format(self.__name__, id, data.get("text")))
                return
            self.es.insert(HOT_SEARCH_TOUTIAO, _type, data, id)
            self.h_es.insert(HOT_SEARCH_TOUTIAO, _type, data, id)
            logger.info("{} save to es success [ index : {}, data={}]！".format(self.__name__, HOT_SEARCH_TOUTIAO, data))
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
    def get_toutiao_hot_seach(self):
        logger.info('Processing get jin ri tou tiao hot search list!')
        url = 'https://lf.snssdk.com/api/suggest_words/?business_id=10017'
        headers = {
            "accept": "text/javascript, text/html, application/xml, text/xml, */*",
            'user-agent': "Mozilla/5.0 (Linux; Android 8.1.0; vivo Y83A Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36  JsSdk/2 NewsArticle/7.2.2 NetType/wifi (NewsLite 7.2.2)  TTWebView/0621111013018",
            'x-requested-with': 'XMLHttpRequest',
            'content-type': 'application/x-www-form-urlencoded',
            'accept-encoding': 'gzip, deflate',
            # 'accept-language': ' zh-CN,en-US;q=0.9'
        }
        try:
            response = self.requester.get(url=url, header_dict=headers)
            # response.encoding = "gbk"
            if "今日热搜" in response.text and response.status_code == 200:
                data_list = response.json().get("data")[0].get("words")
                for data in data_list:
                    keyword = data.get("word")
                    _id = data.get("id")
                    index = data_list.index(data) + 1
                    time = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                    heat = data.get("params").get("fake_click_cnt")
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
        spider = TouTiaoSeachSpider()
        spider.get_toutiao_hot_seach()


    run()
    # from apscheduler.schedulers.blocking import BlockingScheduler
    # sched = BlockingScheduler({'apscheduler.job_defaults.max_instances': '5000'})
    #
    # sched.add_job(run, 'interval', minutes=10)
    #
    # sched.start()
