#! /usr/bin/python3
# -*- coding: utf-8 -*-
import datetime
import random

from apscheduler.schedulers.blocking import BlockingScheduler

from service import logger
from service.micro.sina.weibo_hot_search import WeiBoHotSpider


def run_tasks():
    """
    微博热搜定时任务
    :return:
    """
    logger.info('Time: {}'.format(datetime.datetime.today().strftime('%Y-%m-%d %H:%M')))
    WeiBoHotSpider().get_hot_search_list()
    logger.info('Finish the entire task loop!')


if __name__ == '__main__':
    sched = BlockingScheduler({'apscheduler.job_defaults.max_instances': '500'})

    sched.add_job(run_tasks, 'interval', seconds=60)

    sched.start()
