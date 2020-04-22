#! /usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
import logging
import pytz
from apscheduler.jobstores.memory import MemoryJobStore

from service.utils.seq_no import generate_seq_no
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from pymongo import MongoClient
from service import logger
from pytz import utc
from service.utils.yaml_tool import get_by_name_yaml

conf = get_by_name_yaml('mongodb')

logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)

MAX_INSTANCE_NUM = 2
TIME = 300
TZ = pytz.timezone('America/New_York')

client = MongoClient(
    host='mongodb://{}'.format(conf["host"]),
    port=conf["port"],
)

jobstores = {
    'mongo': MongoDBJobStore(),
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}
# jobstores = {
#     'mongo': MongoDBJobStore(collection='jobs', client=client),
#     'default': MemoryJobStore()
# }

executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': MAX_INSTANCE_NUM,
    'misfire_grace_time': 15 * 60
}


class TaskApscheduler(object):
    """
    weeks (int) – number of weeks to wait
    days (int) – number of days to wait
    hours (int) – number of hours to wait
    minutes (int) – number of minutes to wait
    seconds (int) – number of seconds to wait
    start_date (datetime|str) – starting point for the interval calculation
    end_date (datetime|str) – latest possible date/time to trigger on
    timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations
    """

    def __init__(self, func, job_id="my_job_id"):
        self.func = func
        self.job_id = job_id

    def add_job(self):
        logger.info("Time : {}".format(datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
        scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)

        scheduler.add_job(self.func, 'interval', id=self.job_id, minutes=TIME, jobstore='mongo', replace_existing=True,
                          next_run_time=datetime.now() + timedelta(seconds=5)
                          )
        scheduler.start()


if __name__ == '__main__':
    seq_no = generate_seq_no()
    print(seq_no)

    import time


    def myfunc():
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


    task = TaskApscheduler(myfunc, seq_no)
    task.add_job()
    print(111111111111111111)
    print(22222222222222222)
