#! /usr/bin/python3
# -*- coding: utf-8 -*-

from service import logger
from service.micro.utils.threading_ import WorkerThread
from service.micro.utils.threading_parse import WorkerThreadParse
from service.micro.sina.weibo_hot_search import WeiBoHotSpider


def weibo_hot_run():
    wb = WeiBoHotSpider()
    threads = []
    data_list, page_data_url_list = [], []
    html_list, wb_data_list = [], []
    weibo_detail_list, repost_list, comment_list = [], [], []
    com_or_re_data_list, user_id_list = [], []
    user_info_list = []

    resp_list, url_list = wb.get_hot_search_list()
    for url_data in url_list:
        # 获取每条热搜页的html
        worker = WorkerThread(data_list, wb.get_weibo_page_data, (url_data,))
        worker.start()
        threads.append(worker)
    for work in threads:
        work.join(1)
        if work.isAlive():
            logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
            threads.append(work)
    threads = []
    if data_list:
        for data in data_list:
            # 解析每个热搜的所有页的url
            worker = WorkerThreadParse(page_data_url_list, wb.parse_weibo_page_url, (data,))
            worker.start()
            threads.append(worker)
        for work in threads:
            work.join(1)
            if work.isAlive():
                logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
                threads.append(work)
        threads = []
    if page_data_url_list:
        for page_url_data in page_data_url_list:
            # 获取每页内容的html
            worker = WorkerThread(html_list, wb.get_weibo_page_data, (page_url_data,))
            worker.start()
            threads.append(worker)
        for work in threads:
            work.join(1)
            if work.isAlive():
                logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
                threads.append(work)
        threads = []
    if html_list:
        for html_data in html_list:
            # 解析每页的20微博内容
            worker = WorkerThreadParse(wb_data_list, wb.parse_weibo_html, (html_data,))
            worker.start()
            threads.append(worker)
        for work in threads:
            work.join(1)
            if work.isAlive():
                logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
                threads.append(work)
        threads = []
    for wb_data in wb_data_list:
        # 解析微博详情
        if not wb_data:
            continue
        keyword = wb_data.get("keyword")
        for data in wb_data.get("data"):
            worker = WorkerThread(weibo_detail_list, wb.parse_weibo_detail, (data, keyword))
            worker.start()
            threads.append(worker)
        for work in threads:
            work.join(1)
            if work.isAlive():
                logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
                threads.append(work)
        threads = []

    wb.parse_comment_or_repost_url(weibo_detail_list)


if __name__ == '__main__':
    weibo_hot_run()
