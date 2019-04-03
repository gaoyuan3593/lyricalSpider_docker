#! /usr/bin/python3
# -*- coding: utf-8 -*-
from service.db.utils.redis_utils import cookie_redis_cli, COOKIE_EXPIRE


def save_cookie_with_seq_no(seq_no, cookie):
    cookie_redis_cli.set(seq_no, cookie, ex=COOKIE_EXPIRE)


def get_cookie_with_seq_no(seq_no):
    v = cookie_redis_cli.get(seq_no)
    if v:
        return v.decode('utf-8')
    else:
        return None


def del_cookie_with_seq_no(seq_no):
    cookie_redis_cli.delete(seq_no)
