#! /usr/bin/python3
# -*- coding: utf-8 -*-


import pickle
import time
import datetime

import apscheduler
import pytz
from service.db.utils.mongo_utils import connection
from service.micro.utils.apscheduler_ import TIME, TZ
from service import logger

EPOCH = 1970
_EPOCH_ORD = datetime.date(EPOCH, 1, 1).toordinal()

tz = pytz.timezone('Asia/Shanghai')


def timegm(tuple):
    """Unrelated but handy function to calculate Unix timestamp from GMT."""
    year, month, day, hour, minute, second = tuple[:6]
    days = datetime.date(year, month, 1).toordinal() - _EPOCH_ORD + day - 1
    hours = days * 24 + hour
    minutes = hours * 60 + minute
    seconds = minutes * 60 + second
    return seconds


def pause_job(_id):
    """
    暂停任务
    :param _id: mongo id
    :return:
    """
    _c = connection.new_media.jobs
    _parm = _c.find_one({"_id": _id})
    if _parm:
        sh_time = datetime.datetime.now(tz) + datetime.timedelta(hours=24)
        sh_date = timegm(sh_time.utctimetuple()) + sh_time.microsecond / 1000000
        job_state = pickle.loads(_parm['job_state'])
        job_state["next_run_time"] = sh_time
        _parm.update(next_run_time=sh_date)
        _parm.update(job_state=pickle.dumps(job_state))
        _c.save(_parm)
        logger.info("task pause success task_id : {}  ...".format(_id))


def resume_job(_id):
    """
    恢复任务
    :param _id:
    :return:
    """
    _c = connection.new_media.jobs
    _parm = _c.find_one({"_id": _id})
    if _parm:
        sh_time = datetime.datetime.now(tz) + datetime.timedelta(minutes=5)
        sh_date = timegm(sh_time.utctimetuple()) + sh_time.microsecond / 1000000
        job_state = pickle.loads(_parm['job_state'])
        job_state["next_run_time"] = sh_time
        _parm.update(next_run_time=sh_date)
        _parm.update(job_state=pickle.dumps(job_state))
        _c.save(_parm)
        logger.info("task resume success task_id : {}  ...".format(_id))


def remove_job(_id):
    """
    删除任务
    :param _id:
    :return:
    """
    _c = connection.new_media.jobs
    _parm = _c.find_one({"_id": _id})
    if _parm:
        _c.delete_one({"_id": _id})
        logger.info("task remove success task_id : {}  ...".format(_id))


if __name__ == '__main__':
    _id = "5e76eb1b13b85b15f6050b0cdd40da2d"
    #pause_job(_id)
    resume_job(_id)
    from apscheduler.schedulers.base import BaseScheduler
    aa = BaseScheduler()
    aa.pause_job(job_id=_id, jobstore="mongo")
