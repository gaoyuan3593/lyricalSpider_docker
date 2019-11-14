#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(os.path.split(os.path.split(rootPath)[0])[0])

from service import logger
from service.micro.sina.weibo_hot_search import WeiBoHotSpider
from datetime import datetime, timedelta
from apscheduler.schedulers.blocking import BlockingScheduler
from service.micro.baidu.baidu_hot_search import BaiDuHotSeachSpider
from service.micro.hot_search_360.hot_search_360 import HotSeach360Spider


def weibo_run():
    spider = WeiBoHotSpider()
    spider.get_hot_search_list()


def baidu_run():
    spider = BaiDuHotSeachSpider()
    spider.get_baidu_hot_seach()


def run_360():
    spider = HotSeach360Spider()
    spider.get_360_hot_seach()


if __name__ == '__main__':
    import pytz

    tz = pytz.timezone('America/New_York')
    sched = BlockingScheduler({'apscheduler.job_defaults.max_instances': '5000'})

    sched.add_job(weibo_run, 'interval', seconds=120, next_run_time=datetime.now(tz) + timedelta(seconds=5))
    sched.add_job(baidu_run, 'interval', seconds=120, next_run_time=datetime.now(tz) + timedelta(seconds=5))
    sched.add_job(run_360, 'interval', seconds=120, next_run_time=datetime.now(tz) + timedelta(seconds=5))

    sched.start()
