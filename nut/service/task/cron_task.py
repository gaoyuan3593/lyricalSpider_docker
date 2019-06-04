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
from service.micro.sina.list_task import weibo_hot_run
from service.micro.literature.list_task import cnki_run
from service.micro.sougou_wechat.sougou_task import wechat_key_run, wechat_hot_run


def run_tasks():
    """
    微博热搜定时任务
    :return:
    """
    logger.info('Time: {}'.format(datetime.datetime.today().strftime('%Y-%m-%d %H:%M')))
    weibo_hot_run()
    logger.info('Finish the entire task loop!')


def run_cnki_tasks():
    """
    中国知网定时任务
    :return:
    """
    logger.info('Time: {}'.format(datetime.datetime.today().strftime('%Y-%m-%d %H:%M')))
    cnki_run()
    logger.info('Finish the entire task loop!')


def run_wechat_key_tasks():
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

    # 微博热搜定时任务
    sched.add_job(weibo_hot_run, 'interval', seconds=600)

    # 中国知网定时任务
    sched.add_job(run_cnki_tasks, 'interval', days=7)

    # 搜狗微信关键字定时任务
    sched.add_job(run_wechat_key_tasks, 'interval', days=600)

    # 搜狗微信热搜定时任务
    sched.add_job(run_wechat_hot_tasks, 'interval', days=3600)

    sched.start()
