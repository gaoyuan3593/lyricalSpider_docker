#! /usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime
from functools import reduce
data_list = [
{'date': '2018-05-03T03:09:59Z', 'description': "Chinese and American officials will be trying to defuse tensions pushing the world's two largest economies toward trade war in meetings in Beijing beginning Thursday.", 'image': None, 'taxonomy': [{'path': 'fox-news/us/economy', 'url': 'foxnews.com/category/us/economy', 'adTag': 'economy'}], 'title': 'Chip Wars: Tech rivalry underlines US-China trade conflict', 'type': 'article', 'url': ['https://www.foxnews.com/us/chip-wars-tech-rivalry-underlines-us-china-trade-conflict', 'https://www.foxnews.com/us/2018/05/02/chip-wars-tech-rivalry-underlines-us-china-trade-conflict.html']},
{'date': '2018-05-03T03:09:59Z', 'description': "Chinese and American officials will be trying to defuse tensions pushing the world's two largest economies toward trade war in meetings in Beijing beginning Thursday.", 'image': None, 'taxonomy': [{'path': 'fox-news/us/economy', 'url': 'foxnews.com/category/us/economy', 'adTag': 'economy'}], 'title': 'Chip Wars: Tech rivalry underlines US-China trade conflict', 'type': 'article', 'url': ['https://www.foxnews.com/us/chip-wars-tech-rivalry-underlines-us-china-trade-conflict', 'https://www.foxnews.com/us/2018/05/02/chip-wars-tech-rivalry-underlines-us-china-trade-conflict.html']},
{'date': '2018-07-02T16:17:00Z', 'description': 'Fox News contributor says President Trump is taking a huge risk with trade.', 'image': [{'url': 'http://media2.foxnews.com/BrightCove/694940094001/2018/07/02/694940094001_5804484289001_5804508570001-vs.jpg', 'credit': None, 'caption': None}], 'taxonomy': [{'path': 'fox-news/shows/your-world/transcript/interviews', 'url': 'foxnews.com/category/shows/your-world/transcript/interviews', 'adTag': 'interviews'}, {'path': 'fox-news/shows', 'url': 'foxnews.com/category/shows', 'adTag': 'shows'}], 'title': "Ari Fleischer: Trump wanted a trade war, he's getting one", 'type': 'article', 'url': ['https://www.foxnews.com/transcript/ari-fleischer-trump-wanted-a-trade-war-hes-getting-one', 'https://www.foxnews.com/transcript/2018/07/02/ari-fleischer-trump-wanted-trade-war-hes-getting-one.html']},
{'date': '2018-07-02T16:17:00Z', 'description': 'Fox News contributor says President Trump is taking a huge risk with trade.', 'image': None, 'title': "Ari Fleischer: Trump wanted a trade war, he's getting one", 'type': 'article', 'url': ['https://www.foxnews.com/transcript/ari-fleischer-trump-wanted-a-trade-war-hes-getting-one', 'https://www.foxnews.com/transcript/2018/07/02/ari-fleischer-trump-wanted-trade-war-hes-getting-one.html']}
]


def list_dict_duplicate_removal(data_list):
    run_function = lambda x, y: x if y in x else x + [y]
    return reduce(run_function, [[], ] + data_list)


# a = list_dict_duplicate_removal(data_list)
# print(a)
_ = []
_list = []
for data in data_list:
    print(data)
    title = data.get("title")
    if title in _list:
        continue
    _list.append(title)
    _.append(data)
print(_)
print(_list)