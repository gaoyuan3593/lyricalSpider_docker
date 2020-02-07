from service.utils.yaml_tool import get_by_name_yaml

REDIS = get_by_name_yaml('redis')
__author__ = 'gao yuan'


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


WERBO_HOST = 'redis://:{0}@{1}:{2}'.format(REDIS['password'], REDIS['host'], REDIS['port'])
EVENT_HOST = 'redis://:{0}@{1}:{2}'.format(REDIS['password'], REDIS['host'], REDIS['port'])
KUAI_PROXY_HOST = 'redis://:{0}@{1}:{2}'.format(REDIS['password'], REDIS['host'], REDIS['port'])

# 微博评论，转发
WEIBO_PAGE_REDIS_URL = '{}/1'.format(WERBO_HOST)

# 事件任务
EVENT_REDIS_URL = '{}/2'.format(EVENT_HOST)

# 快代理
KUAI_PROXY_REDIS_URL = '{}/3'.format(KUAI_PROXY_HOST)

# ai评论员
AI_COMMENT_REDIS_URL = '{}/4'.format(KUAI_PROXY_HOST)

weibo_redis_cli = redis_cli(WEIBO_PAGE_REDIS_URL)
event_redis_cli = redis_cli(EVENT_REDIS_URL)
kuai_proxy_redis_cli = redis_cli(KUAI_PROXY_REDIS_URL)
ai_comment_redis_cli = redis_cli(AI_COMMENT_REDIS_URL)

if __name__ == '__main__':
    import redis
    import time
    import json
    import re

    key = "dsafjkasdkfhjsdf"
    value = [
        "129.28.54.14:16819,38649",
        "47.99.200.82:16819,39018",
        "114.215.127.162:16819,40234"
    ]
    conn = redis.StrictRedis(host=REDIS['host'], port=REDIS['port'], password=REDIS['password'], db=3,
                             decode_responses=True)
    conn.set(key, json.dumps(value))
    conn.expire(key, 10)
    # 设置键的过期时间为10s
    for item in range(12):
        value = conn.get(key)
        if value != None:
            print(value)
        else:
            print('the key has been deleted...')
            break
        time.sleep(1)
