#! /usr/bin/python3
# -*- coding: utf-8 -*-

from service import logger
from service.micro.utils.threading_ import WorkerThread
from service.micro.sina.weibo_hot_search import WeiBoHotSpider


def weibo_hot_run():
    wb = WeiBoHotSpider()
    threads = []
    data_list, page_data_url_list = [], []
    html_list, wb_data_list = [], []

    url_list = wb.get_hot_search_list()
    for url_data in url_list:
        # 获取每条热搜页的html
        try:
            data_list.append(wb.get_weibo_page_data(url_data, ))
        except Exception as e:
            url_list.append(url_data)
    if data_list:
        for data in data_list:
            # 解析每个热搜的所有页的url
            try:
                page_data = wb.parse_weibo_page_url(data)
                page_data_url_list.extend(page_data)
            except Exception as e:
                continue
    if page_data_url_list:
        for page_url_data in page_data_url_list:
            # 获取每页内容的html
            try:
                html = wb.get_weibo_page_data(page_url_data, )
                if html:
                    html_list.append(html)
            except Exception as e:
                continue
        #     worker = WorkerThread(html_list, wb.get_weibo_page_data, (page_url_data,))
        #     worker.start()
        #     threads.append(worker)
        # for work in threads:
        #     work.join(1)
        #     if work.isAlive():
        #         logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
        # threads = []
    if html_list:
        for html_data in html_list:
            # 解析每页的20微博内容
            try:
                wb_data_list.append(wb.parse_weibo_html(html_data))
            except Exception as e:
                continue
        #     worker = WorkerThreadParse(wb_data_list, wb.parse_weibo_html, (html_data,))
        #     worker.start()
        #     threads.append(worker)
        # for work in threads:
        #     work.join(1)
        #     if work.isAlive():
        #         logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
        # threads = []
    for wb_data in wb_data_list:
        # 解析微博详情
        if not wb_data:
            continue
        keyword = wb_data.get("keyword")
        for data in wb_data.get("data"):
            wb.parse_weibo_detail(data, keyword)
        #     worker = WorkerThread([], wb.parse_weibo_detail, (data, keyword))
        #     worker.start()
        #     threads.append(worker)
        # for work in threads:
        #     work.join(1)
        #     if work.isAlive():
        #         logger.info('Worker thread: failed to join, and still alive, and rejoin it.')


if __name__ == '__main__':
    weibo_hot_run()
