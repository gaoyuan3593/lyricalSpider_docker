#! /usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import json


def dict_to_cookie_jar(dic):
    n = requests.cookies.cookiejar_from_dict(json.loads(dic))
    return n


def cookie_jar_to_dict(cookie_jar):
    m = requests.utils.dict_from_cookiejar(cookie_jar)
    return m
