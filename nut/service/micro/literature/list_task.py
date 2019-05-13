#! /usr/bin/python3
# -*- coding: utf-8 -*-
import threadpool
from micro.literature.cnki_app import CnkiSpider


def cnki_run():
    for key_word in ["国际新闻界", "新闻与传播研究", "新闻大学", "现代传播"]:
        cn = CnkiSpider(key_word)
        url_list, threads = [], []
        resp_list = cn.get_cnki_begin()
        for resp in resp_list:
            data = cn.parse_detail_url_list(resp)
            url_list.extend(data)

        detail_list, threads = [], []

        def callback(raw_data_list, data):
            detail_list.append(data)

        pool = threadpool.ThreadPool(20)
        tasks = threadpool.makeRequests(cn.get_cnki_dtail, url_list, callback)
        for task in tasks:
            pool.putRequest(task)
        pool.wait()
        data_list = []
        for resp in detail_list:
            try:
                detail = cn.parse_cnki_detail(resp)
                data_list.append(detail)
            except Exception as e:
                continue
        cn.save_data_to_excel(data_list)


if __name__ == '__main__':
    cnki_run()
