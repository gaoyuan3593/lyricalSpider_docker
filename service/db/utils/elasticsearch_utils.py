#! /usr/bin/python3
# -*- coding: utf-8 -*-

import json
from service.db.utils.es_mappings import *
from service import logger
from service.utils.yaml_tool import get_by_name_yaml
from elasticsearch import Elasticsearch

conf = get_by_name_yaml('elasticsearch')


class ElasticsearchClient(Elasticsearch):
    def __init__(self):
        """
        初始化 Elasticsearch 连接
        """
        es_host = "{}:{}/".format(conf["url"], conf["port"])
        self.es = Elasticsearch(hosts=es_host)

    def create_index(self, index_name, index_mappings, ignore=400):
        """
        创建一个索引
        :param index_name: 索引名称
        :param ignore: 默认返回400
        :return:
        """
        _index_mappings = {
            "mappings": index_mappings

        }
        if self.es.indices.exists(index=index_name) is not True:
            return self.es.indices.create(index=index_name, body=_index_mappings, ignore=ignore)

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

    def update(self, index_name, doc_type, id, body):
        """
        更新指定id数据
        :param index: 索引名称
        :param doc_type: 文本类型
        :param id: 数据id
        :param body: 内容
        :return:
        """
        return self.es.update(index_name, doc_type=doc_type, id=id, body={"doc": body})

    def delete(self, index_name, id):
        """
        删除数据
        :param index_name: 索引名字
        :param id: 数据id
        :return:
        """
        return self.es.delete(index_name, id=id)

    def dsl_search(self, index_name, doc_type, dsl):
        """
        通过dsl 全文检索
        :param index_name: 索引名称
        :param doc_type:  文本类型
        :param dsl: dsl语句
        :return: json
        """
        result = self.es.search(index_name, doc_type=doc_type, body=dsl)
        return result

    def helpers(self, action, data):
        """
        批量插入数据
        :param action: 模型
        :param data: dict
        :return:
        """
        try:
            from elasticsearch import helpers
            logger.info("Begin es to data ！")
            action.update(_source=data)
            helpers.bulk(self.es, action)
        except Exception as e:
            pass


# 微博
WEIBO_HOT_SEACH = "weibo_hot_seach"
WEIBO_KEYWORD_DETAIL = "weibo_keyword_details"

# 搜狗微信
SOUGOU_KEYWORD_DETAIL = "sougou_keyword_details"

# 百家号
BSIJISHSO_KRYWORD_DETAIL = "baijiahao_keyword_details"

# 百度贴吧
BAIDUTIEBA = "baidu_tieba_details"

# 所有新闻网站
NEWSDETAIL = "news_details"

if __name__ == '__main__':
    import json

    es = ElasticsearchClient()
    es.create_index("weibo_angelababy_zen_me le_156334272")

    map = {
        "query": {
            "bool":
                {
                    "must":
                        [{
                            "term": {"b_keyword.keyword": "五花八门的过敏反应"}}],
                    "must_not": [],
                    "should": []}},
        "sort": [],
        "aggs": {}
    }

    result1 = es.dsl_search('weibo_hot_seach_details', "detail_type", map)
    result = json.loads(result1)
    print(result)
