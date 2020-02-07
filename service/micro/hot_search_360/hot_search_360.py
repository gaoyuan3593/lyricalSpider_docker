#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random
import time
import json
import hashlib
from service.core.utils.http_ import Requester
from service.exception import retry
from service.exception.exceptions import *
from service import logger
from service.micro.utils import ua
from service.db.utils.es_mappings import HOT_SEARCH_KEYWORD_MAPPING
from service.db.utils.elasticsearch_utils import es_client, HOT_SEARCH_360
from datetime import datetime, timedelta


class HotSeach360Spider(object):
    __name__ = '360 hot search'

    def __init__(self):
        self.requester = Requester(timeout=20)
        self.es = es_client
        self.create_index()

    def create_index(self):
        _index_mapping = {
            "index_type":
                {
                    "properties": HOT_SEARCH_KEYWORD_MAPPING
                },
        }
        self.es.create_index(HOT_SEARCH_360, _index_mapping)

    def filter_keyword(self, id, _type, data):
        try:
            result = self.es.get(HOT_SEARCH_360, _type, id)
            if result.get("found"):
                data_list = []
                raw_data = result.get("_source")
                raw_heat = raw_data.get("result")
                current_heat = data.get("result")
                if current_heat[0].get("heat") != raw_heat[-1].get("heat"):
                    data_list.append(current_heat[0])
                    raw_heat.extend(data_list)
                    self.es.update(HOT_SEARCH_360, data.get("type"), id=id, body=raw_data)
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
                logger.info("Data update success id: {}".format(id))
                return
            self.es.insert(HOT_SEARCH_360, _type, data, id)
            logger.info("save to es success [ index : {}, data={}]！".format(HOT_SEARCH_360, data))
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
    def get_360_hot_seach(self):
        logger.info('Processing get 360 hot search list!')
        url = 'https://trends.so.com/top/realtime'
        headers = {
            'User-Agent': ua(),
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Referer': 'https://trends.so.com/hot'
        }
        try:
            response = self.requester.get(url=url, header_dict=headers)
            if response.json().get("status") == 0:
                result = response.json().get("data").get("result")
                for data in result[:50]:
                    keyword = data.get("query")
                    _id = self.retrun_md5(keyword)
                    index = result.index(data) + 1
                    time = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                    heat = int(data.get("heat"))
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
                        text=keyword
                    )
                    self.save_one_data_to_es(dic, _id)
            else:
                raise HttpInternalServerError
        except Exception as e:
            self.requester.use_proxy()
            raise HttpInternalServerError


if __name__ == '__main__':

    def run():
        spider = HotSeach360Spider()
        spider.get_360_hot_seach()

    run()
    # from apscheduler.schedulers.blocking import BlockingScheduler
    # sched = BlockingScheduler({'apscheduler.job_defaults.max_instances': '5000'})
    #
    # sched.add_job(run, 'interval', minutes=10)
    #
    # sched.start()
