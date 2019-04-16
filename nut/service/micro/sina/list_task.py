#! /usr/bin/python3
# -*- coding: utf-8 -*-
from service import logger
from service.db.utils.redis_utils import RedisQueue

page_qq = RedisQueue('page_id', namespace='page_id')


def save_pages_to_redis(keyword, url):
    """
    # 微博页数url存储待爬取任务到redis
    :param url:微博页码
    :return:
    """
    logger.info('save to redis: {0}'.format(url))
    case_info = "{}|{}".format(keyword, url)
    page_qq.put(case_info)
    logger.info("save to redis success!!! key_word:{0},url:{1}".format(keyword, url))


if __name__ == '__main__':
    a = page_qq.get_nowait()
    print(a)
