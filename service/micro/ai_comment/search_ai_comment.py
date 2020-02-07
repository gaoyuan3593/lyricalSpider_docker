#! /usr/bin/python3
# -*- coding: utf-8 -*-
import json
import multiprocessing

import pypinyin

from service import logger
from service.micro.sina.ai_comment import AiCommentSpider
from service.micro.utils.apscheduler_ import TaskApscheduler
from service.utils.seq_no import generate_seq_no
from service.micro.keyword.utils.utils import remove_job, resume_job, pause_job
from service.micro.keyword import OPERATION
from service.db.utils.redis_utils import RedisQueue
from service.core.config.redis_ import ai_comment_redis_cli


class SearchAiComment(object):
    def __init__(self, data):
        self.data = data
        self.seq_no = generate_seq_no()
        self.task_id = self.data.get("task_id")
        self.operation = self.data.get("operation")
        self.index_name = self.data.get("index_name")
        self.index = self.data.get("index")
        self.keyword = self.data.get("relative_word")
        self.now_data = dict(q=None)

    def query(self):
        logger.info("Begin search ai comment run ...")
        data_dic = dict(
            status=200,
            task_id=self.seq_no,
            result=[],
            message="success",
        )
        if not self.keyword:
            data_dic.update(
                status=-1,
                task_id="",
                message='请加上关键词进行采集。'
            )
            return data_dic

        if self.operation == OPERATION.CREATE:
            index_dic = self.retrun_index_name()
            self.add_parameter(index_dic)
            task = TaskApscheduler(self.get_ai_comment_data, job_id=self.seq_no)
            task.add_job()
            data_dic.update(
                task_id=self.seq_no,
                result=index_dic
            )
            self.save_data_to_redis(self.seq_no, index_dic)
            return data_dic
        elif self.operation == OPERATION.DELETE:
            remove_job(self.task_id)
            data_dic.update(
                task_id=self.task_id,
                message="任务已删除成功"
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

    def get_ai_comment_data(self):
        logger.info("Begin get all data detail ...")
        try:
            #self.now_data.update(q=self.keyword.strip())
            ai_obj = AiCommentSpider(self.now_data)
            ai_obj.query()
            logger.info("task id : {} is task run over.....".format(self.task_id or self.seq_no))
        except Exception as e:
            logger.exception(e)
            return

    def retrun_index_name(self):
        if self.index:
            keyword = self.index
        else:
            keyword = self.keyword
        index = self.hp("ai_", keyword)
        return dict(index=index.lower(), q=keyword)

    def add_parameter(self, index):
        self.now_data.update(index)

    def hp(self, title, text):
        s = ""
        if "," in text:
            text = text.replace(",", "")
        if " " in text:
            text = text.replace(" ", "")
        text = text.strip()
        for i in pypinyin.pinyin(text, style=pypinyin.NORMAL):
            s += "{}{}".format(''.join(i), "_")
        return "{}{}".format(title, s).strip("_")

    def save_data_to_redis(self, task_id, index_list):
        """
        将index名字存到redis队列
        :param _str:
        :return:
        """
        task_qq = RedisQueue('task_id_index_qq', namespace=task_id, redis_cli=ai_comment_redis_cli)
        case_info = json.dumps(index_list)
        try:
            task_qq.put(case_info)
            logger.info("save to redis success!!! task_id={}, case_info={}".format(task_id, case_info))
        except Exception as e:
            logger.exception(e)

    def search_redis_data(self, task_id):
        logger.info(" search_redis_data  task_id: {} ".format(task_id))
        task_qq = RedisQueue('task_id_index_qq', namespace=task_id, redis_cli=ai_comment_redis_cli)
        case_info = task_qq.get_nowait()
        if case_info:
            _str = case_info.decode("utf-8")
            logger.info("search_redis_data success!!! case_info={}".format(case_info))
            return json.loads(_str)


def get_handler(*args, **kwargs):
    return SearchAiComment(*args, **kwargs)


if __name__ == '__main__':
    data = {"status": "1", "relative_word": "dasfasdf,", }
    s = SearchAiComment(data)
