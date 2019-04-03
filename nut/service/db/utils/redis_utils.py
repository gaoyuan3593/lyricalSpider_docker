#! /usr/bin/python3
# -*- coding: utf-8 -*-
from service import logger
from service.utils.yaml_tool import get_by_name_yaml

conf = get_by_name_yaml('redis')

SEQ_NO_REDIS_URL = 'redis://:%s@%s:%s/0' % (conf['password'], conf['host'], conf['port'])
COOKIE_REDIS_URL = 'redis://:%s@%s:%s/1' % (conf['password'], conf['host'], conf['port'])
REFEREES_REDIS_URL = 'redis://:%s@%s:%s/3' % (conf['password'], conf['host'], conf['port'])
TEMP_REDIS_URL = 'redis://:%s@%s:%s/4' % (conf['password'], conf['host'], conf['port'])
CACHE_REDIS_URL = 'redis://:%s@%s:%s/5' % (conf['password'], conf['host'], conf['port'])

SEQ_NO_EXPIRE = 60 * 60
COOKIE_EXPIRE = 20 * 60

cache_config = {
    'CACHE_TYPE': 'redis',
    'CACHE_KEY_PREFIX': 'pandora',
    'CACHE_DEFAULT_TIMEOUT': 24*3600,
    'CACHE_REDIS_HOST': conf['host'],
    'CACHE_REDIS_PORT': conf['port'],
    'CACHE_REDIS_URL': CACHE_REDIS_URL
    }


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
       self.__db = redis_cli(REFEREES_REDIS_URL)
       self.key = '%s:%s' % (namespace, name)

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


seq_no_redis_cli = redis_cli(SEQ_NO_REDIS_URL)
cookie_redis_cli = redis_cli(COOKIE_REDIS_URL)
dict_redis_cli = redis_cli(TEMP_REDIS_URL)


def set_cookie(k, v):
    cookie_redis_cli.set(k, v)


def get_cookie(k):

    v = cookie_redis_cli.get(k)
    if v:
        v = v.decode('utf-8')
        logger.info('get cookie from redis: {}'.format(v))
        return v
    else:
        return None


def set_redis_key(k, v):
    dict_redis_cli.set(k, v)


def get_redis_key(k):
    logger.info("get_redid_key key:{}".format(k))
    try:
        v = dict_redis_cli.get(k)
    except Exception as e:
        logger.exception(e)
    logger.info("get_redid_key values:{}".format(v))
    if v:
        v = v.decode('utf-8')
        logger.info('get cookie from redis: {}'.format(v))
        return v
    else:
        return None