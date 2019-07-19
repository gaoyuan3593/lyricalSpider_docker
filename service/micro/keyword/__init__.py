#! /usr/bin/python3
# -*- coding: utf-8 -*-
import pypinyin
import time

ES_INDEX = (
    "weibo_",
    "wechat_",
    "tieba_",
    "baijiahao_"
)


def hp(title, text):
    s = ""
    if "," in text:
        text = text.replace(",", "")
    if " " in text:
        text = text.replace(" ", "")
    text = text.strip()
    _str = str(int(time.time()))
    for i in pypinyin.pinyin(text, style=pypinyin.NORMAL):
        s += "{}{}".format(''.join(i), "_")
    return "{}{}{}".format(title, s, _str)


if __name__ == '__main__':
    keyword = "Angelababy,经纪人,"
    print(hp("weibo_", "京都,火灾"))
    print(hp("weibo_", "经纪人 阿斯蒂芬"))