#! /usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from service.utils.seq_no import generate_seq_no
from pytz import utc

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

MAX_INSTANCE_NUM = 50
TIME = 60

jobstores = {
    'mongo': MongoDBJobStore(),
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}

executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': MAX_INSTANCE_NUM
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

    def __init__(self, func=None, status=None, job_id="my_job_id"):
        self.job_id = job_id
        self.func = func
        self.status = status

    def add_job(self):
        scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors,
                                        job_defaults=job_defaults, )  # timezone=utc)
        scheduler.add_job(self.func, 'interval', id=self.job_id, minutes=TIME, jobstore='mongo',
                          next_run_time=datetime.now() + timedelta(seconds=5))
        scheduler.start()


if __name__ == '__main__':
    seq_no = generate_seq_no()
    print(seq_no)

    import time


    def myfunc():
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))