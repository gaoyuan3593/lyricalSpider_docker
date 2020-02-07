#! /usr/bin/python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient
from service.utils.yaml_tool import get_by_name_yaml

conf = get_by_name_yaml('mongodb')

MONGODB_USR = conf["user"]
MONGODB_PWD = conf["password"]
MONGODB_HOST = conf["host"]
MONGODB_PORT = conf["port"]
MONGODB_CLIENT = 'mongodb://%s:%s@%s' % (MONGODB_USR, MONGODB_PWD, MONGODB_HOST)


connection = MongoClient("127.0.0.1", MONGODB_PORT)
