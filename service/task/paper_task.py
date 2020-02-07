#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(os.path.split(rootPath)[0])

import multiprocessing
from datetime import datetime, timedelta
from service import logger
from apscheduler.schedulers.blocking import BlockingScheduler
from service.micro.paper.china_qing_nian_bao import china_qing_nian_bao_run
from service.micro.paper.guang_ming_ri_bao import guang_ming_ri_bao_run
from service.micro.paper.jin_wan_bao import jin_wan_bao_run
from service.micro.paper.jing_ji_ri_bao import jing_ji_ri_bao_run
from service.micro.paper.mkdx import xin_hua_mei_ri_dian_xun_run
from service.micro.paper.ren_min_ri_bao import ren_min_ri_bao_run
from service.micro.paper.tj_ri_bao import tian_jin_ri_bao_run


def paper_run():
    func_list = [china_qing_nian_bao_run, guang_ming_ri_bao_run, jin_wan_bao_run,
                 jing_ji_ri_bao_run, xin_hua_mei_ri_dian_xun_run, ren_min_ri_bao_run, tian_jin_ri_bao_run]

    for func in func_list:
        w = multiprocessing.Process(target=func)
        w.start()
        w.join(2)
    logger.info("is task run over.....")


if __name__ == '__main__':
    import pytz

    tz = pytz.timezone('America/New_York')
    sched = BlockingScheduler({'apscheduler.job_defaults.max_instances': '5000'})

    sched.add_job(paper_run, 'interval', hours=4, next_run_time=datetime.now(tz) + timedelta(seconds=5))

    sched.start()
