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
from service.micro.baidu.details_task import tieba_run


def run_tasks():
    """
    百度贴吧定时任务
    :return:
    """
    logger.info('Time: {}'.format(datetime.datetime.today().strftime('%Y-%m-%d %H:%M')))
    tieba_run()
    logger.info('Finish the entire task loop!')


if __name__ == '__main__':
    sched = BlockingScheduler({'apscheduler.job_defaults.max_instances': '5000'})

    # 百度贴吧定时任务
    sched.add_job(run_tasks, 'interval', seconds=600)

    sched.start()
