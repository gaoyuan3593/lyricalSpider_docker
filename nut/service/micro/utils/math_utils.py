#! /usr/bin/python3
# -*- coding: utf-8 -*-

from service import logger
from datetime import datetime, timedelta


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
        elif "年" in _str:
            _str = (_str.split("年")[0].split("-")[1] + "-" + _str.split("年")[1]).strip("\'")
            if "年" in _str:
                _str = (_str.split("年")[0].split("-")[1] + _str.split("年")[1]).strip("\'")
        return _str
    except Exception as e:
        return _str


def date_all(begin_date, end_date):
    date_list = []
    begin_date = datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    while begin_date <= end_date:
        date_list.append(begin_date)
        begin_date += timedelta(days=1)
    return date_list


def date_next(params):
    start_hours = "0"
    url_list = []
    q = params.get("q")
    _date = params.get("date")
    if not _date:
        _date = datetime.now().strftime("%Y-%m-%d")
    if ":" in _date:
        start_date, end_date = _date.split(":")
        date_list = date_all(start_date, end_date)
        s_y, s_m, s_d = start_date.split('-')
        for date in date_list:
            cu_date = "{}-{}-{}".format(s_y, s_m, str(date.day))
            if datetime.strptime(start_date, "%Y-%m-%d") < datetime.strptime(end_date, "%Y-%m-%d"):
                for i in range(1, 24):
                    k = start_hours if i == 1 else str(i - 1)
                    _s_date = (cu_date + "-" + k) + ":" + (cu_date + "-" + str(i))
                    url = "https://s.weibo.com/weibo?q={}&typeall=1&suball=1&Refer=g&timescope=custom:{}".format(q,
                                                                                                                 _s_date)
                    url_list.append(url)
    else:
        for i in range(1, 24):
            k = start_hours if i == 1 else str(i - 1)
            _s_date = (_date + "-" + k) + ":" + (_date + "-" + str(i))
            url = "https://s.weibo.com/weibo?q={}&typeall=1&suball=1&Refer=g&timescope=custom:{}".format(q,
                                                                                                         _s_date)
            url_list.append(url)

    return url_list


if __name__ == '__main__':
    a = '2019-2018年04-28 11:48'
    b = str_to_format_time(a )
    print(b)