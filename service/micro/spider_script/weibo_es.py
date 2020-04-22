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
        return False


def save_data_to_es(index, data, ):

    for dic in data:
        resp = dict(
            time=dic.get("time"),
            platform=dic.get("platform"),
            contents=dic.get("contents"),
            id=dic.get("id"),
            mid=dic.get("mid"),
            user_id=dic.get("user_id"),
            like=dic.get("like"),
            comment_num=dic.get("comment_num"),
            repost_num=dic.get("repost_num"),
            is_forward=dic.get("is_forward"),
            forward_weibo_id=dic.get("forward_weibo_id"),
            type=dic.get("type"),
            key_user_id_list=dic.get("key_user_id_list"),
            forward_user_id_list=dic.get("forward_user_id_list"),
            b_keyword=dic.get("b_keyword"),
            topic_list=dic.get("topic_list"),
            is_has_href=dic.get("is_has_href"),
            is_pics=dic.get("is_pics"),
            is_videos=dic.get("is_videos"),
            crawl_time=dic.get("crawl_time"),
        )
        if filter_keyword(index, dic.get("id"), dic.get("type")):
            continue
        es_client.insert(index, dic.get("type"), resp, dic.get("id"))
        logger.info("Weibo Data save success time: {}, data: {}".format(resp.get("time"), resp))


if __name__ == '__main__':
    from service.micro.spider_script._inmero import weibo_list

    # for dic in weibo_list:
    #     index = dic.get("weibo_index")
    _type = "comment_type"
    final_results = search("weibo_xiang_gang_ge_jie_dui_jing_ji_biao_shi_dan_you_1565857466", _type)
    #new_index = "_".join(index.split("_")[:-1])
    save_data_to_es("weibo_hot_search_detail", final_results)
