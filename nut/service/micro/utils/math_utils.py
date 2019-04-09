#! /usr/bin/python3
# -*- coding: utf-8 -*-

from service import logger


def str_to_int(x):
    try:
        if not x:
            return 0
        else:
            return int(x)
    except Exception as e:
        return 0


def str_to_float(x):
    try:
        if not x:
            return 0.0
        else:
            return float(x)
    except Exception as e:
        return 0.0


def data_to_str_for_print(data):
    data_str = str(data)
    if len(data_str) > 200:
        return '{}......{}'.format(data_str[:150], data_str[-50:])
    else:
        return data_str


def to_json(data, replace_single_quote=True):
    import json
    if data:
        try:
            r_json = json.loads(data.replace("\'", '"'), encoding='utf-8')
            return r_json
        except:
            logger.info("to_json failed with replace: data: {}".format(data_to_str_for_print(data)))

        try:
            r_json = json.loads(data, encoding='utf-8')
            return r_json
        except:
            logger.info("to_json failed without replace: data: {}".format(data_to_str_for_print(data)))

    return data
