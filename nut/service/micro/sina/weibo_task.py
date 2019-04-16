#! /usr/bin/python3
# -*- coding: utf-8 -*-
import datetime
from service.db.utils.redis_utils import RedisQueue
from service.micro.sina.weibo import WeiBoSpider
from service.micro.utils.threading_ import WorkerThread

page_qq = RedisQueue('page_id', namespace='page_id')


def run(params):
    """
    方法入口
    :param params:
    :return:
    """
    threads = []
    data_list, details_list = [], []
    wb_obj = WeiBoSpider(params)
    url_list = wb_obj.run()
    for url in url_list:
        worker = WorkerThread(data_list, wb_obj.get_weibo_page_data, (url,))
        worker.start()
        threads.append(worker)
    if data_list:
        for resp in data_list:
            worker = WorkerThread(details_list, wb_obj.get_weibo_details, (resp,))
            worker.start()
            threads.append(worker)
    for work in threads:
        work.join(1)
        if work.isAlive():
            threads.append(work)
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    wb_obj.save_data_to_es(details_list)
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == '__main__':
    run("艾米")
