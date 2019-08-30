#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(os.path.split(os.path.split(rootPath)[0])[0])

import multiprocessing
from service.micro.utils.threading_ import WorkerThread
from service import logger
from service.db.utils.redis_utils import WEIBO_COMMENT_QQ, WEIBO_REPOST_QQ
from service.micro.sina.weibo_hot_search import WeiBoHotSpider
from datetime import datetime

spider = WeiBoHotSpider()


def get_redis_comment_url():
    case_info = WEIBO_COMMENT_QQ.get_nowait()
    if not case_info:
        logger.info("not url")
        return
    weibo_id, user_id, url = case_info.decode("utf-8").split("|")
    try:
        dic = spider.get_comment_data(url, weibo_id, user_id)
        user_id_list = spider.parse_comment_data(dic)
        parse_user_info(user_id_list)
    except Exception as e:
        WEIBO_COMMENT_QQ.put(case_info)
        raise e


def get_redis_repost_url():
    case_info = WEIBO_REPOST_QQ.get_nowait()
    if not case_info:
        logger.info("not url")
        return
    weibo_id, user_id, url = case_info.decode("utf-8").split("|")
    try:
        dic = spider.get_repost_data(url, weibo_id, user_id)
        user_id_list = spider.parse_repost_data(dic)
        parse_user_info(user_id_list)
    except Exception as e:
        WEIBO_REPOST_QQ.put(case_info)
        raise e


def parse_user_info(user_id_list):
    user_info_list, threads = [], []
    user_url_list = spider.parse_user_info_url(user_id_list)
    for url_data in user_url_list:
        worker = WorkerThread(user_info_list, spider.get_user_info, (url_data,))
        worker.start()
        threads.append(worker)
    for work in threads:
        work.join()
        if work.isAlive():
            logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
            threads.append(work)
    for user_data in user_info_list:
        worker = WorkerThread([], spider.get_profile_user_info, (user_data,))
        worker.start()

    print("完成时间 %s" % datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == '__main__':
    import gc

    while True:
        # func_list = [get_redis_comment_url, get_redis_repost_url]
        # for func in func_list:
        #     w = multiprocessing.Process(target=func)
        #     w.start()
        #     w.join()
        try:
            get_redis_comment_url()
            get_redis_repost_url()
            logger.info("释放内存")
            gc.collect()
        except:
            continue