#! /usr/bin/python3
# -*- coding: utf-8 -*-

import json
from service import logger
from service.utils.yaml_tool import get_by_name_yaml
from elasticsearch import Elasticsearch

conf = get_by_name_yaml('elasticsearch')


class ElasticsearchClient(object):
    def __init__(self):
        """
        初始化 Elasticsearch 连接
        """
        es_host = "{}:{}/".format(conf["url"], conf["port"])
        self.es = Elasticsearch(hosts=es_host)

    def create_index(self, index_name, ignore=400):
        """
        创建一个索引
        :param index_name: 索引名称
        :param ignore: 默认返回400
        :return:
        """
        return self.es.indices.create(index_name, ignore=ignore)

    def delete_index(self, index_name, ignore=[400, 404]):
        """
        删除一个索引
        :param index_name: 索引名称
        :param ignore: 默认400,404 忽略 Index 不存在而删除失败导致程序中断的问题
        :return:
        """
        return self.es.indices.delete(index_name, ignore=ignore)

    def insert(self, index_name, doc_type, body):
        """
        插入数据
        :param index: 索引名称
        :param doc_type: 文本类型
        :param body: 内容
        :return:
        """
        return self.es.index(index_name, doc_type=doc_type, body=body)

    def create(self, index_name, doc_type, id, body):
        """
        插入指定id数据
        :param index: 索引名称
        :param doc_type: 文本类型
        :param id: 数据id
        :param body: 内容
        :return:
        """
        return self.es.create(index_name, doc_type=doc_type, id=id, body=body)

    def update(self, index_name, doc_type, id, body):
        """
        更新指定id数据
        :param index: 索引名称
        :param doc_type: 文本类型
        :param id: 数据id
        :param body: 内容
        :return:
        """
        return self.es.update(index_name, doc_type=doc_type, id=id, body=body)

    def delete(self, index_name, id):
        """
        删除数据
        :param index_name: 索引名字
        :param id: 数据id
        :return:
        """
        return self.es.delete(index_name, id=id)

    def search(self, index_name, doc_type):
        """
        查询所有数据
        :param index_name: 索引名称
        :param doc_type: 文本类型
        :return: 当前索引所有数据
        """
        result = self.es.search(index_name, doc_type=doc_type)
        return json.dumps(result, aensure_ascii=False)

    def dsl_search(self, index_name, doc_type, dsl):
        """
        通过dsl 全文检索
        :param index_name: 索引名称
        :param doc_type:  文本类型
        :param dsl: dsl语句
        :return: json
        """
        result = self.es.search(index_name, doc_type=doc_type, body=dsl)
        return json.dumps(result, aensure_ascii=False)

    def helpers(self, action, data):
        try:
            from elasticsearch import helpers
            logger.info("Begin es to data ！")
            action.update(_source=data)
            helpers.bulk(self.es, action)
        except Exception as e:
            pass


if __name__ == '__main__':
    es = ElasticsearchClient()
    result = es.create_index('news')
    print(result)
    # result = es.delete_index('news')
    # print(result)
    # data = {'title': '美国留给伊拉克的是个烂摊子吗', 'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm'}
    # result = es.create('news', 'politics', id=1, body=data)
    # print(result)
