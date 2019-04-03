#! /usr/bin/python3
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch


MONGODB_USR = ''
MONGODB_PWD = ''
MONGODB_HOST = 'mongodb://%s:%s@pandora_mongo_host' % (MONGODB_USR, MONGODB_PWD)
MONGODB_PORT = 27017

es = Elasticsearch(
        ['xxx.xxx.xxx.xxx'],
        http_auth=('user', 'pwd'),
        port=MONGODB_PORT)

