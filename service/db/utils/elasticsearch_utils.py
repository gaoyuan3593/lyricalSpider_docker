#! /usr/bin/python3
# -*- coding: utf-8 -*-


from service.db.utils.es_mappings import *
from service import logger
from service.utils.yaml_tool import get_by_name_yaml
from elasticsearch import Elasticsearch

h_conf = get_by_name_yaml('huaweiyun_elasticsearch')
s_conf = get_by_name_yaml('school_elasticsearch')


class ElasticsearchClient():

    def __init__(self, url, port):
        """
        初始化 Elasticsearch 连接
        """
        # es_host = 'http://{}:{}@{}:{}'.format(conf["user"], conf["password"], conf["host"], conf["port"])
        # es_host = "{}:{}/".format(conf["url"], conf["port"])
        es_host = "{}:{}/".format(url, port)
        self.es = Elasticsearch(hosts=es_host)
        self.h_es = Elasticsearch(hosts=es_host)

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
            result = self.es.indices.create(index=index_name, body=_index_mappings, ignore=ignore)
            h_result = self.h_es.indices.create(index=index_name, body=_index_mappings, ignore=ignore)
            if result.get("acknowledged"):
                return result
            elif result.get("status") == 400:
                return result.get("error")

    def delete_index(self, index_name):
        """
        删除一个索引
        :param index_name: 索引名称
        :param ignore: 默认400,404 忽略 Index 不存在而删除失败导致程序中断的问题
        :return:
        """
        return self.es.indices.delete(index_name)

    def insert(self, index_name, doc_type, body, id=None):
        """
        插入数据
        :param index: 索引名称
        :param doc_type: 文本类型
        :param body: 内容
        :return:
        """
        if id:
            self.es.index(index_name, doc_type=doc_type, body=body, id=id)
            self.h_es.index(index_name, doc_type=doc_type, body=body, id=id)
        else:
            return self.es.index(index_name, doc_type=doc_type, body=body)

    def get(self, index_name, doc_type, id, ignore=[400, 404]):
        """
        查询数据
        :param index: 索引名称
        :param doc_type: 文本类型
        :param id: id
        :return:
        """

        return self.es.get(index_name, doc_type=doc_type, id=id, ignore=ignore)

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


# 微博热搜
WEIBO_HOT_SEARCH = "weibo_hot_search_detail"

# 搜狗微信
SOUGOU_KEYWORD_DETAIL = "sougou_keyword_details"

# 百家号
BSIJISHSO_KRYWORD_DETAIL = "baijiahao_keyword_details"

# 百度贴吧
# 原贴吧index
# BAIDUTIEBA = "baidu_tieba_details"
BAIDUTIEBA = "new_baidu_tieba_details"

# 今日头条热搜榜
HOT_SEARCH_TOUTIAO = "hot_search_keyword_toutiao"

# 百度热搜
HOT_SEARCH_BAIDU = "hot_search_keyword_baidu"

# 360热搜榜
HOT_SEARCH_360 = "hot_search_keyword_360"

# 微博热搜榜
HOT_SEARCH_WEIBO = "hot_search_keyword_weibo"

# 所有新闻网站
ALL_NEWS_DETAILS = "all_news_details"

# 监控报纸
ALL_PAPER_DETAILS = "all_paper_details"

# es连接
es_client = ElasticsearchClient(s_conf["url"], s_conf["port"])
h_es_client = ElasticsearchClient(h_conf["url"], h_conf["port"])
