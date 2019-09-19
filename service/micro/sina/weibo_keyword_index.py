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


def run():
    spider = WeiBoHotSpider()
    data = spider.get_hot_search_list()


if __name__ == '__main__':
    import pytz

    tz = pytz.timezone('America/New_York')
    sched = BlockingScheduler({'apscheduler.job_defaults.max_instances': '5000'})

    # 微博热搜定时任务
    sched.add_job(run, 'interval', seconds=3, next_run_time=datetime.now(tz) + timedelta(seconds=5))
    # 中国知网定时任务
    # sched.add_job(run_cnki_tasks, 'interval', days=7)

    sched.start()
