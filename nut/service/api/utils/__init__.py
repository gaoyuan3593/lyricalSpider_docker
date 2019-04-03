#! /usr/bin/python3
# -*- coding: utf-8 -*-
from flask import jsonify


def resp_ok(dic):
    resp = jsonify(dic)
    resp.status_code = 200
    return resp


def resp_404():
    resp = jsonify(dict(err_code=404,
                        err_msg='请求URL不正确'))
    resp.status_code = 200
    return resp
