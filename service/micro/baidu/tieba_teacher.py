#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random
import time
import json
import re

from urllib import parse
from datetime import datetime
from bs4 import BeautifulSoup
from service.core.utils.http_ import Requester
from service.exception import retry
from service.exception.exceptions import *
from service import logger
from service.micro.utils import ua
from service.micro.utils.threading_ import WorkerThread
from service.db.utils.elasticsearch_utils import es_client, h_es_client
from service.db.utils.es_mappings import TIEBA_DETAIL_MAPPING


INDEX_TYPE = "tie_ba"
_index_mapping = {
    INDEX_TYPE:
        {
            "properties": TIEBA_DETAIL_MAPPING
        },
}


class TiebaTeacherSpider(object):
    __name__ = 'bai du tie ba teacher'

    def __init__(self, params=None):
        self.params = params
        self.es_index = self.params.get("index")
        self.name_cn = self.params.get("name_cn")
        self.name_en = self.params.get("name_en")
        self.requester = Requester(timeout=20)
        self.es = es_client
        self.h_es = h_es_client
        self.task_date = self.params.get("date")

    def filter_keyword(self, id, _type):
        try:
            result = self.es.get(self.es_index, _type, id)
            if result.get("found"):
                return True
            return False
        except Exception as e:
            logger.exception(e)
            raise e

    def save_one_data_to_es(self, data, id=None):
        """
        将为爬取的数据存入es中
        :param data_list: 数据
        :return:
        """
        try:
            _type = INDEX_TYPE
            if self.filter_keyword(id, _type):
                logger.info("Data already exists id: {}".format(id))
                return
            self.es.insert(self.es_index, _type, data, id)
            self.h_es.insert(self.es_index, _type, data, id)
            logger.info("save to es success [ index : {}, data={}]！".format(self.es_index, data))
        except Exception as e:
            logger.exception(e)
            raise e

    def random_num(self):
        return random.uniform(0.1, 0.5)

    def query(self):
        page_data_list, tiezi_url_list, replay_url_list = [], [], []
        threads = []
        keyword = self.params.get("q")
        keyword_dic = self.parse_url_kewword(keyword)
        url_list = self.get_begin_page_url(keyword_dic)
        if not url_list:
            return dict(
                status=1,
                index=None,
                message="百度贴吧暂无数据"
            )
        self.es.create_index(self.es_index, _index_mapping)
        self.h_es.create_index(self.es_index, _index_mapping)

        # 获取所有页的html
        for url_dic in url_list:
            worker = WorkerThread(page_data_list, self.get_page_url_data, (url_dic,))
            worker.start()
            threads.append(worker)
        for work in threads:
            work.join(1)
            if work.isAlive():
                logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
                threads.append(work)

        # 解析 发帖的内容
        for resp_dic in page_data_list:
            try:
                self.parse_tiezi_detail(resp_dic)
            except Exception as e:
                continue

        return dict(
            status=200,
            index=self.es_index,
            message="百度贴吧获取成功！"
        )

    def parse_url_kewword(self, keyword):
        return dict(
            url='http://tieba.baidu.com/f/search/res?isnew=1&ie=utf-8&kw=&qw={}&rn=10&un=&only_thread=1&sm=1'.format(
                parse.quote(keyword)),
            keyword=keyword
        )

    @retry(max_retries=7, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_begin_page_url(self, dic):
        """
        获取开始页的内容
        :return: dict
        """
        logger.info('Processing get baidu tie ba key word ！')
        keyword = dic.get("keyword")
        url = dic.get("url")
        headers = {
            'User-Agent': ua(),
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 'tieba.baidu.com'
        }
        try:
            resp = self.requester.get(url, header_dict=headers)
            if "抱歉，没有找到与" in resp.text:
                logger.info("keyword : {} is not data".format(keyword))
                return
            elif keyword in resp.text and "百度一下，找到相关贴吧贴子" in resp.text:
                logger.info("get_begin_page_url sussess！！！！ ")
                url_list = self.parse_tieba_page_url(resp, keyword)
                return url_list
        except Exception as e:
            self.requester.use_proxy()
            raise e

    @retry(max_retries=7, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_page_url_data(self, dic):
        """
        获取开始页的内容
        :return: dict
        """
        logger.info('Processing get bai du tie ba key word ！')
        keyword = dic.get("keyword")
        url = dic.get("url")
        headers = {
            'User-Agent': ua(),
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 'tieba.baidu.com'
        }
        try:
            resp = self.requester.get(url, header_dict=headers)
            if "抱歉，没有找到与" in resp.text or "去百度网页搜索" in resp.text:
                logger.info("keyword : {} is not data".format(keyword))
                return
            elif keyword in resp.text and "只看主题贴" in resp.text:
                logger.info("get_page_url_data sussess！！！！ ")
                return dict(keyword=keyword, resp=resp.text)
            else:
                raise InvalidResponseError
        except Exception as e:
            time.sleep(0.2)
            self.requester.use_proxy()
            raise e

    def parse_tieba_page_url(self, resp, keyword):
        """
        解析所有页的url
        :return: list
        """
        if not resp:
            return
        url_list = []
        try:
            _str = re.findall(r'百度一下，找到相关贴吧贴子(\d+)?篇，', resp.text)[0]
            page_num = int(_str) // 10 + 1
            soup = BeautifulSoup(resp.text, "html.parser")
            page_num_obj = soup.find("a", attrs={"class": "last"})
            if page_num_obj:
                _page = page_num_obj.attrs.get("href")
                page_num = int(_page.split("pn=")[1])
            for i in range(1, page_num + 1):
                url = "http://tieba.baidu.com/f/search/res?isnew=1&ie=utf-8&kw=&qw={}&rn=10&un=&only_thread=1&sm=1&pn={}".format(
                    keyword, i)
                url_list.append(dict(url=url, keyword=keyword))
            if url_list:
                return url_list
            return []
        except Exception as e:
            url = "http://tieba.baidu.com/f/search/res?isnew=1&kw=&qw={}&rn=10&un=&only_thread=1&sm=1&pn={}".format(
                keyword, 1)
            return [dict(url=url, keyword=keyword)]

    def parse_tiezi_detail(self, resp_dic):
        """
         解析每个关键词的下页内容
        :return: dict
        """
        pics, imgs, content, tid, fid, tieba, author = "", [], "", "", "", None, None
        if not resp_dic:
            return
        logger.info('Processing parse page data！')
        try:
            keyword = resp_dic.get("keyword")
            resp = resp_dic.get("resp")
            soup = BeautifulSoup(resp, "html.parser")
            obj_list = soup.find_all("div", attrs={"class": "s_post"})
            for obj in obj_list:
                title_obj = obj.find("a", attrs={"class": "bluelink"})
                title = title_obj.text.strip()  # 贴子标题
                _content = obj.find("div", attrs={"class": "p_content"})
                if _content:
                    content = _content.text  # 贴子内容，也就是楼主发布的内容
                p_violet = obj.find_all("font", attrs={"class": "p_violet"})
                try:
                    tieba = p_violet[0].text  # 所属贴吧
                    author = p_violet[1].text  # 作者
                    tid = title_obj.attrs.get("data-tid")
                    fid = title_obj.attrs.get("data-fid")
                    author_url = "https://tieba.baidu.com{}".format(p_violet[1].parent.attrs.get("href"))
                except:
                    pass
                if keyword not in keyword:
                    return
                tiezi_time = obj.find("font", attrs={"class": "p_green p_date"}).text.strip()  # 发布时间
                _tiezi_time = datetime.strptime(tiezi_time, "%Y-%m-%d %H:%M")
                article_date = self.parse_crawl_date(_tiezi_time, self.task_date)
                if not article_date:
                    logger.info("Time exceeds start date data= [ article_date : {}, tid : {}]".
                                format(_tiezi_time, tid))
                    return
                is_photo = obj.find_all("div", attrs={"class": "p_mediaCont"})
                if is_photo:
                    pics = 1  # 是否有图片
                    imgs = [i.next.attrs.get("original") for i in is_photo if i.next.attrs.get("original")]  # 图片链接
                if self.name_cn:
                    if self.name_cn not in content:
                        return
                if self.name_en:
                    if self.name_en not in content:
                        return
                resp_data = dict(
                    title=title,  # 贴子标题
                    contents=content,  # 贴子内容，也就是楼主发布的内容
                    tieba=tieba,  # 所属贴吧
                    author=author,  # 作者
                    time=article_date,  # 发布时间
                    is_pics=pics,  # 是否有图片
                    img_url_list=imgs,  # 图片链接
                    b_keywold=keyword,  # 关键字
                    id=tid,  # 贴子id
                    user_id=fid,  # 作者id
                    crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")  # 爬取时间
                )
                self.save_one_data_to_es(resp_data, tid)

        except Exception as e:
            logger.exception(e)

    def parse_crawl_date(self, article_date, task_date):
        if not task_date:
            return
        if ":" in task_date:
            start_date, end_date = task_date.split(":")
            _end_date = datetime.strptime(end_date, "%Y-%m-%d")
            begin_date = datetime.strptime(start_date, "%Y-%m-%d")
            _article_date = datetime.strptime(article_date.strftime("%Y-%m-%d"), "%Y-%m-%d")
            if _article_date.__ge__(begin_date):
                if _article_date.__le__(_end_date):
                    return article_date
                else:
                    return None
            else:
                return None


if __name__ == '__main__':
    data = {
        "date": "2020-02-05:2020-02-27",
        "tieba_index": "tieba_dan_yu_hou_1582701150",
        "q": "单玉厚"
    }
    tieba = TiebaTeacherSpider(data)
    tieba.query()
