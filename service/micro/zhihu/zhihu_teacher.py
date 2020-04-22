#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random
import time
import json
import hashlib
from bs4 import BeautifulSoup
from service.core.utils.http_ import Requester
from service.exception import retry
from service.exception.exceptions import *
from service import logger
from service.db.utils.es_mappings import ZHIHU_DETAIL_MAPPING
from service.db.utils.elasticsearch_utils import es_client, h_es_client
from datetime import datetime

from service.micro.utils import ua

INDEX_TYPE = "zhi_hu"


class ZhiHuTeacherSpider(object):
    __name__ = 'zhi hu keyword'

    def __init__(self, params=None):
        self.params = params
        self.es_index = self.params.get("index")
        self.q = self.params.get("q", None)
        self.name_cn = self.params.get("name_cn")
        self.name_en = self.params.get("name_en")
        self.requester = Requester(timeout=20)
        self.es = es_client
        self.h_es = h_es_client
        self.headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "user-agent": ua(),
        }

    def create_index(self):

        index_mapping = {
            INDEX_TYPE:
                {
                    "properties": ZHIHU_DETAIL_MAPPING
                }

        }
        self.es.create_index(self.es_index, index_mapping)
        self.h_es.create_index(self.es_index, index_mapping)

    def filter_keyword(self, id, _type, data=None):
        try:
            result = self.es.get(self.es_index, _type, id)
            if result.get("found"):
                return True
            return False
        except Exception as e:
            logger.exception(e)
            raise e

    def save_one_data_to_es(self, data, id=None):
        try:
            _type = INDEX_TYPE
            if self.filter_keyword(id, _type, data):
                logger.info("{} Data already exists id: {}".format(self.__name__, id))
                return
            self.es.insert(self.es_index, _type, data, id)
            self.h_es.insert(self.es_index, _type, data, id)
            logger.info("{} save to es success [ index : {}, data={}]！".format(self.__name__, self.es_index, data))
        except Exception as e:
            logger.exception(e)
            raise e

    def random_num(self):
        return random.uniform(1, 3)

    def retrun_md5(self, s):
        m = hashlib.md5()
        m.update(s.encode("utf-8"))
        return m.hexdigest()

    def query(self):
        try:
            self.create_index()
            next_url = "https://api.zhihu.com/search_v3?limit=20&offset=0&q={}".format(self.q)
            while True:
                next_url, data = self.get_api_data(next_url)
                if not data or not next_url:
                    break
                self.parse_zhihu_keyword_data(data)

            return dict(
                status=200,
                index=self.es_index,
                message="知乎爬取成功！"
            )
        except Exception as e:
            logger.exception(e)
            return dict(
                status=200,
                index=self.es_index,
                message="知乎爬取失败！"
            )

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_api_data(self, next_url):
        """
        获取知乎关键字内容页
        :return:
        """
        logger.info('Processing get zhi hu keyword ！')
        try:
            time.sleep(self.random_num())
            response = self.requester.get(url=next_url, header_dict=self.headers)
            if response.status_code == 200:
                logger.info("request zhi hu api keyword data success ")
                resp_data = response.json()
                next_url = resp_data.get("paging").get("next")
                data = resp_data.get("data")
                if data:
                    return next_url, data
                else:
                    return None, None
            else:
                logger.error('get zhi hu keyword data failed !')
                raise HttpInternalServerError
        except Exception as e:
            self.requester.use_proxy()
            raise HttpInternalServerError

    def parse_zhihu_keyword_data(self, data_list):
        if not data_list:
            return
        for data in data_list:
            has_href, pics, videos, img_url_list, content, url = 0, 0, 0, [], "", ""
            try:
                _type = data.get("type")
                if _type == 'one_box':
                    content_list = data.get("object").get("content_list")
                    data_list.remove(data)
                    data_list.extend(content_list)
                    continue
                if _type == 'relevant_query': continue
                if _type == 'answer':
                    _author = data.get("author")
                    _id = data.get("id")
                    question = data.get("question")
                    if question:
                        question_id = question.get("id")
                        url = "https://www.zhihu.com/question/{}/{}/{}".format(question_id, _type, _id)
                    else:
                        print(11111)
                    title = data.get("question").get("name")
                    description = data.get("excerpt")
                    contents = data.get("content")
                    create_time = data.get("created_time")
                    update_time = data.get("updated_time")
                    like_num = data.get("voteup_count")
                    com_num = data.get("comment_count")
                else:
                    _object = data.get("object")
                    if len(_object) <= 10: continue
                    _author = _object.get("author")
                    _id = _object.get("id")
                    _type = _object.get("type")
                    question = _object.get("question")
                    if question:
                        question_id = question.get("id")
                        url = "https://www.zhihu.com/question/{}/{}/{}".format(question_id, _type, _id)
                    elif _type == "article":
                        url = "https://zhuanlan.zhihu.com/{}/{}".format(_type, _id)
                    else:
                        url = "https://zhuanlan.zhihu.com/{}/{}".format(_type, _id)
                    title = data.get("highlight").get("title")
                    description = data.get("highlight").get("description")
                    contents = _object.get("content")
                    create_time = _object.get("created_time")
                    update_time = _object.get("updated_time")
                    like_num = _object.get("voteup_count")
                    com_num = _object.get("comment_count")
                if contents:
                    soup = BeautifulSoup(contents, "html.parser")
                    content = soup.text.strip()
                    img_list = soup.find_all("img")
                    if img_list:
                        pics = 1
                        img_url_list = [tag.attrs.get("src") for tag in img_url_list]
                    if "https" in content or "http" in content:
                        has_href = 1
                if "<em>" in title:
                    title = title.replace("</em>", "").replace("<em>", "")
                task_date = self.params.get("date")
                create_time = self.parse_time_chuo(create_time) if create_time else None
                if not self.parse_crawl_date(create_time, task_date):
                    logger.info("Time exceeds start date data= [ create_time : {}, id : {}]".
                                format(create_time, _id))
                    continue
                if self.name_cn:
                    if self.name_cn not in content:
                        return
                if self.name_en:
                    if self.name_en not in name_en:
                        return
                author_data = self.parse_author_data(_author)
                resp_data = dict(
                    id=_id,  # id
                    user_name=author_data.get("user_name"),  # 用户名
                    user_id=author_data.get("user_id"),  # 用户id
                    title=title,  # 文章标题
                    description=description,  # 简介
                    time=create_time,  # 发表时间
                    update_time=self.parse_time_chuo(update_time) if update_time else None,  # 更新时间
                    contents=content,  # 内容
                    like=like_num,  # 点赞数
                    comment_num=com_num,  # 评论数
                    b_keyword=self.q,  # 关键词
                    link=url,  # 文章链接
                    is_has_href=has_href,  # 是否有网页链接,
                    is_pics=pics,  # 是否有图片,
                    is_videos=videos,  # 是否有视频,
                    img_url_list=img_url_list,  # 图片url列表
                    crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")  # 爬取时间
                )
                self.save_one_data_to_es(resp_data, _id)
            except Exception as e:
                logger.exception(e)
                continue

    def parse_author_data(self, data):
        if not data:
            return
        try:
            topics, author_description = [], ""
            user_id = data.get("id")
            user_name = data.get("name")
            headline = data.get("headline")  # 从事行业
            url_token = data.get("url_token")  # 用户的url_token
            gender = data.get("gender")  # 0 男 -1 女
            profile_image_url = data.get("avatar_url")  # 头像url
            user_type = data.get("user_type")
            is_followed = data.get("is_followed")  # 是否是关注的人
            is_following = data.get("is_following")  # 是否是他的粉丝
            badge = data.get("badge")
            if badge:
                for dge in badge:
                    topic = dge.get("topics")  # 话题
                    if topic:
                        topics.extend([i.get("name") for i in topic])
                    author_description += dge.get("description") + ","  # 作者简介
            author_data = dict(
                id=user_id,  # 用户id
                url_token=url_token,  # url_token
                user_name=user_name,  # 用户名
                headline=headline,  # 从事行业
                gender="男" if gender == 0 else "女",  # 性别
                user_type=user_type,  # 用户类型
                profile_image_url=profile_image_url,  # 头像url
                is_followed=is_followed,  # 是否是关注的人
                is_following=is_following,  # 是否是他的粉丝
                topic_list=topics,  # 话题列表
                introduction=author_description,  # 作者简介
                crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")  # 爬取时间
            )
            # self.save_one_data_to_es(author_data, user_id)
            return author_data
        except Exception as e:
            logger.exception(e)
            return {}

    def parse_time_chuo(self, _time):
        try:
            time_array = time.localtime(_time)
            _time = time.strftime("%Y-%m-%d %H:%M", time_array)
        except Exception as e:
            _time = datetime.now().strftime("%Y-%m-%d %H:%M")
        return datetime.strptime(_time, "%Y-%m-%d %H:%M")

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


if __name__ == '__main__':
    # "天津滨海收费站回应仅供ETC通行"
    parsm = {"q": "李涛", "index": "li_tao",
             "date": "2020-02-09:2020-02-10"}
    zh = ZhiHuTeacherSpider(parsm)
    zh.query()
