#! /usr/bin/python3
# -*- coding: utf-8 -*-
import datetime
import random

from apscheduler.schedulers.blocking import BlockingScheduler
from service import logger
from service.micro.sina.list_task import weibo_hot_run


def run_tasks():
    """
    微博热搜定时任务
    :return:
    """
    logger.info('Time: {}'.format(datetime.datetime.today().strftime('%Y-%m-%d %H:%M')))
    weibo_hot_run()
    logger.info('Finish the entire task loop!')


if __name__ == '__main__':
    sched = BlockingScheduler({'apscheduler.job_defaults.max_instances': '500'})

    sched.add_job(weibo_hot_run, 'interval', seconds=600)

    sched.start()
