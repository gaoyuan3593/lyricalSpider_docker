#! /usr/bin/python3
# -*- coding: utf-8 -*-
import datetime
from service.db.utils.redis_utils import RedisQueue
from service.micro.sina.weibo import WeiBoSpider
from service.micro.utils.threading_ import WorkerThread

page_qq = RedisQueue('page_id', namespace='page_id')


def run(weibo_obj):
    """
    方法入口
    :param params:
    :return:
    """
    wb = weibo_obj
    threads = []
    html_list, wb_data_list = [], []
    weibo_detail_list, comment_or_repost_list = [], []
    com_or_re_data_list, user_id_list = [], []
    user_info_list = []
    page_data_url_list = wb.query()
    for page_url_data in page_data_url_list:
        # 获取每页内容的html
        worker = WorkerThread(html_list, wb.get_weibo_page_data, (page_url_data,))
        worker.start()
        threads.append(worker)
    for work in threads:
        work.join()
    threads = []

    if len(html_list) >= 10:
        for html_data in html_list:
            # 解析每页的20微博内容
            worker = WorkerThread(wb_data_list, wb.parse_weibo_html, (html_data,))
            worker.start()
            threads.append(worker)
        for work in threads:
            work.join()
        threads = []
    else:
        for html_data in html_list:
            wb_data_list.append(wb.parse_weibo_html(html_data))

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
            work.join()
        threads = []

    comment_url_list, repost_url_list = wb.parse_comment_or_repost_url(weibo_detail_list)

    if comment_url_list or repost_url_list:
        for data in comment_url_list:  # 所有评论url
            weibo_id = data.get("weibo_id")
            user_id = data.get("user_id")
            for url in data.get("url_list"):
                worker = WorkerThread(comment_or_repost_list, wb.get_comment_data, (url, weibo_id, user_id))
                worker.start()
                threads.append(worker)
            for work in threads:
                work.join()
            threads = []
        for data in repost_url_list:  # 所有转发url
            weibo_id = data.get("weibo_id")
            user_id = data.get("user_id")
            for url in data.get("url_list"):
                worker = WorkerThread(comment_or_repost_list, wb.get_repost_data, (url, weibo_id, user_id))
                worker.start()
                threads.append(worker)
            for work in threads:
                work.join()
            threads = []
    # 解析所有评论和转发信息，评论和转发用户ld列表
    for data in comment_or_repost_list:
        if not data:
            continue
        if data.get("type") == "comment_type":
            worker = WorkerThread(user_id_list, wb.parse_comment_data, (data,))
            worker.start()
            threads.append(worker)
        elif data.get("type") == "repost_type":
            worker = WorkerThread(user_id_list, wb.parse_repost_data, (data,))
            worker.start()
            threads.append(worker)
    for work in threads:
        work.join()
    threads = []
    # 获取用户个人信息
    for uid in user_id_list:
        worker = WorkerThread(user_info_list, wb.get_user_info, (uid,))
        worker.start()
        threads.append(worker)
    for work in threads:
        work.join()


if __name__ == '__main__':
    # run("奔驰女车主公开录音原因")
    run("西安奔驰维权")

