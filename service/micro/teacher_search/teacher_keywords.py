#! /usr/bin/python3
# -*- coding: utf-8 -*-

import json
import requests
from datetime import datetime, timedelta
import multiprocessing
from service import logger
from service.micro.baidu.baijiahao_teacher import BaiJiaHaoTeacherSpider
from service.micro.baidu.tieba_teacher import TiebaTeacherSpider
from service.micro.sina.weibo_teacher import WeiBoTeacherSpider
from service.micro.zhihu.zhihu_teacher import ZhiHuTeacherSpider
from service.micro.muchong.xiaomuchong import XiaoMuChongSpider
from service.micro.utils.apscheduler_ import TaskApscheduler
from service.utils.seq_no import generate_seq_no
from service.micro.keyword.utils.utils import remove_job


class TeacherKeyword(object):
    def __init__(self, data):
        self.data = data
        self.seq_no = generate_seq_no()
        self.index = self.data.get("index")
        self.date = self.data.get("date")
        self.params = json.loads(self.data.get("teacher"))
        self.name_cn = self.params.get("nameCn")
        self.name_en = self.params.get("nameEn")
        self.id = self.params.get("id")
        self.keyword = self.data.get("keyword")
        self.keyword_list = self.keyword.split(";")
        self.now_data = dict(q=None, index=None, date=self.date, name_cn=self.name_cn, name_en=self.name_en)

    def query(self):
        logger.info("Begin search keyword run ...")
        data_dic = dict(
            status=200,
            index=None,
            message="success",
        )
        if ";" not in self.keyword:
            data_dic.update(
                status=-1,
                message='关键字格式错误, 请用英文“分号”做为分隔符.'
            )
            return data_dic
        index = self.retrun_index_name()
        data_dic.update(index=index)
        self.now_data.update(index=index)

        task = TaskApscheduler(self.get_search_keyword_data, job_id=self.seq_no)
        task.add_job()
        return data_dic

    def get_search_keyword_data(self):
        logger.info("Begin get all data detail ...")

        try:
            remove_job(self.seq_no)
            for keyword in self.keyword_list:
                if not keyword:
                    continue
                self.now_data.update(q=keyword.strip())
                func_list = [self.get_weibo_data, self.get_baijiahao_data, self.get_tieba_data,
                             self.get_zhihu_data, self.get_xiao_mu_chong_data]
                # func_list = [self.get_zhihu_data]
                for func in func_list:
                    # w = multiprocessing.Process(target=func, args=(self.now_data,))
                    # w.start()
                    # w.join(2)
                    func(self.now_data)
                logger.info("get search keyword data is task run over.....")
                barck_url = "http://172.19.135.131:8002/teacherInformation/complete?id={}".format(self.id)
                resp = requests.post(barck_url)
                logger.info(resp.text)
        except Exception as e:
            raise e

    def retrun_index_name(self):
        import pypinyin
        s = ""
        for i in pypinyin.pinyin(self.keyword_list[0], style=pypinyin.NORMAL):
            s += "{}{}".format(''.join(i), "_")
        return "{}".format(s).strip("_")

    def get_weibo_data(self, data):
        weibo_data = {}
        try:
            weibo_spider = WeiBoTeacherSpider(data)
            weibo_data = weibo_spider.query()
        except Exception as e:
            weibo_data.update(
                status=-1,
                index=None,
                message="微博爬取失败"
            )
        logger.info("weibo keyword: {} , result : {}".format(data, weibo_data))
        return weibo_data

    def get_baijiahao_data(self, data):
        bajihao_data = {}
        try:
            spider = BaiJiaHaoTeacherSpider(data)
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
            spider = TiebaTeacherSpider(data)
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

    def get_zhihu_data(self, data):
        zhihu_data = {}
        try:
            spider = ZhiHuTeacherSpider(data)
            zhihu_data = spider.query()
            if zhihu_data.get("status"):
                return zhihu_data
        except Exception as e:
            zhihu_data.update(
                status=-1,
                index=None,
                message="知乎爬取失败"
            )
        logger.info("zhi hu keyword : {} , result : {}".format(data, zhihu_data))
        return zhihu_data

    def get_xiao_mu_chong_data(self, data):
        xiao_mu_chong_data = {}
        try:
            spider = XiaoMuChongSpider(data)
            xiao_mu_chong_data = spider.query()
            if xiao_mu_chong_data.get("status"):
                return xiao_mu_chong_data
        except Exception as e:
            xiao_mu_chong_data.update(
                status=-1,
                index=None,
                message="小木虫爬取失败"
            )
        logger.info("xiao mu chong keyword : {} , result : {}".format(data, xiao_mu_chong_data))
        return xiao_mu_chong_data


def get_handler(*args, **kwargs):
    return TeacherKeyword(*args, **kwargs)


if __name__ == '__main__':
    data = {"status": "1", "relative_word": "dasfasdf,", }
    s = TeacherKeyword(data)
