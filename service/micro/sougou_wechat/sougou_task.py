#! /usr/bin/python3
# -*- coding: utf-8 -*-

from service import logger
from service.micro.utils.threading_ import WorkerThread
from service.micro.utils.threading_parse import WorkerThreadParse
from service.micro.sougou_wechat.sougou_keyword import SouGouKeywordSpider
from service.micro.sougou_wechat.sougou_hot_search import SouGouHotSpider


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

    weibo_key_list = weichat.get_weibo_hot_seach()
    keyword_list = weichat.get_sougou_hot_seach()
    keyword_list.extend(weibo_key_list)
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
            worker = WorkerThreadParse(weixin_article_url_list, weichat.parse_weixin_article_url, (data,))
            worker.start()
            threads.append(worker)
        for work in threads:
            work.join(1)
            if work.isAlive():
                logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
                threads.append(work)

    for article_data in weixin_article_url_list:
        #     worker = WorkerThread(article_detail_list, weichat.get_weixin_article_details, (article_data,))
        #     worker.start()
        #     threads.append(worker)
        # for work in threads:
        #     work.join(1)
        #     if work.isAlive():
        #         logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
        #         threads.append(work)
        try:
            weichat.get_weixin_article_details(article_data)
        except Exception as e:
            continue


if __name__ == '__main__':
    wechat_hot_run()