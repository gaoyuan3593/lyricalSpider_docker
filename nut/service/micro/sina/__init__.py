#! /usr/bin/python3
# -*- coding: utf-8 -*-
import redis
r = redis.Redis(host='172.19.135.135', port=6379, password="tjunmwz123",db=1, decode_responses=True)
#list_keys = r.keys("weibo_user_qq:weibo_user_qq")
#list_keys = r.keys("weibo_repost_qq:weibo_repost_qq")
list_keys = r.keys("weibo_comment_qq:weibo_comment_qq")


for key in list_keys:
    r.delete(key)