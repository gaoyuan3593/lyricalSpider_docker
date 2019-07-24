#! /usr/bin/python3
# -*- coding: utf-8 -*-

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
    sched = BlockingScheduler({'apscheduler.job_defaults.max_instances': '5000'})

    # 百家号定时任务
    sched.add_job(run_tasks, 'interval', minutes=6, next_run_time=datetime.now() + timedelta(seconds=5))

    sched.start()
