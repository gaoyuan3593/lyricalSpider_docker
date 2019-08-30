#! /usr/bin/python3
# -*- coding: utf-8 -*-
from service import logger
from service.db.utils.elasticsearch_utils import ElasticsearchClient, ALL_NEWS_DETAILS


class SaveDataToEs(object):

    @classmethod
    def create_client(cls):
        return ElasticsearchClient()

    @classmethod
    def filter_keyword(cls, es, index, _type, id):

        try:
            result = es.get(index, _type, id)
            if result.get("found"):
                return True
            return False
        except Exception as e:
            logger.exception(e)
            raise e

    @classmethod
    def save_one_data_to_es(cls, index, data, id):
        """
        将为爬取的数据存入es中
        :param data_list: 数据
        :return:
        """
        try:
            es = cls.create_client()
            _type = data.get("type")
            if cls.filter_keyword(es, index, _type, id):
                logger.info("is existed  id: {}".format(id))
                return
            es.insert(index, _type, data, id)
            logger.info(" save to es success data= {}！".format(data))
        except Exception as e:
            raise e
