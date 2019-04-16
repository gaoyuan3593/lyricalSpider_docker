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


def str_to_format_time(_str):
    if not _str:
        return
    from datetime import datetime, timedelta
    try:
        if "秒前" in _str:
            _str = (datetime.now() + timedelta(minutes=-1)).strftime("%Y-%m-%d %H:%M")
        elif "分钟前" in _str:
            fen = int(_str.split("分钟前")[0])
            _str = (datetime.now() + timedelta(minutes=-fen)).strftime("%Y-%m-%d %H:%M")
        elif "今天" in _str:
            today = _str.split("今天")[1]
            _str = (datetime.now()).strftime("%Y-%m-%d ") + today
        elif "月" in _str:
            _str = datetime.now().strftime("%Y-") + _str.replace("月", "-").replace("日", "")
            if len(_str) < 16:
                _str = datetime.strptime(_str, '%Y-%m-%d %H:%M').strftime("%Y-%m-%d %H:%M")
        return _str
    except Exception as e:
        return _str
