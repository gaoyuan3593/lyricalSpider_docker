#! /usr/bin/python3
# -*- coding: utf-8 -*-
import json
import multiprocessing
from service import logger
from service.micro.baidu.baijiahao_keyword import BaiJiaHaoSpider
from service.micro.baidu.tieba_keyword import TiebaSpider
from service.micro.sina.weibo_keyword import WeiBoSpider
from service.micro.sougou_wechat.sougou_keyword import SouGouKeywordSpider
from service.micro.utils.apscheduler_ import TaskApscheduler
from service.utils.seq_no import generate_seq_no
from service.micro.keyword.utils.utils import remove_job, resume_job, pause_job
from service.micro.keyword import OPERATION
from service.db.utils.redis_utils import RedisQueue
from service.core.config.redis_ import event_redis_cli


class SearchKeyword(object):
    def __init__(self, data):
        self.data = data
        self.seq_no = generate_seq_no()
        self.date = self.data.get("date")
        self.task_id = self.data.get("task_id")
        self.operation = self.data.get("operation")
        self.index_name = self.data.get("index_name")
        self.relative_word = self.data.get("relative_word")
        self.exclude_word = self.data.get("exclude_word")
        self.public_opinion_word = self.data.get("public_opinion_word")
        self.now_data = dict(q=None, date=self.date)
        self.keyword_list = self.relative_word.split(";")

    def query(self):
        logger.info("Begin search keyword run ...")
        data_dic = dict(
            status=200,
            task_id=self.seq_no,
            result=[],
            message="success",
        )
        if ";" not in self.relative_word:
            data_dic.update(
                status=-1,
                message='关键字格式错误, 请用英文“分号”做为分隔符.'
            )
            return data_dic

        if self.operation == OPERATION.CREATE:
            task = TaskApscheduler(self.get_all_data, job_id=self.seq_no)
            index_list = self.retrun_index_name()
            self.add_parameter(index_list)
            result = [
                index.get("weibo_index") or index.get("wechat_index") or index.get("baijiahao_index") or index.get(
                    "tieba_index")
                for index in index_list]
            task.add_job()
            data_dic.update(
                task_id=self.seq_no,
                result=result
            )
            self.save_data_to_redis(self.seq_no, index_list)
            return data_dic
        elif self.operation == OPERATION.DELETE:
            remove_job(self.task_id)
            data_dic.update(
                task_id=self.task_id,
                message="任务已删除成功"
            )
        elif self.operation == OPERATION.RESUME:
            resume_job(self.task_id)
            data_dic.update(
                task_id=self.task_id,
                message="任务以恢复采集状态"
            )
        elif self.operation == OPERATION.PAUSE:
            pause_job(self.task_id)
            data_dic.update(
                task_id=self.task_id,
                message='任务已经暂停采集'
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
                task = TaskApscheduler(self.get_all_data, job_id=self.task_id)
                task.add_job()
                self.save_data_to_redis(self.task_id, _str)
                data_dic.update(
                    task_id=self.task_id,
                    message='任务已经修改成功'
                )
        else:
            data_dic.update(
                status=-1,
                message="任务不存在 或 重复提交"
            )
        return data_dic

    def seach_obj_mongo(self, _id):
        from service.db.utils.mongo_utils import connection
        _c = connection.apscheduler.jobs
        data = _c.find_one({"_id": _id})
        if data:
            return data

    def get_all_data(self):
        logger.info("Begin get all data detail ...")
        for keyword in self.keyword_list[:1]:
            if not keyword:
                continue
            try:
                self.now_data.update(q=keyword.strip())
                func_list = [self.get_weibo_data, self.get_wechat_data, self.get_baijiahao_data, self.get_tieba_data]
                for func in func_list:
                    w = multiprocessing.Process(target=func, args=(self.now_data,))
                    w.start()
                    w.join(2)
                logger.info("task id : {} is task run over.....".format(self.task_id or self.seq_no))
            except Exception as e:
                continue

    def retrun_index_name(self):
        from service.micro.keyword import ES_INDEX, hp
        _list = []
        keyword = self.keyword_list[0]
        weibo_index = hp(ES_INDEX[0], keyword)
        wechat_index = hp(ES_INDEX[1], keyword)
        tieba_index = hp(ES_INDEX[2], keyword)
        baijiahao_index = hp(ES_INDEX[3], keyword)
        _list.extend([
            dict(weibo_index=weibo_index.lower(), keyword=keyword),
            dict(wechat_index=wechat_index.lower(), keyword=keyword),
            dict(tieba_index=tieba_index.lower(), keyword=keyword),
            dict(baijiahao_index=baijiahao_index.lower(), keyword=keyword)
        ])
        return _list

    def add_parameter(self, index_list):
        for index in index_list:
            self.now_data.update(index)

    def save_data_to_redis(self, task_id, index_list):
        """
        将index名字存到redis队列
        :param _str:
        :return:
        """
        task_qq = RedisQueue('task_id_index_qq', namespace=task_id, redis_cli=event_redis_cli)
        case_info = json.dumps(index_list)
        task_qq.put(case_info)
        logger.info("save to redis success!!! task_id={}, case_info={}".format(task_id, case_info))

    def search_redis_data(self, task_id):
        logger.info(" search_redis_data  task_id: {} ".format(task_id))
        task_qq = RedisQueue('task_id_index_qq', namespace=task_id, redis_cli=event_redis_cli)
        case_info = task_qq.get_nowait()
        if case_info:
            _str = case_info.decode("utf-8")
            logger.info("search_redis_data success!!! case_info={}".format(case_info))
            return json.loads(_str)

    def get_weibo_data(self, data):
        weibo_data = {}
        try:
            weibo_spider = WeiBoSpider(data)
            weibo_data = weibo_spider.query()
            if weibo_data.get("status"):
                return weibo_data
        except Exception as e:
            weibo_data.update(
                status=-1,
                index=None,
                message="微博爬取失败"
            )
        logger.info("weibo keyword: {} , result : {}".format(data, weibo_data))
        return weibo_data

    def get_wechat_data(self, data):
        wechat_data = {}
        try:
            spider = SouGouKeywordSpider(data)
            wechat_data = spider.query()
            return wechat_data
        except Exception as e:
            wechat_data.update(
                status=-1,
                index=None,
                message="搜狗微信爬取失败"
            )
        logger.info("wechat sougou  keyword : {} , result : {}".format(data, wechat_data))
        return wechat_data

    def get_baijiahao_data(self, data):
        bajihao_data = {}
        try:
            spider = BaiJiaHaoSpider(data)
            bajihao_data = spider.query()
            return bajihao_data
        except Exception as e:
            bajihao_data.update(
                status=-1,
                index=None,
                message="百家号爬取失败"
            )
        logger.info("baijiahao keyword : {} , result : {}".format(data, bajihao_data))
        return bajihao_data

    def get_tieba_data(self, data):
        tieba_data = {}
        try:
            spider = TiebaSpider(data)
            tieba_data = spider.query()
            if tieba_data.get("status"):
                return tieba_data
        except Exception as e:
            tieba_data.update(
                status=-1,
                index=None,
                message="百度贴吧爬取失败"
            )
        logger.info("baidu tieba keyword : {} , result : {}".format(data, tieba_data))
        return tieba_data


def get_handler(*args, **kwargs):
    return SearchKeyword(*args, **kwargs)


if __name__ == '__main__':
    data = {"status": "1", "relative_word": "dasfasdf,", }
    s = SearchKeyword(data)
