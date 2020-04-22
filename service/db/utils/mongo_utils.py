#! /usr/bin/python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient
from service.utils.yaml_tool import get_by_name_yaml

conf = get_by_name_yaml('mongodb')

MONGODB_USR = conf["user"]
MONGODB_PWD = conf["password"]
MONGODB_HOST = conf["host"]
MONGODB_PORT = conf["port"]

MONGODB_CLIENT = 'mongodb://{}'.format(MONGODB_HOST)

# 华为云 上配置
#connection = MongoClient(MONGODB_CLIENT, MONGODB_PORT)

connection = MongoClient("127.0.0.1", MONGODB_PORT)

if __name__ == '__main__':
    _c = connection.local
    result = _c.startup_log.find_one({"_id": "db-mongo-6b95c9f98f-6tgs5-1584099366775"})

    print(result)