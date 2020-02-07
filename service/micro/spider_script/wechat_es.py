#! /usr/bin/python3
# -*- coding: utf-8 -*-
from datetime import datetime
import json

from elasticsearch import helpers
from elasticsearch import Elasticsearch

from service import logger
from service.db.utils.elasticsearch_utils import es_client


es = Elasticsearch(hosts="http://172.19.135.135:9200")


def search(index, doc_type):
    es_search_options = set_search_optional()
    es_result = get_search_result(es_search_options, index=index, doc_type=doc_type)
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
            pass


def save_data_to_es(index, data):
    for dic in data:
        resp = dict(
            title=dic.get("title"),
            author=dic.get("author"),
            time=dic.get("article_date"),
            contents=dic.get("article_text"),
            id=dic.get("article_id"),
            type=dic.get("type"),
            is_pics=dic.get("pics"),
            img_url_list=dic.get("img_url"),
            wechat_num=dic.get("wechat_num"),
            profile_meta=dic.get("profile_meta"),
            is_share=dic.get("is_share"),
            link=dic.get("article_url"),
            crawl_time=dic.get("crawl_time"),
        )
        if filter_keyword(index, dic.get("article_id"), dic.get("type")):
            return
        es_client.insert(index, dic.get("type"), resp, dic.get("article_id"))
        logger.info("Weibo Data save success id: {}..........".format(resp))


if __name__ == '__main__':
    from service.micro.spider_script._inmero import wechat_list

    for dic in wechat_list:
        index = dic.get("wechat_index")
        _type = "detail_type"
        final_results = search(index, _type)
        new_index = "_".join(index.split("_")[:-1])
        save_data_to_es(new_index, final_results)
