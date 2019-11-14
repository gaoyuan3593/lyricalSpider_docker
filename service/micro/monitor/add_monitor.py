#! /usr/bin/python3
# -*- coding: utf-8 -*-
import json
import multiprocessing
from service import logger
from service.db.utils.elasticsearch_utils import ElasticsearchClient
from service.micro.utils.apscheduler_ import TaskApscheduler
from service.utils.seq_no import generate_seq_no
from service.micro.keyword.utils.utils import remove_job, resume_job, pause_job
from service.micro.keyword import OPERATION
from service.db.utils.redis_utils import RedisQueue


class AddMonitorAccount(object):
    __name__ = "add monitor account"

    def __init__(self, data):
        self.data = data
        self.seq_no = generate_seq_no()
        self.operation = self.data.get("operation")
        self.task_id = self.data.get("task_id")
        self.account = self.data.get("account")
        self.index_name = self.data.get("index_name")
        self.domain = self.data.get("website")
        self.app_name = self.data.get("app")
        self.douyin_name = self.data.get("douyin")
        self.weibo_user_id = self.data.get("weibo_user_id")
        self.now_data = dict(weibo_user_id=self.weibo_user_id)

    def query(self):
        logger.info("Begin add monitor account query run ...")
        data_dic = dict(
            status=200,
            task_id=self.seq_no,
            result=[],
            message="success",
        )
        if self.operation == OPERATION.CREATE:
            task = TaskApscheduler(self.get_monitor_result, job_id=self.seq_no)
            index_list = self.retrun_index_name()
            self.add_parameter(index_list)
            result = [
                index.get("weibo_index") or index.get("website_index") or index.get("wechat_index") for index in
                index_list]
            task.add_job()
            data_dic.update(
                task_id=self.seq_no,
                result=result
            )
            # self.save_data_to_redis(self.seq_no, index_list)
            return data_dic
        elif self.operation == OPERATION.DELETE:
            remove_job(self.task_id)
            data_dic.update(
                task_id=self.task_id,
            )
        elif self.operation == OPERATION.RESUME:
            resume_job(self.task_id)
            data_dic.update(
                task_id=self.task_id,
            )
        elif self.operation == OPERATION.PAUSE:
            pause_job(self.task_id)
            data_dic.update(
                task_id=self.task_id,
            )
        elif self.operation == OPERATION.UPDATE:
            remove_job(self.task_id)
            _str = self.search_redis_data(self.task_id)
            if not _str:
                data_dic.update(
                    task_id=self.task_id,
                    message='redis里的数据已经取完'
                )
            else:
                self.add_parameter(_str)
                task = TaskApscheduler(self.get_monitor_result, job_id=self.task_id)
                task.add_job()
                # self.save_data_to_redis(self.task_id, _str)
                data_dic.update(
                    task_id=self.task_id,
                )
        else:
            data_dic.update(
                status=-1,
                message="任务不存在 或 重复提交"
            )
        return data_dic

    def seach_obj_mongo(self, _id):
        from service.db.utils.mongo_utils import connection
        _c = connection.new_media.jobs
        data = _c.find_one({"_id": _id})
        if data:
            return data

    def get_monitor_result(self):
        logger.info("Begin get all data detail ...")
        try:
            #wechat = self.get_wechat_data(self.now_data)
            website = self.get_website_data(self.now_data)
            weibo = self.get_weibo_account_data(self.now_data)
            logger.info("task id : {} is task run over.....".format(self.task_id or self.seq_no))
        except Exception as e:
            logger.exception(e)

    def retrun_index_name(self):
        from service.micro.keyword import ES_INDEX, hp_account
        _list = []
        weibo_index = hp_account(ES_INDEX[0], self.account, self.weibo_user_id)
        wechat_index = hp_account(ES_INDEX[1], self.account, self.weibo_user_id)
        website_index = hp_account(ES_INDEX[4], self.account, self.weibo_user_id)
        _list.extend([
            dict(weibo_index=weibo_index.lower(), account=self.account),
            dict(wechat_index=wechat_index.lower(), account=self.account),
            dict(website_index=website_index.lower(), account=self.account),
        ])
        return _list

    def add_parameter(self, index_list):
        for index in index_list:
            self.now_data.update(index)

    def save_data_to_redis(self, task_id, index_list):
        """
        将数据存到redis队列中
        :param _str:
        :return:
        """
        task_qq = RedisQueue('task_id_index_qq', namespace=task_id)
        case_info = json.dumps(index_list)
        task_qq.put(case_info)
        logger.info("save to redis success!!! case_info={}".format(case_info))

    def search_redis_data(self, task_id):
        logger.info(" search_redis_data  task_id: {} ".format(task_id))
        task_qq = RedisQueue('task_id_index_qq', namespace=task_id)
        case_info = task_qq.get_nowait()
        if case_info:
            _str = case_info.decode("utf-8")
            logger.info("search_redis_data success!!! case_info={}".format(case_info))
            return json.loads(_str)

    def get_weibo_account_data(self, data):
        weibo_data = {}
        try:
            from service.micro.sina.weibo_monitor import WeiBoMonitorSpider
            weibo_spider = WeiBoMonitorSpider(data)
            weibo_data = weibo_spider.query()
            if weibo_data.get("status"):
                return weibo_data
        except Exception as e:
            weibo_data.update(
                status=-1,
                index=None,
                message="微博爬取失败"
            )
        logger.info("weibo account: {} , result : {}".format(data, weibo_data))
        return weibo_data

    def get_website_data(self, data):
        news_data = {}
        try:
            from service.api.utils.ds_utils import get_news_source_with_service
            from service.utils import get_module_from_service
            from service.db.utils.es_mappings import NEWS_DETAIL_MAPPING

            ds = get_news_source_with_service(self.domain)
            if not ds:
                news_data.update(
                    status=-1,
                    message="网址不对"
                )
                return news_data

            _index_mapping = {
                "detail_type":
                    {
                        "properties": NEWS_DETAIL_MAPPING
                    },
            }
            es = ElasticsearchClient()
            es.create_index(data.get("website_index"), _index_mapping)
            handler = get_module_from_service("news", ds.handler)
            data.update(domain=self.domain)
            website = handler.get_handler(data)
            news_url_list = website.get_news_all_url()
            for url in news_url_list:
                news_data = website.get_news_detail(url)
                website.parse_news_detail(news_data)
            logger.info("news keyword : {} , result : {}".format(data, news_data))

            return True
        except Exception as e:
            news_data.update(
                status=-1,
                message="网站爬取失败"
            )
        return news_data

    def get_wechat_data(self, data):
        wechat_data = {}
        try:
            from service.micro.wechat.sougou_monitor import SouGouMonitorSpider
            wechat_spider = SouGouMonitorSpider(data)
            wechat_data = wechat_spider.query()
            if wechat_data.get("status"):
                return wechat_data
        except Exception as e:
            wechat_data.update(
                status=-1,
                index=None,
                message="微信公众号爬取失败"
            )
        logger.info("wechat account: {} , result : {}".format(data, wechat_data))
        return wechat_data


def get_handler(*args, **kwargs):
    return AddMonitorAccount(*args, **kwargs)


if __name__ == '__main__':
    data = {"status": "1", "relative_word": "dasfasdf,", }
    s = AddMonitorAccount(data)
