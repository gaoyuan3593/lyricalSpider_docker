#! /usr/bin/python3
# -*- coding: utf-8 -*-
from service import logger
from service.db.utils.redis_utils import RedisQueue

page_qq = RedisQueue('page_id', namespace='page_id')


def save_pages_req_to_redis(index, url):
    """
    # 存储待爬取任务到redis
    :param index:
    :param para:
    :return:
    """
    logger.info('save to redis: {0}, {1}'.format(index, url))
    if index == 1:
        case_info = "{}|{}".format(index, url)
        page_qq.put(case_info)

    for i in range(2, int(index + 1)):
        case_info = "{}|{}".format(i, url)
        page_qq.put(case_info)
        logger.info("save to redis success!!! data=page:{0},para:{1}".format(i, url))


def save_pages_to_redis(url):
    """
    # 微博页数url存储待爬取任务到redis
    :param url:微博页码
    :return:
    """
    logger.info('save to redis: {0}'.format(url))
    page_qq.put(url)


if __name__ == '__main__':
    a = page_qq.get_nowait()
    print(a)