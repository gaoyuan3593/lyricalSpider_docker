#! /usr/bin/python3
# -*- coding: utf-8 -*-

from service.db.utils.redis_utils import RedisQueue

page_qq = RedisQueue('article_id', namespace='article_id')

