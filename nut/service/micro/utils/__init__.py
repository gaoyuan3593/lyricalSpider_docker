#! /usr/bin/python3
# -*- coding: utf-8 -*-

import random

USER_AGENTS = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:49.0) Gecko/20100101 Firefox/49.0',
    'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Mobile Safari/537.36'
]


def ua():
    return random.choice(USER_AGENTS)
