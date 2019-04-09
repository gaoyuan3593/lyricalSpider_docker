#! /usr/bin/python3
# -*- coding: utf-8 -*-


from elasticsearch import Elasticsearch

ES_URL = "http://172.19.135.131:9200/"
ES_USER = ""
ES_PWD = ""
ES_PORT = "9200"
ES_HOST = "{}:{}@{}:{}".format(ES_USER, ES_PWD, ES_URL, ES_PORT)

es = Elasticsearch(hosts=ES_URL)
# 创建索引，索引的名字是my-index,如果已经存在了，就返回个400，
# 这个索引可以现在创建，也可以在后面插入数据的时候再临时创建
# 創建映射
mappings = {
    "mappings": {
        "data": {        # "文档类型"
            "properties": {
                "xxx": {     # "索引名"
                    "type": "join",   # "如果想用join功能必须定义类型为join"
                    "relations": {
                        "parent": "child"    # 父类对应子类  attr 是父文档 info子文档(自己指定)
                    }
                }
            }
        }
    }
}
if es.indices.exists("xxx") is not True:
    es.indices.create(index="xxx", body=mappings)

es.delete(index='xxx', doc_type='xxx', id='xxx')

#更新

es.update(index='xxx', doc_type='xxx', id='xxx', body='{待更新字段}')