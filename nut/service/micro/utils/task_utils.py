#! /usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
import random
from apscheduler.schedulers.blocking import BlockingScheduler
from service import logger
from service.micro.sina.weibo_keyword import WeiBoSpider


def run_weibo_tasks():
    """
    微博热搜定时任务
    :return:
    """
    logger.info('Time: {}'.format(datetime.datetime.today().strftime('%Y-%m-%d %H:%M')))
    logger.info('Finish the entire task loop!')
    sched = BlockingScheduler({'apscheduler.job_defaults.max_instances': '500'})
    sched.add_job(WeiBoSpider().run(), trigger='interval', seconds=2, id="page_id")
    #sched.remove_job("page_id")
    sched.start()


if __name__ == '__main__':
    run_weibo_tasks()