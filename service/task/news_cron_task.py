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
from service.micro.news.cctv_world import cctv_worl_run
from service.micro.news.china import china_spider_run
from service.micro.news.china_daily import china_daily_run
from service.micro.news.china_economy import china_economy_run
from service.micro.news.china_news import china_news_run
from service.micro.news.china_taiwan import china_taiwan_run
from service.micro.news.ckxx_news import ckxx_news_run
from service.micro.news.cri_news import cri_news_run
from service.micro.news.cyol_news import cyol_news_run
from service.micro.news.dangjian import dangjian_run
from service.micro.news.gmw_news import gmw_news_run
from service.micro.news.huanqiu_news import huanqiu_news_run
from service.micro.news.k618_news import k618_news_run
from service.micro.news.people import people_run
from service.micro.news.xfrb_news import xfrb_news_run
from service.micro.news.xinhua import xinhua_run
from service.micro.news.youth_news import youth_spider_run


def run_tasks():
    """
    新闻网站定时任务
    :return:
    """
    logger.info('Time: {}'.format(datetime.today().strftime('%Y-%m-%d %H:%M')))
    cctv_worl_run()
    china_spider_run()
    china_daily_run()
    china_economy_run()
    china_news_run()
    china_taiwan_run()
    ckxx_news_run()
    cri_news_run()
    cyol_news_run()
    dangjian_run()
    gmw_news_run()
    huanqiu_news_run()
    k618_news_run()
    people_run()
    xfrb_news_run()
    xinhua_run()
    youth_spider_run()
    logger.info('Finish the entire task loop!')


if __name__ == '__main__':
    sched = BlockingScheduler({'apscheduler.job_defaults.max_instances': '5000'})

    # 新闻网站定时任务
    sched.add_job(run_tasks, 'interval', hours=1, next_run_time=datetime.now() + timedelta(seconds=5))

    sched.start()
