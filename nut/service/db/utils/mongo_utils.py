#! /usr/bin/python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient

MONGODB_USR = 'mongo'
MONGODB_PWD = 'pand0ra2o17!'
MONGODB_HOST = 'mongodb://%s:%s@pandora_mongo_host' % (MONGODB_USR, MONGODB_PWD)
MONGODB_PORT = 27017

connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
