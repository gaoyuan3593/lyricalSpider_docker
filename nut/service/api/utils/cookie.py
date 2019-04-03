#! /usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import requests


def cookiejar_to_dict(cookie_jar):
    m = requests.utils.dict_from_cookiejar(cookie_jar)
    return m


def dict_to_cookiejar(dic):
    n = requests.cookies.cookiejar_from_dict(dic)
    return n
