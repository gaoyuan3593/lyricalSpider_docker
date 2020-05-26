#! /usr/bin/python3
# -*- coding: utf-8 -*-
from datetime import datetime
import json

import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from elasticsearch import helpers
from elasticsearch import Elasticsearch

from service import logger
from service.db.utils.elasticsearch_utils import es_client

es = Elasticsearch(hosts="http://172.19.135.135:9200")


def search(index):
    es_search_options = set_search_optional()
    es_result = get_search_result(es_search_options, index=index)
    final_result = get_result_list(es_result)
    return final_result


def get_result_list(es_result):
    final_result = []
    for item in es_result:
        final_result.append(item['_source'])
    return final_result


def get_search_result(es_search_options, scroll='6m', index=None, doc_type=None, timeout="2m"):
    es_result = helpers.scan(
        client=es,
        query=es_search_options,
        scroll=scroll,
        index=index,
        doc_type=doc_type,
        timeout=timeout
    )
    return es_result


def set_search_optional():
    # 检索选项
    es_search_options = {
        "query": {
            "match_all": {}
        }
    }
    return es_search_options


def filter_keyword(index, id, _type):
    try:
        result = es_client.get(index, _type, id)
        if result.get("found"):
            return True
        return False
    except Exception as e:
        logger.exception(e)
        return False


def save_data_to_es(index, data):
    for dic in data:
        title = dic.get("title")
        time = dic.get("time")
        if not time or not title:
            continue
        resp = dict(
            title=dic.get("title"),
            author=dic.get("author"),
            introduction=dic.get("introduction"),
            time=dic.get("time"),
            avatar_img=dic.get("avatar_img"),
            b_keyword=dic.get("b_keyword"),
            contents=dic.get("article_text"),
            id=dic.get("article_id"),
            type=dic.get("type"),
            is_pics=dic.get("pics"),
            user_id=dic.get("user_id"),
            img_url_list=dic.get("img_url"),
            link=dic.get("user_id"),
            crawl_time=dic.get("acticle_url"),
        )
        if filter_keyword(index, dic.get("article_id"), dic.get("type")):
            continue
        es_client.insert(index, dic.get("type"), resp, dic.get("article_id"))
        logger.info("Weibo Data save success data: {}".format(resp))


if __name__ == '__main__':
    final_results = search("baijiahao_keyword_details")
    save_data_to_es("test_baijiahao", final_results, )
