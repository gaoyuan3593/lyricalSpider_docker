#! /usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os
import datetime

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(os.path.split(rootPath)[0])

from apscheduler.schedulers.blocking import BlockingScheduler
from service import logger
from service.micro.sougou_wechat.sougou_task import wechat_key_run, wechat_hot_run


def run_keyword_tasks():
    """
    搜狗微信关键字定时任务
    :return:
    """
    logger.info('Time: {}'.format(datetime.datetime.today().strftime('%Y-%m-%d %H:%M')))
    wechat_key_run()
    logger.info('Finish the entire task loop!')


def run_wechat_hot_tasks():
    """
    搜狗微信热搜定时任务
    :return:
    """
    logger.info('Time: {}'.format(datetime.datetime.today().strftime('%Y-%m-%d %H:%M')))
    wechat_hot_run()
    logger.info('Finish the entire task loop!')


if __name__ == '__main__':
    sched = BlockingScheduler({'apscheduler.job_defaults.max_instances': '5000'})

    # 搜狗微信关键字定时任务
    sched.add_job(run_keyword_tasks, 'interval', seconds=600)

    # 搜狗微信热搜定时任务
    sched.add_job(run_wechat_hot_tasks, 'interval', seconds=3600)
    sched.start()
