#! /usr/bin/python3
# -*- coding: utf-8 -*-

from service import logger
from service.utils.yaml_tool import get_by_name_yaml
import random
import redis

conf = get_by_name_yaml('redis')
# 页码
WEIBO_PAGE_REDIS_URL = 'redis://:%s@%s:%s/1' % (conf['password'], conf['host'], conf['port'])
# 评论
WEIBO_CONTENT_REDIS_URL = 'redis://:%s@%s:%s/2' % (conf['password'], conf['host'], conf['port'])
# 转发
WEIBO_FORWARD_REDIS_URL = 'redis://:%s@%s:%s/3' % (conf['password'], conf['host'], conf['port'])


def redis_cli(url):
    import re
    m = re.match('^redis://:(.*)@(.*):(.*)/(.*)', url)
    password, host, port, db = m.groups()
    import redis
    return redis.Redis(
        host=host,
        port=port,
        db=db,
        password=password
    )


class RedisQueue(object):
    def __init__(self, name, namespace='queue', **redis_kwargs):
       self.__db = redis_cli(WEIBO_PAGE_REDIS_URL)
       self.key = '{}:{}'.format(namespace, name)

    def qsize(self):
        return self.__db.llen(self.key)

    def put(self, item):
        self.__db.rpush(self.key, item)

    def get_wait(self, timeout=None):
        item = self.__db.blpop(self.key, timeout=timeout)
        return item

    def get_nowait(self):
        item = self.__db.lpop(self.key)
        return item


class RedisClient(object):
    def __init__(self, type, website, host=conf['host'], port=conf['port'], password=conf['password']):
        """
        初始化Redis连接
        :param host: 地址
        :param port: 端口
        :param password: 密码
        """
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)
        self.type = type
        self.website = website

    def name(self):
        """
        获取Hash的名称
        :return: Hash名称
        """
        return "{type}:{website}".format(type=self.type, website=self.website)

    def set(self, username, value):
        """
        设置键值对
        :param username: 用户名
        :param value: 密码或Cookies
        :return:
        """
        return self.db.hset(self.name(), username, value)

    def get(self, username):
        """
        根据键名获取键值
        :param username: 用户名
        :return:
        """
        return self.db.hget(self.name(), username)

    def delete(self, username):
        """
        根据键名删除键值对
        :param username: 用户名
        :return: 删除结果
        """
        return self.db.hdel(self.name(), username)

    def count(self):
        """
        获取数目
        :return: 数目
        """
        return self.db.hlen(self.name())

    def random(self):
        """
        随机得到键值，用于随机Cookies获取
        :return: 随机Cookies
        """
        return random.choice(self.db.hvals(self.name()))

    def usernames(self):
        """
        获取所有账户信息
        :return: 所有用户名
        """
        return self.db.hkeys(self.name())

    def all(self):
        """
        获取所有键值对
        :return: 用户名和密码或Cookies的映射表
        """
        return self.db.hgetall(self.name())

    def return_choice_cookie(self):
        """
        :return: 一个随机cookie
        """
        user_name = random.choice(list(self.all()))
        return self.get(user_name)


if __name__ == '__main__':
    conn = RedisClient('accounts', 'weibo')
    conn_cookie = RedisClient('cookies', 'weibo')
    result = conn.usernames()
    user = random.choice(list(conn_cookie.all()))
    result2 = conn_cookie.get(user)
    print(result)
