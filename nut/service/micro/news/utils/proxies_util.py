#! /usr/bin/python3
# -*- coding: utf-8 -*-

import random
from service.utils.yaml_tool import get_by_name_yaml


def get_proxies():
    conf = get_by_name_yaml("proxy")
    proxym_meta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": conf["host"],
        "port": conf["port"],
        "user": conf["user"],
        "pass": conf["password"],
    }

    proxies = random.choice([
        {'http': proxym_meta, 'https': proxym_meta}
    ])
    return proxies
