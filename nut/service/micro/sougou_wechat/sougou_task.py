#! /usr/bin/python3
# -*- coding: utf-8 -*-
import datetime

from service import logger
from service.micro.utils.threading_ import WorkerThread
from service.micro.sougou_wechat.sougou_keyword import SouGouKeywordSpider
from service.micro.sougou_wechat.sougou_hot_search import SouGouHotSpider


def wechat_key_run():
    """
    搜狗微信关键字方法入口
    :param params:
    :return:
    """

    weichat = SouGouKeywordSpider()
    threads = []
    data_list, weixin_article_url_list = [], []
    article_detail_list, url_list = [], []

    keyword_list = weichat.get_weibo_hot_seach()
    for keyword_data in keyword_list:
        try:
            url_list.extend(weichat.get_weixin_page_url(keyword_data))
        except:
            continue

    for url_data in url_list:
        try:
            data = weichat.get_weixin_page_data(url_data)
            if data:
                data_list.append(data)
        except Exception as e:
            continue
    if data_list:
        for data in data_list:
            # 解析所有页的文章url
            # weixin_article_url_list.extend(weichat.parse_weixin_article_url(data))
            worker = WorkerThread(weixin_article_url_list, weichat.parse_weixin_article_url, (data,))
            worker.start()
            threads.append(worker)
        for work in threads:
            work.join(1)
            if work.isAlive():
                logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
                threads.append(work)
    threads = []
    for article_data in weixin_article_url_list:
        worker = WorkerThread(article_detail_list, weichat.get_weixin_article_details, (article_data,))
        worker.start()
        threads.append(worker)
    for work in threads:
        work.join(1)
        if work.isAlive():
            logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
            threads.append(work)

    threads = []
    for article in article_detail_list:
        # weichat.parse_weixin_article_detail(article)
        worker = WorkerThread([], weichat.parse_weixin_article_detail, (article,))
        worker.start()
        threads.append(worker)
    for work in threads:
        work.join(1)
        if work.isAlive():
            logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
            threads.append(work)


def wechat_hot_run():
    """
    搜狗微信热搜方法入口
    :param params:
    :return:
    """
    weichat = SouGouHotSpider()
    threads = []
    data_list, weixin_article_url_list = [], []
    article_detail_list, url_list = [], []

    keyword_list = weichat.get_sougou_hot_seach()
    for keyword_data in keyword_list:
        try:
            url_list.extend(weichat.get_weixin_page_url(keyword_data))
        except:
            continue
    for url_data in url_list:
        try:
            data = weichat.get_weixin_page_data(url_data)
            if data:
                data_list.append(data)
        except Exception as e:
            continue

    if data_list:
        for data in data_list:
            # 解析所有页的文章url
            # weixin_article_url_list.extend(weichat.parse_weixin_article_url(data))
            worker = WorkerThread(weixin_article_url_list, weichat.parse_weixin_article_url, (data,))
            worker.start()
            threads.append(worker)
        for work in threads:
            work.join(1)
            if work.isAlive():
                logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
                threads.append(work)
    threads = []
    for article_data in weixin_article_url_list:
        worker = WorkerThread(article_detail_list, weichat.get_weixin_article_details, (article_data,))
        worker.start()
        threads.append(worker)
    for work in threads:
        work.join(1)
        if work.isAlive():
            logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
            threads.append(work)

    threads = []
    for article in article_detail_list:
        # weichat.parse_weixin_article_detail(article)
        worker = WorkerThread([], weichat.parse_weixin_article_detail, (article,))
        worker.start()
        threads.append(worker)
    for work in threads:
        work.join(1)
        if work.isAlive():
            logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
            threads.append(work)


if __name__ == '__main__':
    wechat_key_run()
