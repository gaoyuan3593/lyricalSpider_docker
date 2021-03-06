#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random
import re
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
    from datetime import datetime, timedelta
    try:
        _str = _str.strip()
        if "来自主持人的推荐" in _str:
            _str = datetime.now().strftime("%Y-%m-%d %H:%M")
        elif "秒前" in _str:
            _str = (datetime.now() + timedelta(minutes=-1)).strftime("%Y-%m-%d %H:%M")
        elif "分钟前" in _str:
            fen = int(_str.split("分钟前")[0])
            _str = (datetime.now() + timedelta(minutes=-fen)).strftime("%Y-%m-%d %H:%M")
        elif "今天" in _str:
            today = _str.split("今天")[1]
            _str = (datetime.now()).strftime("%Y-%m-%d ") + today.strip()
        elif "月" in _str:
            if "年" in _str:
                _str = _str.split("年")[0] + "-" + _str.split("年")[1].replace("月", "-").replace("日", "")
            else:
                _str = datetime.now().strftime("%Y-") + _str.replace("月", "-").replace("日", "")
                if len(_str) < 16:
                    _str = datetime.strptime(_str, '%Y-%m-%d %H:%M').strftime("%Y-%m-%d %H:%M")
        elif re.findall(r"\d+-\d+-\d+ \d+:\d+", _str):
            _str = re.findall(r"\d+-\d+-\d+ \d+:\d+", _str)[0]
        else:
            _str = datetime.now().strftime("%Y-%m-%d %H:%M")
        return datetime.strptime(_str, "%Y-%m-%d %H:%M")
    except Exception as e:
        return datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")


def people_str_to_format_time(_str):
    try:
        if isinstance(_str, list):
            _str = "".join(_str).strip()
            old_str = _str.split("来源")[0].strip()
            _str = old_str.split("年")[0] + "-" + old_str.split("年")[1].replace("月", "-").replace("日", " ")
            return datetime.strptime(_str, "%Y-%m-%d %H:%M")
    except:
        return datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")


def china_str_to_format_time(_str):
    try:
        if isinstance(_str, list):
            _str = "".join(_str).strip()
            if "年" in _str or "月" in _str:
                _str = _str.split("年")[0] + "-" + _str.split("年")[1].replace("月", "-").replace("日", "")
                return datetime.strptime(_str, "%Y-%m-%d %H:%M")
            elif "发布时间" in _str:
                old_str = re.findall(r"(\d+-\d+-\d+.\d+:\d+)", _str)[0]
                if len(old_str) > 16:
                    old_str = old_str[:-3]
                return datetime.strptime(old_str, "%Y-%m-%d %H:%M")
            elif "时间" in _str:
                old_str = re.findall(r"(\d+-\d+-\d+)", _str)[0]
                if len(old_str) < 16:
                    old_str = old_str + (datetime.now() + timedelta(minutes=--random.uniform(1, 10))).strftime(" %H:%M")
                return datetime.strptime(old_str, "%Y-%m-%d %H:%M")
    except:
        return datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")


def xinhua_str_to_format_time(_str):
    try:
        if isinstance(_str, list):
            _str = "".join(_str).strip()
            if "年" in _str or "月" in _str:
                _new_str = _str.split("年")[0] + "-" + _str.split("年")[1].replace("月", "-").replace("日", "")[:-3]
                return datetime.strptime(_new_str, "%Y-%m-%d %H:%M")
            _str = _str[:-3]
            return datetime.strptime(_str, "%Y-%m-%d %H:%M")
    except:
        return datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")


def china_news_str_to_format_time(_str):
    try:
        if isinstance(_str, list):
            _str = "".join(_str).strip()
            if "年" in _str or "月" in _str:
                _new_str = _str.split("年")[0] + "-" + _str.split("年")[1].replace("月", "-").replace("日", "")[:-3]
                return datetime.strptime(_new_str, "%Y-%m-%d %H:%M")
            if len(_str) > 16:
                _str = _str[:-3]
            else:
                return datetime.strptime(_str, "%Y-%m-%d %H:%M")
            return datetime.strptime(_str, "%Y-%m-%d %H:%M")
        elif isinstance(_str, str):
            new_str = _str.split("年")[0] + "-" + _str.split("年")[1].replace("月", "-").replace("日", "") + \
                      (datetime.now() + timedelta(minutes=-random.uniform(1, 10))).strftime(" %H:%M")
            return datetime.strptime(new_str, "%Y-%m-%d %H:%M")
    except:
        return datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")


