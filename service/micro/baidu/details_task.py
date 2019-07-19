#! /usr/bin/python3
# -*- coding: utf-8 -*-

from service import logger
import threadpool
from service.micro.baidu.baijiahao import BaiJiaHaoSpider
from service.micro.baidu.tieba import TiebaSpider
from micro.utils.threading_ import WorkerThread
from micro.utils.threading_parse import WorkerThreadParse


def baijiahao_run():
    logger.info("baijiahao it run start")
    acticle_detail_list = []
    acticle_url_list = []
    threads = []

    bjh = BaiJiaHaoSpider()
    keyword_list = bjh.get_weibo_hot_seach()

    for keyword in keyword_list:
        worker = WorkerThread(acticle_url_list, bjh.get_begin_page_url, (keyword,))
        worker.start()
        threads.append(worker)
    for work in threads:
        work.join(1)
        if work.isAlive():
            logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
            threads.append(work)
    threads = []
    for url_dic in acticle_url_list:
        worker = WorkerThread(acticle_detail_list, bjh.get_acticle_detail, (url_dic,))
        worker.start()
        threads.append(worker)
    for work in threads:
        work.join(1)
        if work.isAlive():
            logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
            threads.append(work)

    pool = threadpool.ThreadPool(5)
    tasks = threadpool.makeRequests(bjh.parse_baijiahao_article_detail, acticle_detail_list)
    for task in tasks:
        pool.putRequest(task)
    pool.wait()


def tieba_run():
    logger.info("bai du tie ba it run start")

    url_list, page_data_list, tiezi_url_list, replay_url_list = [], [], [], []
    threads = []
    tieba = TiebaSpider()

    keyword_list = tieba.get_weibo_hot_seach()
    for keyword in keyword_list:
        worker = WorkerThreadParse(url_list, tieba.get_begin_page_url, (keyword,))
        worker.start()
        threads.append(worker)
    for work in threads:
        work.join(1)
        if work.isAlive():
            logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
            threads.append(work)
    # 获取所有页的html
    threads = []
    for url_dic in url_list:
        worker = WorkerThreadParse(page_data_list, tieba.get_page_url_data, (url_dic,))
        worker.start()
        threads.append(worker)
    for work in threads:
        work.join(1)
        if work.isAlive():
            logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
            threads.append(work)

    # 解析 发帖的内容
    threads = []
    for resp_dic in page_data_list:
        worker = WorkerThreadParse(tiezi_url_list, tieba.parse_tiezi_detail, (resp_dic,))
        worker.start()
        threads.append(worker)
    for work in threads:
        work.join(1)
        if work.isAlive():
            logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
            threads.append(work)

    # 获取 贴子内的 回复内容
    threads = []
    for tiezi_url_dic in tiezi_url_list:
        worker = WorkerThreadParse(replay_url_list, tieba.get_tiezi_data_url, (tiezi_url_dic,))
        worker.start()
        threads.append(worker)
    for work in threads:
        work.join(1)
        if work.isAlive():
            logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
            threads.append(work)
    threads = []
    for repaly in replay_url_list:
        worker = WorkerThreadParse([], tieba.get_next_data, (repaly,))
        worker.start()
        threads.append(worker)
    for work in threads:
        work.join(1)
        if work.isAlive():
            logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
            threads.append(work)
