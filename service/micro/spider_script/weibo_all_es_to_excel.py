#! /usr/bin/python3
# -*- coding: utf-8 -*-
from datetime import datetime
import json
import pandas as pd
from elasticsearch import helpers
from elasticsearch import Elasticsearch

from service import logger
from service.db.utils.elasticsearch_utils import es_client

es = Elasticsearch(hosts="http://172.19.135.135:9200")

detail_type = ['time', 'platform', 'contents', "id", "mid"", user_id", "like", "comment_num", "repost_num",
               "is_forward",
               "forward_weibo_id", "key_user_id_list", "forward_user_id_list", "topic_list", "is_has_href", "is_pics",
               "is_videos"]
comment_type = ['time', 'platform', 'contents', "id", "user_id", "user_name", "weibo_id", "like"]
repost_type = ['time', 'platform', 'contents', "user_id", "user_name", "weibo_id", "like"]
user_type = ['user_id', 'fan_count', 'follow_count', "profile_image_url", "user_name", "verified", "verified_reason",
              "weibo_count",
             "city", "gender", "introduction", "grade", "registration", "birthday"]


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


def save_data_to_excel(file_name, data, _type):
    _list = []
    if _type == "comment_type":
        for data_dic in data:
            _list.append([
                data_dic.get("time", None),
                data_dic.get("platform", None),
                data_dic.get("contents", None),
                data_dic.get("id", None),
                data_dic.get("user_id", None),
                data_dic.get("user_name", None),
                data_dic.get("weibo_id", None),
                data_dic.get("like", None),
            ])

        df = pd.DataFrame(_list, columns=comment_type)
        # df.drop_duplicates(subset=["id"], keep='first', inplace=True)
        # df2 = df.sort_values(by="date", ascending=False)
        df.to_excel(r"C:\Users\dell\Desktop\{}.xlsx".format(file_name), encoding="utf-8", index=False)
        print("保存成功...")

    if _type == "repost_type":
        for data_dic in data:
            _list.append([
                data_dic.get("time", None),
                data_dic.get("platform", None),
                data_dic.get("contents", None),
                data_dic.get("user_id", None),
                data_dic.get("user_name", None),
                data_dic.get("weibo_id", None),
                data_dic.get("like", None),
                data_dic.get("key_user_list", None),
            ])

        df = pd.DataFrame(_list, columns=repost_type)
        # df.drop_duplicates(subset=["id"], keep='first', inplace=True)
        # df2 = df.sort_values(by="date", ascending=False)
        df.to_excel(r"C:\Users\dell\Desktop\{}.xlsx".format(file_name), encoding="utf-8", index=False)
        print("保存成功...")
    elif _type == "detail_type":
        for data_dic in data:
            _list.append([
                data_dic.get("time", None),
                data_dic.get("platform", None),
                data_dic.get("contents", None),
                data_dic.get("id", None),
                data_dic.get("user_id", None),
                data_dic.get("like", None),
                data_dic.get("comment_num", None),
                data_dic.get("repost_num", None),
                data_dic.get("is_forward", None),
                data_dic.get("forward_weibo_id", None),
                data_dic.get("key_user_id_list", None),
                data_dic.get("forward_user_id_list", None),
                data_dic.get("topic_list", None),
                data_dic.get("is_has_href", None),
                data_dic.get("is_pics", None),
                data_dic.get("videos", None),
            ])

        df = pd.DataFrame(_list, columns=detail_type)
        # df.drop_duplicates(subset=["id"], keep='first', inplace=True)
        # df2 = df.sort_values(by="date", ascending=False)
        df.to_excel(r"C:\Users\dell\Desktop\{}.xlsx".format(file_name), encoding="utf-8", index=False)
        print("保存成功...")

    if _type == "user_type":
        for data_dic in data:
            _list.append([
                data_dic.get("user_id", None),
                data_dic.get("fan_count", None),
                data_dic.get("follow_count", None),
                data_dic.get("profile_image_url", None),
                data_dic.get("user_name", None),
                data_dic.get("verified", None),
                data_dic.get("verified_reason", None),
                data_dic.get("weibo_count", None),
                data_dic.get("city", None),
                data_dic.get("gender", None),
                data_dic.get("introduction", None),
                data_dic.get("grade", None),
                data_dic.get("registration", None),
                data_dic.get("birthday", None),
            ])
        # ['user_id', 'fan_count', 'follow_count', "profile_image_url", "user_name", "verified", "verified_reason",
        #  "tags", "weibo_count",
        #  "city", "gender", "introduction", "grade", "registration", "birthday"]
        df = pd.DataFrame(_list, columns=user_type)
        # df.drop_duplicates(subset=["id"], keep='first', inplace=True)
        # df2 = df.sort_values(by="date", ascending=False)
        df.to_excel(r"C:\Users\dell\Desktop\{}.xlsx".format(file_name), encoding="utf-8", index=False)
        print("保存成功...")


if __name__ == '__main__':
    _type = "detail_type"
    file_name = "chongwu_user"
    final_results = search("weibo_xin_guan_feiyan", _type)
    save_data_to_excel(file_name, final_results, _type)
