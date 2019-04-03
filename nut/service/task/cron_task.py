#! /usr/bin/python3
# -*- coding: utf-8 -*-
import datetime
import random

from apscheduler.schedulers.blocking import BlockingScheduler

from service import logger
from service.micro.referee import CASES_TYPE
from service.micro.referee.detail_task import run_, run_details, run_to_redis
from service.micro.referee.list_task import run_ as run_list
from service.micro.referee.new_list_task import run_ as referee_date_run


def run_tasks():
    logger.info('Time: {}'.format(datetime.datetime.today().strftime('%Y-%m-%d %H:%M')))
    run_list(random.choice(CASES_TYPE))

    logger.info('Finish the entire task loop!')


def run_referee_date_tasks():
    logger.info('Time: {}'.format(datetime.datetime.today().strftime('%Y-%m-%d %H:%M')))
    referee_date_run(random.choice(CASES_TYPE))

    logger.info('Finish the entire referee date task loop!')


def run_redis_task():
    logger.info('Time: {0}, task: redis'.format(datetime.datetime.today().strftime('%Y-%m-%d %H:%M')))
    run_()
    logger.info('Finish the entire task loop!')


def run_detail_task():
    logger.info('Begin redis detail task')
    run_details()
    logger.info('Finish the detail task!')


def run_put_redis_from_mongo():
    logger.info('Begin put into redis')
    run_to_redis()


if __name__ == '__main__':
    sched = BlockingScheduler({'apscheduler.job_defaults.max_instances': '500'})

    sched.add_job(run_tasks, 'interval', seconds=60)
    sched.add_job(run_referee_date_tasks, 'interval', seconds=10)
    # 定时将mongo中的case detail put to qq
    # sched.add_job(run_put_redis_from_mongo, 'interval', seconds=50)
    #
    sched.add_job(run_redis_task, 'interval', seconds=0.3)
    # sched.add_job(run_detail_task, 'interval', seconds=1)

    sched.start()
