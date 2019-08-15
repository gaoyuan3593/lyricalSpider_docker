#! /usr/bin/python3
# -*- coding: utf-8 -*-

import random

from service.core.utils.proxy import get_proxy_pool
from service import logger


def get_proxies():
    proxy_pool = get_proxy_pool()
    if not proxy_pool or len(proxy_pool) == 0:
        return None
    proxy = random.choice(proxy_pool)
    logger.info("proxy : {}".format(proxy))
    http_proxy = "http://" + proxy
    https_proxy = "https://" + proxy
    proxym_meta = {'http': http_proxy, 'https': https_proxy}
    return proxym_meta
