#! /usr/bin/python3
# -*- coding: utf-8 -*-

import json
from service.db.utils.es_mappings import *
from service import logger
from service.utils.yaml_tool import get_by_name_yaml
from elasticsearch import Elasticsearch

conf = get_by_name_yaml('elasticsearch')


class ElasticsearchClient():

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
            result = self.es.indices.create(index=index_name, body=_index_mappings, ignore=ignore)
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
            return self.es.index(index_name, doc_type=doc_type, body=body, id=id)
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
BAIDUTIEBA = "baidu_tieba_details"

# 百度热搜
HOT_SEARCH_BAIDU = "hot_search_keyword_baidu"

# 360热搜榜
HOT_SEARCH_360 = "hot_search_keyword_360"

# 微博热搜榜
HOT_SEARCH_WEIBO = "hot_search_keyword_weibo"

# 所有新闻网站
NEWSDETAIL = "news_details"
ALL_NEWS_DETAILS = "all_news_details"

if __name__ == '__main__':
    import json

    es = ElasticsearchClient()
    # from service.db.utils.es_mappings import WEIBO_INDEX
    #
    # _index_mapping = {
    #     "index_type":
    #         {
    #             "properties": WEIBO_INDEX
    #         },
    # }
    # es.create_index("weibo_index", _index_mapping)
    #
    # mapping = {
    #     "query": {
    #         "bool":
    #             {
    #                 "must":
    #                     [{
    #                         "term": {"weibo_id": "HD4WswYEO"}}],
    #                 "must_not": [],
    #                 "should": []}},
    #     "from": 0,
    #     "sort": [],
    #     "aggs": {}
    # }
    # data = {
    #     "weibo_time": "2019-07-12T08:49:00",
    #     "platform": "iPhone客户端",
    #     "contents": "山东大学留学生“学伴”项目惹争议，学校师生：为友好交流",
    #     "weibo_id": "HD5jkgWwB",
    #     "mid": "4393152104038221",
    #     "user_id": "2814131830",
    #     "like_num": 2,
    #     "com_num": 222,
    #     "repost_num": None,
    #     "is_forward": 1,
    #     "is_forward_weibo_id": "HD56lkUy3",
    #     "type": "detail_type",
    #     "key_user_list": [],
    #     "forward_user_url_list": [],
    #     "b_keyword": "山东大学留学生学伴为友好交流",
    #     "topic": [],
    #     "has_href": 0,
    #     "pics": 1,
    #     "videos": 0,
    #     "crawl_time": "2019-07-23T23:07:00",
    # }
    # result = es.dsl_search("weibo_shan_dong_da_xue_xue_ban_1563934000", "detail_type", mapping)
    # if result.get("hits").get("hits"):
    #     es.update("test", "detail_type", result.get("hits").get("hits")[0].get("_id"), data)
    #     logger.info("dic : {}, update success".format(data))
    # es.insert("test", "detail_type", data)
    # result1 = es.dsl_search('weibo_hot_seach_details', "detail_type", map)
    # result = json.loads(result1)
    # print(result)
    aa = es.get("test", "detail_type", "HD7Uclqu61")
    print(aa)
    dada = aa.get("_source")
    dada.update(com_num=1000000)
    bb = es.update("test", "detail_type", "HD7Uclqu6", dada)
