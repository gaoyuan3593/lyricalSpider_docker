#! /usr/bin/python3
# -*- coding: utf-8 -*-

from service import logger
from service.utils.yaml_tool import get_by_name_yaml
from service.core.config.redis_ import weibo_redis_cli, event_redis_cli
import random
import redis

conf = get_by_name_yaml('redis')


class RedisQueue(object):
    def __init__(self, name, namespace='queue', redis_cli=event_redis_cli):
        self.__db = redis_cli
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


def get_redis_key(k):
    logger.info("get_redid_key key:{}".format(k))
    try:
        v = weibo_redis_cli.get(k)
    except Exception as e:
        logger.exception(e)
    logger.info("get_redid_key values:{}".format(v))
    if v:
        v = v.decode('utf-8')
        logger.info('get cookie from redis: {}'.format(v))
        return v
    else:
        return None


# 微博评论qq
WEIBO_COMMENT_QQ = RedisQueue('weibo_comment_qq', namespace='weibo_comment_qq')

# 微博转发qq
WEIBO_REPOST_QQ = RedisQueue('weibo_repost_qq', namespace='weibo_repost_qq')

if __name__ == '__main__':
    import json

    task_qq = RedisQueue('task_id_index_qq', namespace="33bc32628785b44ab22f78b8b91d8cd9")
    data = [{"weibo_index": "weibo_shi_shui_fa_xian_le_bing_du_1580364476",
             "keyword": "\u662f\u8ab0\u53d1\u73b0\u4e86\u75c5\u6bd2"},
            {"wechat_index": "wechat_shi_shui_fa_xian_le_bing_du_1580364476",
             "keyword": "\u662f\u8ab0\u53d1\u73b0\u4e86\u75c5\u6bd2"},
            {"tieba_index": "tieba_shi_shui_fa_xian_le_bing_du_1580364476",
             "keyword": "\u662f\u8ab0\u53d1\u73b0\u4e86\u75c5\u6bd2"},
            {"baijiahao_index": "baijiahao_shi_shui_fa_xian_le_bing_du_1580364476",
             "keyword": "\u662f\u8ab0\u53d1\u73b0\u4e86\u75c5\u6bd2"},
            {"zhihu_index": "zhihu_shi_shui_fa_xian_le_bing_du_1580364476",
             "keyword": "\u662f\u8ab0\u53d1\u73b0\u4e86\u75c5\u6bd2"}]
    case_info = json.dumps(data)
    task_qq.put(case_info)



