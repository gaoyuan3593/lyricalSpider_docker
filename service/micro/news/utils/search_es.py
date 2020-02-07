#! /usr/bin/python3
# -*- coding: utf-8 -*-
from service import logger
from service.db.utils.elasticsearch_utils import es_client


class SaveDataToEs(object):

    @classmethod
    def create_client(cls):
        return es_client

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

    @classmethod
    def create_index(cls, index_name, index_mappings):
        es = cls.create_client()
        return es.create_index(index_name, index_mappings)