def chinadaily_str_to_format_time(_str):
    try:
        if isinstance(_str, list):
            if "月" in "".join(_str) and "日" in "".join(_str):
                _str = "".join(_str).strip()
                year = datetime.now().strftime("%Y")
                time = datetime.now().strftime(" %H:%M")
                _new_str = year + "-" + _str.replace("月", "-").replace("日", "") + time
                return datetime.strptime(_new_str, "%Y-%m-%d %H:%M")
            else:
                _str = _str[-1].strip()
                return datetime.strptime(_str, "%Y-%m-%d %H:%M")

    except:
        return datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")


def sougou_str_to_format_time(_str):
    if not _str:
        return
    from datetime import datetime, timedelta
    try:
        if "分钟前" in _str:
            fen = int(_str.split("分钟前")[0])
            _str = (datetime.now() + timedelta(minutes=-fen)).strftime("%Y-%m-%d %H:%M")
        elif "小时" in _str:
            hours = int(re.findall(r"\d+", _str)[0])
            _str = (datetime.now() + timedelta(hours=-hours)).strftime("%Y-%m-%d %H:%M")
        elif "天" in _str:
            days = int(re.findall(r"\d+", _str)[0])
            _str = (datetime.now() + timedelta(days=-days)).strftime("%Y-%m-%d %H:%M")
        else:
            _str = datetime.now().strftime("%Y-%m-%d %H:%M")
        return _str
    except Exception as e:
        return (datetime.now() + timedelta(minutes=-10)).strftime("%Y-%m-%d %H:%M")


def date_all(begin_date, end_date):
    date_list = []
    begin_date = datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    today_date = datetime.strptime(datetime.today().strftime("%Y-%m-%d"), "%Y-%m-%d")
    end_date = end_date if end_date <= today_date else today_date
    while begin_date <= end_date:
        date_list.append(begin_date)
        begin_date += timedelta(days=1)
    return date_list


def wechat_date_next(params):
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
            url = "https://weixin.sogou.com/weixin?type=2&ie=utf8&query={}&tsn=5&ft={}&et={}&interation=&wxid=&usip=".format(
                q, cu_date, cu_date)
            url_list.append(
                dict(
                    url=url,
                    keyword=q
                ))
    else:
        url = "https://weixin.sogou.com/weixin?type=2&ie=utf8&query={}&tsn=5&ft={}&et={}&interation=&wxid=&usip=".format(
            q, _date, _date)
        url_list.append(
            dict(
                url=url,
                keyword=q
            ))
    return url_list


def weibo_date_next(params):
    start_hours, _str_date = "0", ""
    url_list = []
    q = params.get("q")
    _date = params.get("date")
    if not _date:
        _date = datetime.now().strftime("%Y-%m-%d")
    if ":" in _date:
        start_date, end_date = _date.split(":")
        if start_date.count("-") == 3 or end_date.count("-") == 3:
            url = "https://s.weibo.com/weibo?q={}&typeall=1&suball=1&Refer=g&timescope=custom:{}".format(q,
                                                                                                         _date)
            url_list.append(
                dict(
                    url=url,
                    keyword=q
                ))
            return url_list
        date_list = date_all(start_date, end_date)
        for date in date_list:
            cu_date = "{}-{}-{}".format(date.year,
                                        "0{}".format(date.month) if len(str(date.month)) < 2 else str(date.month),
                                        "0{}".format(date.day) if len(str(date.day)) < 2 else str(date.day))
            if datetime.strptime(start_date, "%Y-%m-%d") < datetime.strptime(end_date, "%Y-%m-%d") or \
                    datetime.strptime(start_date, "%Y-%m-%d") == datetime.strptime(end_date, "%Y-%m-%d"):
                for i in range(1, 24):
                    k = start_hours if i == 1 else str(i - 1)
                    _s_date = (cu_date + "-" + k) + ":" + (cu_date + "-" + str(i))
                    url = "https://s.weibo.com/weibo?q={}&typeall=1&suball=1&Refer=g&timescope=custom:{}". \
                        format(q, _s_date)
                    url_list.append(
                        dict(
                            url=url,
                            keyword=q
                        ))
    else:
        for i in range(1, 24):
            k = start_hours if i == 1 else str(i - 1)
            _s_date = (_date + "-" + k) + ":" + (_date + "-" + str(i))
            url = "https://s.weibo.com/weibo?q={}&typeall=1&suball=1&Refer=g&timescope=custom:{}".format(q,
                                                                                                         _s_date)
            url_list.append(
                dict(
                    url=url,
                    keyword=q
                ))

    return url_list


if __name__ == '__main__':
    data = {"date": "2020-02-13:2020-02-14", "q": "sdafdsafsdaf"}
    a = weibo_date_next(data)
    print(a)
