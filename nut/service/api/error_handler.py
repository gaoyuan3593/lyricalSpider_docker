#! /usr/bin/python3
# -*- coding: utf-8 -*-
from flask import jsonify

from service.exception import GenericAppError
from service.server.main import application as app


@app.errorhandler(GenericAppError)
def generic_error(error):
    message = {
        'err_code': error.code,
        'err_msg': error.message
    }
    if hasattr(error, 'data'):
        message.update(data=error.data)

    resp = jsonify(message)
    resp.status_code = error.status_code
    h = resp.headers
    h['Access-Control-Allow-Origin'] = '*'
    h['Access-Control-Allow-Methods'] = 'POST', 'GET'
    return resp
