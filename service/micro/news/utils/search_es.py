#! /usr/bin/python3
# -*- coding: utf-8 -*-
from service import logger
from service.db.utils.elasticsearch_utils import ElasticsearchClient, ALL_NEWS_DETAILS


class SaveDataToEs(object):

    @classmethod
    def create_client(cls):
        return ElasticsearchClient()

    @classmethod
    def filter_keyword(cls, es, _type, _dic):
        mapping = {
            "query": {
                "bool":
                    {
                        "must":
                            [
                                {"term": _dic}
                            ],
                        "must_not": [],
                        "should": []}},
            "from": 0,
            "size": 10,
            "sort": [],
            "aggs": {}
        }
        try:
            result = es.dsl_search(ALL_NEWS_DETAILS, _type, mapping)
            if result.get("hits").get("hits"):
                logger.info("dic : {} is existed".format(_dic))
                return True
            return False
        except Exception as e:
            return False

    @classmethod
    def save_one_data_to_es(cls, data, dic):
        """
        将为爬取的数据存入es中
        :param data_list: 数据
        :return:
        """
        try:
            es = cls.create_client()
            _type = data.get("type")
            if cls.filter_keyword(es, _type, dic):
                logger.info("is existed  dic: {}".format(dic))
                return
            es.insert(ALL_NEWS_DETAILS, _type, data)
            logger.info(" save to es success data= {}！".format(data))
        except Exception as e:
            raise e