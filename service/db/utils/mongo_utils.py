#! /usr/bin/python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient

MONGODB_USR = ''
MONGODB_PWD = ''
MONGODB_HOST = 'mongodb://%s:%s@nut_mongo_host' % (MONGODB_USR, MONGODB_PWD)
MONGODB_PORT = 27017

connection = MongoClient("127.0.0.1", MONGODB_PORT)
