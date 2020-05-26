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


comment_type = ['time', 'platform', 'contents', "id", "user_id", "user_name", "weibo_id", "like"]


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






if __name__ == '__main__':

    _type = "comment_type"
    file_name = "fangfang"
    final_results = search("weibo_fang_fang_ri_ji_1586399369", _type)
    save_data_to_excel(file_name, final_results, _type)
