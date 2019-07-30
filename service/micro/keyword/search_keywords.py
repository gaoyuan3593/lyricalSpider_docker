#! /usr/bin/python3
# -*- coding: utf-8 -*-
import multiprocessing
from service import logger
from service.micro.baidu.baijiahao_keyword import BaiJiaHaoSpider
from service.micro.baidu.tieba_keyword import TiebaSpider
from service.micro.sina.weibo_keyword import WeiBoSpider
from service.micro.sougou_wechat.sougou_keyword import SouGouKeywordSpider
from service.micro.utils.apscheduler_ import TaskApscheduler
from service.utils.seq_no import generate_seq_no
from service.micro.keyword.utils.utils import remove_job, resume_job, pause_job


class SearchKeyword(object):
    def __init__(self, data):
        self.data = data
        self.seq_no = generate_seq_no()
        self.date = self.data.get("date")
        self.task_id = self.data.get("task_id")
        self.status = int(self.data.get("status"))
        self.relative_word = self.data.get("relative_word")
        self.exclude_word = self.data.get("exclude_word")
        self.public_opinion_word = self.data.get("public_opinion_word")
        self.now_data = dict(q=None, date=self.date)
        self.keyword_list = self.relative_word.split(";")

    def _run(self):
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
        task_obj = self.seach_obj_mongo(self.task_id if self.task_id else self.seq_no)
        if not task_obj:
            if self.status != 1:
                data_dic.update(
                    task_id=None,
                    message="任务不存在, 请新建任务"
                )
                return data_dic
            if self.task_id:
                if len(self.task_id) < 32 or len(self.task_id) > 32:
                    data_dic.update(
                        task_id=self.task_id,
                        message="请用32位长度的 字母或数字"
                    )
                    return data_dic
            task = TaskApscheduler(self.get_all_data, self.status, self.task_id if self.task_id else self.seq_no)
            index_list = self.retrun_index_name()
            for index in index_list:
                self.now_data.update(index)
            result = [
                index.get("weibo_index") or index.get("wechat_index") or index.get("baijiahao_index") or index.get(
                    "tieba_index")
                for index in index_list]
            task.add_job()
            data_dic.update(
                task_id=self.task_id if self.task_id else self.seq_no,
                result=result
            )
            return data_dic

        else:
            if (self.status == 0 or self.status == 3) and self.task_id:
                remove_job(self.task_id)
                data_dic.update(
                    task_id=self.task_id,
                    message="任务已删除成功"
                )
            elif self.status == 1 and self.task_id:
                resume_job(self.task_id)
                data_dic.update(
                    task_id=self.task_id,
                    message="任务以恢复采集状态"
                )
            elif self.status == 2 and self.task_id:
                pause_job(self.task_id)
                data_dic.update(
                    task_id=self.task_id,
                    message='任务已经暂停采集'
                )
            else:
                data_dic.update(
                    status=-1,
                    message="状态值不存在 或 重复提交"
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
        for keyword in self.keyword_list:
            if not keyword:
                continue
            try:
                self.now_data.update(q=keyword)
                func_list = [self.get_weibo_data, self.get_wechat_data, self.get_baijiahao_data, self.get_tieba_data]
                for func in func_list:
                    w = multiprocessing.Process(target=func, args=(self.now_data,))
                    w.start()
                    w.join(1)
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
