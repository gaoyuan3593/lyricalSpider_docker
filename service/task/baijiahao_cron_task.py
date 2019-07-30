#! /usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(os.path.split(rootPath)[0])
from datetime import datetime, timedelta

from apscheduler.schedulers.blocking import BlockingScheduler
from service import logger
from service.micro.baidu.details_task import baijiahao_run


def run_tasks():
    """
    百家号定时任务
    :return:
    """
    logger.info('Time: {}'.format(datetime.today().strftime('%Y-%m-%d %H:%M')))
    baijiahao_run()
    logger.info('Finish the entire task loop!')


if __name__ == '__main__':
    import pytz

    tz = pytz.timezone('America/New_York')
    sched = BlockingScheduler({'apscheduler.job_defaults.max_instances': '5000'})

    # 百家号定时任务
    sched.add_job(run_tasks, 'interval', minutes=60, next_run_time=datetime.now(tz) + timedelta(seconds=5))

    sched.start()
