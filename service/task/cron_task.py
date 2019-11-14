#! /usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(os.path.split(rootPath)[0])
print(sys.path)
from datetime import datetime, timedelta

from apscheduler.schedulers.blocking import BlockingScheduler
from service import logger
from service.micro.sina.list_task import weibo_hot_run
from service.micro.literature.list_task import cnki_run


def run_tasks():
    """
    微博热搜定时任务
    :return:
    """
    logger.info('Time: {}'.format(datetime.today().strftime('%Y-%m-%d %H:%M')))
    weibo_hot_run()
    logger.info('Finish the entire task loop!')


def run_cnki_tasks():
    """
    中国知网定时任务
    :return:
    """
    logger.info('Time: {}'.format(datetime.today().strftime('%Y-%m-%d %H:%M')))
    cnki_run()
    logger.info('Finish the entire task loop!')


if __name__ == '__main__':
    import pytz
    print('datetime : {}'.format(datetime.now() + timedelta(seconds=5)))
    tz = pytz.timezone('America/New_York')
    logger.info('datetime : {}'.format(datetime.now(tz) + timedelta(seconds=5)))
    sched = BlockingScheduler({'apscheduler.job_defaults.max_instances': '5000'})
    logger.info('datetime : {}'.format(datetime.now(tz) + timedelta(seconds=5)))
    # 微博热搜定时任务
    sched.add_job(weibo_hot_run, 'interval', minutes=120, next_run_time=datetime.now(tz) + timedelta(seconds=5))
    # 中国知网定时任务
    # sched.add_job(run_cnki_tasks, 'interval', days=7)

    sched.start()
