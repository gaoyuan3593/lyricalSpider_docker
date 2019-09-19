#! /usr/bin/python3
# -*- coding: utf-8 -*-
import pypinyin
import time
from service.micro.utils.customerized_data_type import enum

ES_INDEX = (
    "weibo_",  # 微博
    "wechat_",  # 微信
    "tieba_",  # 贴吧
    "baijiahao_",  # 百家号
    "website_",  # 新闻网站
    "app_",  # app
    "douyin_",  # 抖音
)

OPERATION = enum(
    CREATE='CREATE',  # 创建
    UPDATE='UPDATE',  # 修改
    DELETE='DELETE',  # 删除
    PAUSE='PAUSE',  # 暂停
    RESUME='RESUME'  # 恢复
)


def hp(title, text, flag):
    s = ""
    if "," in text:
        text = text.replace(",", "")
    if " " in text:
        text = text.replace(" ", "")
    text = text.strip()
    _str = str(int(time.time()))
    for i in pypinyin.pinyin(text, style=pypinyin.NORMAL):
        s += "{}{}".format(''.join(i), "_")
    if not flag:
        return "{}{}{}".format(title, s, _str)
    else:
        return "{}{}".format(title, s).strip("_")


def hp_account(title, text, user_id):
    s = ""
    text = text.strip()
    for i in pypinyin.pinyin(text, style=pypinyin.NORMAL):
        s += "{}{}".format(''.join(i), "_")
    return "{}{}{}".format(title, s, user_id)


if __name__ == '__main__':
    keyword = "Angelababy,经纪人,"
    print(hp("weibo_", "京都,火灾"))
    print(hp("weibo_", "经纪人 阿斯蒂芬"))
    if "aa" not in OPERATION:
        print(111)
