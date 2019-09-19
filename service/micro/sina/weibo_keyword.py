#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random
import time
import re
import gc
import json
from datetime import datetime
from bs4 import BeautifulSoup
from service.core.utils.http_ import Requester
from service.exception import retry
from service.exception.exceptions import *
from service import logger
from service.micro.utils import ua
from service.micro.utils.cookie_utils import dict_to_cookie_jar
from service.micro.utils.math_utils import str_to_format_time, weibo_date_next
from service.db.utils.redis_utils import RedisClient
from service.micro.utils.threading_ import WorkerThread
from service.db.utils.elasticsearch_utils import ElasticsearchClient
from service.db.utils.es_mappings import (WEIBO_DETAIL_MAPPING, WEIBO_COMMENT_MAPPING, WEIBO_REPOST_MAPPING,
                                          WEIBO_USERINFO_MAPPING)
from service.micro.sina.utils.sina_mid import mid_to_str

_index_mapping = {
    "detail_type":
        {
            "properties": WEIBO_DETAIL_MAPPING
        },
    "comment_type":
        {
            "properties": WEIBO_COMMENT_MAPPING
        },
    "repost_type":
        {
            "properties": WEIBO_REPOST_MAPPING
        },
    "user_type":
        {
            "properties": WEIBO_USERINFO_MAPPING
        }
}


class WeiBoSpider(object):
    __name__ = 'Weibo kek word'

    def __init__(self, params=None):
        self.params = params
        self.headers = {
            'User-Agent': ua(),
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 's.weibo.com',
        }
        self.es_index = self.params.get("weibo_index")
        self.cookie = dict_to_cookie_jar(self.get_cookie())
        self.requester = Requester(cookie=self.cookie, timeout=15)
        self.es = ElasticsearchClient()

    def get_cookie(self):
        redis_cli = RedisClient('cookies', 'weibo')
        return redis_cli.return_choice_cookie()

    def next_cookie(self):
        cookie = dict_to_cookie_jar(self.get_cookie())
        self.requester = Requester(cookie=cookie)

    def random_num(self):
        return random.uniform(0.5, 2)

    def filter_keyword(self, id, _type, data=None):
        try:
            result = self.es.get(self.es_index, _type, id)
            if result.get("found"):
                if _type == "repost_type":
                    return True
                else:
                    self.es.update(self.es_index, _type, id, data)
                    logger.info("update success  data : {}".format(data))
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
            _type = data.get("type")
            if self.filter_keyword(id, _type, data):
                return
            self.es.insert(self.es_index, _type, data, id)
            logger.info("save to es success [ index : {}, data={}]！".format(self.es_index, data))
        except Exception as e:
            logger.exception(e)
            raise e

    def url_threads(self, dic):
        html_list, threads = [], []
        for data in dic:
            url = data.get("url")
            keyword = data.get("keyword")
            # 获取每页内容的html
            try:
                html_list.append(self.get_weibo_page_data(url, keyword))
            except Exception as e:
                logger.exception(e)
                continue
        return [data for data in html_list if not data.get("status")]

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def query(self):
        logger.info('Processing get weibo key word ！')
        try:
            url_list = weibo_date_next(self.params)
            if isinstance(url_list, list):
                threads = []
                wb_data_list = []
                weibo_detail_list, comment_list, repost_list, user_id_list = [], [], [], []
                user_info_list, page_data_url_list, page_html_url_list = [], [], []
                html_list = self.url_threads(url_list)
                if html_list:
                    self.es.create_index(self.es_index, _index_mapping)
                    for data in html_list:
                        # 解析每个热搜的所有页的url
                        worker = WorkerThread(page_data_url_list, self.parse_weibo_page_url, (data,))
                        worker.start()
                        threads.append(worker)
                    for work in threads:
                        if work.isAlive():
                            logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
                    threads = []
                else:
                    return dict(
                        status=1,
                        index=None,
                        message="微博暂无数据"
                    )
                for page_url_data in page_data_url_list:
                    # 获取每页内容的html
                    url = page_url_data.get("url")
                    keyword = page_url_data.get("keyword")
                    worker = WorkerThread(page_html_url_list, self.get_weibo_page_data, (url, keyword))
                    worker.start()
                    threads.append(worker)
                for work in threads:
                    if work.isAlive():
                        logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
                        threads.append(work)
                threads = []
                for html_data in page_html_url_list:
                    # 解析每页的20微博内容
                    worker = WorkerThread(wb_data_list, self.parse_weibo_html, (html_data,))
                    worker.start()
                    threads.append(worker)
                for work in threads:
                    work.join(1)
                    if work.isAlive():
                        logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
                        threads.append(work)
                threads = []

                for wb_data in wb_data_list:
                    # 解析微博详情
                    if not wb_data:
                        continue
                    keyword = wb_data.get("keyword")
                    for data in wb_data.get("data"):
                        # try:
                        #     weibo_detail_list.append(self.parse_weibo_detail(data, keyword))
                        # except:
                        #     continue
                        worker = WorkerThread(weibo_detail_list, self.parse_weibo_detail, (data, keyword))
                        worker.start()
                        threads.append(worker)
                    for work in threads:
                        work.join(1)
                    threads = []
                comment_url_list, repost_url_list = self.parse_comment_or_repost_url(weibo_detail_list)

                if comment_url_list or repost_url_list:
                    for data in comment_url_list:  # 所有评论url
                        weibo_id = data.get("weibo_id")
                        user_id = data.get("user_id")
                        for url in data.get("url_list"):
                            worker = WorkerThread(comment_list, self.get_comment_data, (url, weibo_id, user_id))
                            worker.start()
                            threads.append(worker)
                        for work in threads:
                            work.join(1)
                            if work.isAlive():
                                logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
                                threads.append(work)
                        threads = []
                    for data in repost_url_list:  # 所有转发url
                        weibo_id = data.get("weibo_id")
                        user_id = data.get("user_id")
                        for url in data.get("url_list"):
                            worker = WorkerThread(repost_list, self.get_repost_data, (url, weibo_id, user_id))
                            worker.start()
                            threads.append(worker)
                        for work in threads:
                            work.join(1)
                            if work.isAlive():
                                logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
                                threads.append(work)
                        threads = []
                # 获取用户个人信息
                user_url_list = self.parse_user_info_url(user_id_list)
                for url_data in user_url_list:
                    worker = WorkerThread(user_info_list, self.get_user_info, (url_data,))
                    worker.start()
                    threads.append(worker)
                for work in threads:
                    work.join(1)
                    if work.isAlive():
                        logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
                        threads.append(work)

                threads = []
                for user_data in user_info_list:
                    worker = WorkerThread([], self.get_profile_user_info, (user_data,))
                    worker.start()
                    threads.append(worker)
                for work in threads:
                    work.join(1)
                    if work.isAlive():
                        logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
                        threads.append(work)

                return dict(
                    status=200,
                    index=self.es_index,
                    message="微博爬取成功！"
                )
            gc.collect()
        except Exception as e:
            gc.collect()

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_weibo_page_data(self, url, keyword):
        """
        获取微博内容页
        :return:
        """
        if not url:
            return {}
        logger.info('Processing get weibo key word ！')
        try:
            response = self.requester.get(url=url, header_dict=self.headers)
            if "抱歉，未找到“{}”相关结果。".format(keyword) in response.text or "您可以尝试更换关键词，再次搜索" in response.text:
                return dict(
                    status=200,
                    message="抱歉，未找到“{}”相关结果。".format(keyword)
                )
            if '微博搜索' in response.text and response.status_code == 200:
                logger.info("get_weibo_page_data success ")
                return dict(data=response.text, keyword=keyword, url=url)
            else:
                logger.error('get weibo detail failed !')
                self.requester.use_proxy()
                raise HttpInternalServerError
        except Exception as e:
            self.next_cookie()
            raise HttpInternalServerError

    def parse_weibo_html(self, data):
        """
        解析每页的20条微博
        :return: list
        """
        if data.get("status"):
            return
        response = data.get("data")
        try:
            resp_obj = BeautifulSoup(response, 'html.parser')
            raw_data = resp_obj.find_all("div", attrs={"class": "card-wrap", "mid": True})
            if raw_data:
                return dict(data=raw_data, keyword=data.get("keyword"), url=data.get("url"))
            return {}
        except Exception as e:
            logger.exception(e)
            return {}

    def parse_weibo_page_url(self, data):
        """
        解析当前页面的所有页的url
        :return: list
        """
        if not data:
            return
        if isinstance(data, dict):
            response = data.get("data")
        else:
            response = data
        try:
            resp_obj = BeautifulSoup(response, 'html.parser')
            page_url_obj = resp_obj.find("span", attrs={"class": "list"})
            if page_url_obj:
                page_url_list = page_url_obj.find_all("li")
                url_list = [
                    dict(url="https://s.weibo.com" + obj.contents[0].attrs.get("href").replace("×cope", "&timescope"),
                         keyword=data.get("keyword")
                         ) for obj in page_url_list]
                if url_list:
                    return url_list
            else:
                return dict(data=response, keyword=data.get("keyword"))
        except Exception as e:
            logger.exception(e)
            return []

    def parse_weibo_detail(self, tag_obj, keyword):
        if not tag_obj:
            return {}
        try:
            topic, is_forward_weibo_id, key_user_list, forward_user_url_list = [], None, [], []
            weibo_time, platform = "", "微博 weibo.com"
            has_href, pics, videos = 0, 0, 0
            mid = tag_obj.attrs.get("mid")  # 微博id
            weibo_id = mid_to_str(mid)
            is_forward = tag_obj.find_all("div", attrs={"class": "con"})  # 是否是转发微博
            if len(is_forward):
                is_forward_weibo_id = \
                    is_forward[0].find("p", {"class": "from"}).find("a").attrs.get("href").split("?")[0].replace(
                        "om",
                        "n").split(
                        "cn/")[1].split("/")[1]
            weibo_list = tag_obj.find_all("p", attrs={"class": "from"})
            for tag in weibo_list:
                a_list = tag.find_all("a")
                for a in a_list:
                    if weibo_id in a.attrs.get("href"):
                        weibo_time = a.text.strip()
                        try:
                            platform = a_list[1].text.strip()
                        except:
                            platform = "微博 weibo.com"
            weibo_num = tag_obj.find_all("div", attrs={"class": "card-act"})[0].contents[1].find_all("li")[
                        1:]  # 评论，转发，赞
            raw_id = tag_obj.find("a", {"class": "name", "suda-data": True})
            user_id = raw_id.attrs.get("href").split("/")[3].split("?")[0]

            is_photo = tag_obj.find("div", attrs={"class": "media media-piclist"})
            if is_photo:
                pics = 1
            is_videos = tag_obj.find("div", attrs={"node-type": "fl_h5_video_disp"})
            if is_videos:
                videos = 1
            content = tag_obj.find_all("p", attrs={"class": "txt"})
            if len(content) == 2:
                contents = content[0].text.split("收起全文")[0].strip()
            else:
                contents = content[0].text.strip()
            topic = re.findall("#(.*?)#", contents)  # 关键字
            if "O网页链接" in contents or "随笔" in contents:
                has_href = 1
            if "//@" in contents:
                try:
                    forward_user_url_list = self.parse_forward_user_list(weibo_id, user_id)  # 解析转发用户链列表
                except Exception as e:
                    pass
            else:
                try:
                    user_key_list = content[0].find_all("a")
                    key_user_data = self.parse_key_user_list(user_key_list)  # 获取@用户id
                except Exception as e:
                    key_user_data = []
                if key_user_data:
                    key_user_list = key_user_data
            if "转赞" in weibo_time:
                weibo_time = weibo_time.split("转赞")[0].strip()
            resp_dada = dict(
                weibo_time=str_to_format_time(weibo_time),  # 发微时间
                platform=platform,  # 平台
                contents=contents,  # 内容
                weibo_id=weibo_id,  # 微博id
                mid=mid,  # 微博id
                user_id=user_id,  # 用户id
                like_num=self.comment_str_to_int(weibo_num[2].text),  # 点赞数
                com_num=self.comment_str_to_int(weibo_num[1].text),  # 评论数
                repost_num=self.repost_str_to_int(weibo_num[0].text),  # 转发数
                is_forward=1 if is_forward else 0,  # 是否转发
                is_forward_weibo_id=is_forward_weibo_id,  # 转发原微博id
                type="detail_type",
                key_user_list=key_user_list,  # @ 用户id 列表
                forward_user_url_list=forward_user_url_list,  # 转发链 用户id列表
                b_keyword=keyword,
                topic=topic,  # 双#号话题
                has_href=has_href,  # 是否有网页链接
                pics=pics,  # 是否有图片
                videos=videos,  # 是否有视频
                crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")  # 爬取时间
            )
            self.save_one_data_to_es(resp_dada, id=weibo_id)
            user_url_list = self.parse_user_info_url([user_id])
            user_data = self.get_user_info(user_url_list[0])
            self.get_profile_user_info(user_data)
            return resp_dada
        except Exception as e:
            logger.exception(e)
            return {}

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_comment_data(self, url, weibo_id, user_id):
        """
       获取评论信息
       :param url: 评论页url
       :return:
       """
        headers = {
            "User-Agent": ua()
        }
        try:
            random_time = self.random_num()
            time.sleep(random_time)
            resp = self.requester.get(url, header_dict=headers).text
            self.next_cookie()
            if "首页" in resp and "消息" in resp and "评论" in resp:
                return self.parse_comment_data(resp, weibo_id, user_id)
            else:
                raise HttpInternalServerError
        except Exception as e:
            time.sleep(1)
            self.requester.use_proxy()
            raise HttpInternalServerError

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_repost_data(self, url, weibo_id, user_id):
        """
       获取转发信息
       :param url: 转发页url
       :return:
       """
        headers = {
            "User-Agent": ua()
        }
        try:
            random_time = self.random_num()
            time.sleep(random_time)
            resp = self.requester.get(url, header_dict=headers).text
            self.next_cookie()
            if "首页" in resp and "消息" in resp:
                return self.parse_repost_data(resp, weibo_id, user_id)
            else:
                raise HttpInternalServerError
        except Exception as e:
            time.sleep(1)
            self.requester.use_proxy(tag="same")
            raise HttpInternalServerError

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, ServiceUnavailableError), time_to_sleep=2)
    def get_user_info(self, url_data):
        """
        获取个人信息
        :param uid: 用户id
        :return: dict
        """
        url = url_data.get("url")
        uid = url_data.get("uid")
        headers = {
            "User-Agent": ua()
        }
        try:
            random_time = self.random_num()
            time.sleep(random_time)
            response = self.requester.get(url, header_dict=headers).json()
            if response.get("ok") == 1:
                user_data, containerid = self.parse_user_info(response.get("data", None))
                return dict(user_id=uid, data=user_data, containerid=containerid)
            else:
                return {}
        except Exception as e:
            time.sleep(1)
            self.next_cookie()
            self.requester.use_proxy(tag="same")
            raise HttpInternalServerError

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, ServiceUnavailableError), time_to_sleep=2)
    def get_profile_user_info(self, profile_data):
        """
        获取个人详细信息信息
        :param uid: 用户id
        :return: dict
        """
        try:
            if not profile_data:
                return
            uid = profile_data.get("user_id")
            containerid = profile_data.get("containerid")
            headers = {
                "User-Agent": ua()
            }
            random_time = self.random_num()
            time.sleep(random_time)
            pro_url = "https://m.weibo.cn/api/container/getIndex?uid={}&type=uid&value={}" \
                      "&containerid={}".format(uid, uid, containerid)

            response = self.requester.get(pro_url, header_dict=headers).json()
            self.next_cookie()
            if response.get("ok") == 1:
                u_data = self.parse_profile_info(response)
                info_data = dict(profile_data.get("data"), **u_data)
                self.save_one_data_to_es(info_data, id=uid)
            else:
                p_dic = dict(city="其他", gender="其他", introduction=None, grade=None, registration=None,
                             birthday=None)
                user_dic = dict(p_dic, **profile_data.get("data"))
                self.save_one_data_to_es(user_dic, id=uid)
            return True
        except Exception as e:
            time.sleep(0.5)
            self.requester.use_proxy()
            raise HttpInternalServerError

    def parse_comment_or_repost_url(self, data_list):
        comment_url_list, repost_url_list = [], []
        try:
            data_list = list(filter(None, data_list))
            for data in data_list:
                comment_num = data.get("com_num")
                weibo_id = data.get("weibo_id")
                user_id = data.get("user_id")
                repost_num = data.get("repost_num")
                if comment_num:
                    count = 2 if comment_num < 10 else comment_num // 10 + 2
                    comment_url_list.append(dict(user_id=user_id, weibo_id=weibo_id, url_list=[
                        "https://weibo.cn/comment/{}?&uid={}&page={}".format(weibo_id, user_id, i) for i in
                        range(1, count)]))
                if repost_num:
                    count = 2 if repost_num < 10 else repost_num // 10 + 2
                    repost_url_list.append(dict(user_id=user_id, weibo_id=weibo_id, url_list=[
                        "https://weibo.cn/repost/{}?uid={}&page={}".format(weibo_id, user_id, i) for i in
                        range(1, count)]))
            return comment_url_list, repost_url_list
        except Exception as e:
            return comment_url_list, repost_url_list

    @retry(max_retries=5, exceptions=(HttpInternalServerError, TimedOutError, ServiceUnavailableError), time_to_sleep=3)
    def parse_key_user_list(self, data_list):
        user_id_list, user_id = [], None
        if not data_list:
            return []
        for i in data_list:
            if "@" in i.text:
                if "weibo.com" in i.get("href"):
                    url = "https://weibo.com" + i.get("href").split("com")[1]
                else:
                    url = "https://weibo.com" + i.get("href")
                headers = {
                    "User-Agent": ua()
                }
                try:
                    random_num = self.random_num()
                    time.sleep(random_num)
                    user_resp = self.requester.get(url, header_dict=headers).text
                    self.next_cookie()
                    if "抱歉，未找到" in user_resp:
                        continue
                    uid = re.findall(r"\['oid'\]='(\d+)?", user_resp)[0]
                    user_id_list.append(uid)
                except Exception as e:
                    self.next_cookie()
                    self.requester.use_proxy(tag="same")
                    raise HttpInternalServerError
        return list(set(user_id_list))

    def parse_weibo_type_url(self, obj, _type):
        """
        :param obj: 标签对象
        :return: 评论url
        """
        flag_url = ""
        try:
            flag_url = obj.contents[1].attrs.get("href").split("?")[0].replace("om", "n")
            if _type == "forward":
                uid = flag_url.split("cn/")[1].split("/")[0]
                flag = flag_url.split("cn/")[1].split("/")[1]
                flag_url = "https://weibo.cn/repost/{}?uid={}".format(flag, uid)
        except:
            pass
        return "https:{}?type=comment".format(flag_url) if _type == "comment" else flag_url

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, ServiceUnavailableError), time_to_sleep=3)
    def get_forward_user_list(self, w_id, u_id):
        """
        返回转发用户链的 用户id列表
        :param w_id: 微博id
        :param u_id: 用户id
        :return: list
        """
        forward_user_url = "https://weibo.cn/comment/{}?uid={}".format(w_id, u_id)
        headers = {
            "User-Agent": ua()
        }
        try:
            user_resp = self.requester.get(forward_user_url, header_dict=headers).text
            if "首页" not in user_resp:
                raise HttpInternalServerError
            url_list = user_resp.split('//<a href="')
            forward_user_url_list = ["https://weibo.cn" + url.split('">')[0] for url in url_list if
                                     url.startswith("/n/")]
            return forward_user_url_list
        except Exception as e:
            self.next_cookie()
            self.requester.use_proxy()
            raise HttpInternalServerError

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, ServiceUnavailableError), time_to_sleep=3)
    def parse_forward_user_list(self, w_id, u_id):
        """
        返回转发用户链的 用户id列表
        :param w_id: 微博id
        :param u_id: 用户id
        :return: list
        """
        user_id_list = []
        try:
            forward_user_url_list = self.get_forward_user_list(w_id, u_id)
        except Exception as e:
            return []
        if forward_user_url_list:
            for url in forward_user_url_list:
                try:
                    headers = {
                        "User-Agent": ua()
                    }
                    resp = self.requester.get(url, header_dict=headers).text
                    resp_obj = BeautifulSoup(resp, "html.parser")
                    a_obj = resp_obj.find("div", attrs={"class": "ut"})
                    a_list = a_obj.find_all("a")
                    for k in a_list:
                        if "加关注" in k.text or "私信" in k.text:
                            user_id = k.attrs.get("href").split("uid=")[1].split("&")[0]
                            user_id_list.append(user_id)
                        elif "资料" in k.text:
                            user_id = k.attrs.get("href").split("/")[1]
                            user_id_list.append(user_id)
                except Exception as e:
                    self.next_cookie()
                    self.requester.use_proxy()
                    raise ServiceUnavailableError
            return list(set(user_id_list))

    def comment_str_to_int(self, _str):
        if _str.split(" ")[1].isdigit():
            return int(_str.split(" ")[1])
        return None

    def repost_str_to_int(self, _str):
        if _str.split(" ")[2].isdigit():
            return int(_str.split(" ")[2])
        return None

    def parse_comment_data(self, resp, weibo_id, w_user_id):
        """
        解析评论信息
        :param div_obj: 标签对象
        :return: dict
        """
        div_list, user_id_list, key_user_list = [], [], []
        try:
            user_id_list.append(w_user_id)
            if isinstance(resp, str):
                resp_obj = BeautifulSoup(resp, "html.parser")
                div_list = resp_obj.find_all("div", attrs={"id": True})[1:]
            for div_obj in div_list:
                if "评论只显示前140字:" in div_obj.text or "下页" in div_obj.text or "上页" in div_obj.text:
                    continue
                key_user = div_obj.find_all("a")
                try:
                    _data = self.parse_key_user_list(key_user)
                    if _data:
                        key_user_list = _data
                except Exception as e:
                    pass
                try:
                    _platform = div_obj.find("span", attrs={"class": "ct"}).text
                    comment_time = _platform.split("来自")[0].strip()  # 评论时间
                    platform = _platform.split("来自")[1].strip()  # 平台
                    comment_like = int(div_obj.text.split("赞")[1].split("]")[0].split("[")[1])  # 评论点赞数
                except Exception as e:
                    comment_like, comment_time, platform = 0, datetime.now().strftime('%Y-%m-%d %H:%M'), "网页"
                comment = div_obj.text.split("举报")[0].split(":")
                if len(comment) >= 3:
                    comment_contents = "".join(div_obj.text.split("举报")[0].split(":")[1:])
                else:
                    comment_contents = comment[1].strip(),  # 评论内容
                comment_id = div_obj.attrs.get("id").split("_")[1].strip()  # 评论id
                user_name = div_obj.find("a").text.strip(),  # 用户名
                le_list = div_obj.find("a").attrs.get("href").split("/"),  # 用户id
                user_id = le_list[0][1] if len(le_list[0]) == 2 else le_list[0][2]
                resp_dada = dict(
                    comment_time=str_to_format_time(comment_time),  # 评论时间
                    platform=platform,  # 平台
                    comment_contents="".join(comment_contents) if isinstance(comment_contents,
                                                                             tuple) else comment_contents,  # 评论内容
                    comment_id=comment_id,  # 评论id
                    user_id=user_id,  # 用户id
                    user_name="".join(user_name) if isinstance(user_name, tuple) else user_name,  # 用户名
                    weibo_id=weibo_id,  # 原微博id
                    type="comment_type",
                    comment_like=comment_like,
                    key_user_list=key_user_list,
                    crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")
                )
                user_id_list.append(user_id)
                self.save_one_data_to_es(resp_dada, id=comment_id)
            return list(set(user_id_list))
        except Exception as e:
            return list(set(user_id_list))

    def parse_repost_data(self, resp, weibo_id, w_user_id):
        """
        解析转发信息
        :param div_obj: 标签对象
        :return: dict
        """
        div_list, user_id_list, key_user_list = [], [], []
        try:
            user_id_list.append(w_user_id)
            if isinstance(resp, str):
                resp_obj = BeautifulSoup(resp, "html.parser")
                div_list = resp_obj.find_all("div", attrs={"class": "c"})[1:]
            for div_obj in div_list:
                _len = len(div_obj.contents)
                if not div_obj.text or "返回" in div_obj.text:
                    continue
                try:
                    _platform = div_obj.find("span", attrs={"class": "ct"}).text
                    repost_time = _platform.split("来自")[0].strip()  # 转发时间
                    platform = _platform.split("来自")[1].strip()  # 平台
                    repost_like = int(div_obj.text.split("赞")[1].split("]")[0].split("[")[1])  # 转发点赞数
                except Exception as e:
                    repost_like, repost_time, platform = 0, datetime.now().strftime('%Y-%m-%d %H:%M'), "微博 weibo.com"
                repost_contents = "".join(div_obj.text.split("赞")[0].split(":")[1:]),  # 转发内容
                user_name = div_obj.find("a").text.strip(),  # 用户名
                if ":" in user_name:
                    user_name = "".join(user_name).split(":")[0]
                le_list = div_obj.find("a").attrs.get("href").split("/"),  # 用户id
                if "repost" in le_list[0]:
                    continue
                else:
                    user_id = le_list[0][1] if len(le_list[0]) == 2 else le_list[0][2]
                key_user = div_obj.find_all("a")
                try:
                    _data = self.parse_key_user_list(key_user)
                    if _data:
                        key_user_list = _data
                except Exception as e:
                    pass
                resp_dada = dict(
                    repost_time=str_to_format_time(repost_time),  # 转发时间
                    platform=platform,  # 平台
                    repost_contents="".join(repost_contents) if isinstance(repost_contents,
                                                                           tuple) else repost_contents,  # 转发内容
                    user_id=user_id,  # 用户id
                    user_name="".join(user_name) if isinstance(user_name, tuple) else user_name,  # 用户名
                    weibo_id=weibo_id,  # 原微博id
                    type="repost_type",
                    repost_like=repost_like,
                    key_user_list=key_user_list,
                    crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")
                )
                user_id_list.append(user_id)
                self.save_one_data_to_es(resp_dada, id=user_id)
            return list(set(user_id_list))
        except Exception as e:
            return list(set(user_id_list))

    def parse_user_info(self, data):
        """
        解析个人信息
        :param data: dict
        :param uid: 用户id
        :return:
        """
        try:
            user_info, verified = {}, "common"
            fan_data = data.get("userInfo")
            con_id_list = data.get("tabsInfo").get("tabs")
            con_id = "".join([i.get("containerid") for i in con_id_list if i.get("tab_type") == "profile"])
            fan_count = fan_data.get("followers_count")  # 粉丝数
            follow_count = fan_data.get("follow_count")  # 关注数
            profile_image_url = fan_data.get("profile_image_url")  # 头像地址
            user_name = fan_data.get("screen_name")  # 用户名
            verified_reason = fan_data.get("verified_reason")  # 认证信息
            statuses_count = fan_data.get("statuses_count")  # 微博数
            tags = fan_data.get("tags", [])  # 标签
            user_id = fan_data.get("id")  # 用户名
            container_id = con_id + "_-_INFO"
            verified_type = fan_data.get("verified_type")
            if verified_type == 0:
                verified = "yellow"
            elif verified_type == 1 or verified_type == 3:
                verified = "blue"
            user_info.update(
                user_id=user_id,  # 用户id
                fan_count=fan_count,  # 粉丝数
                follow_count=follow_count,  # 关注数
                profile_image_url=profile_image_url,  # 头像url
                user_name=user_name,
                verified=verified if verified else "common",  # 大v
                verified_reason=verified_reason,  # 认证信息
                tags=tags,  # 认证信息
                weibo_count=statuses_count,  # 微博数
                type="user_type"
            )
            return user_info, container_id
        except Exception as e:
            return {}

    def parse_profile_info(self, data):
        """
        解析简介，性别，所在地等等
        :param data: json
        :return:
        """
        if data.get("ok") == 0:
            return {}
        resp_data = data.get("data").get("cards")[0:2]
        city, gender, introduction, grade, sign_time, birthday = "其他", "其他", "", "", None, ""  # 所在地 性别 简介
        for i in resp_data:
            for k in i.get("card_group"):
                if k.get("item_name") == "简介":
                    introduction = k.get("item_content")
                elif k.get("item_name") == "性别":
                    gender = k.get("item_content") if k.get("item_content") else gender
                elif k.get("item_name") == "所在地":
                    if k.get("item_content") != "其他":
                        city = k.get("item_content").split(" ")[0]
                    else:
                        city = "其他"
                elif k.get("item_name") == "等级":
                    grade = k.get("item_content")
                elif k.get("item_name") == "注册时间":
                    sign_time = None if not k.get("item_content") else k.get("item_content")
                elif k.get("item_name") == "生日":
                    birthday = k.get("item_content")
        return dict(city=city, gender=gender, introduction=introduction, grade=grade, registration=sign_time,
                    birthday=birthday)

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, ServiceUnavailableError), time_to_sleep=2)
    def get_num_user_id(self, uid):
        if not uid:
            return
        url = "https://weibo.com/{}?is_hot=1".format(uid)
        headers = {
            "User-Agent": ua()
        }
        try:
            time.sleep(1)
            resp = self.requester.get(url, header_dict=headers).text
            uid = re.findall(r"\['oid'\]='(\d+)?", resp)[0]
        except Exception as e:
            self.next_cookie()
            self.requester.use_proxy()
            raise HttpInternalServerError
        return [uid]

    def thread_uid_url(self, uid_list):
        new_uid_list, threads = [], []
        for uid in uid_list:
            worker = WorkerThread(new_uid_list, self.get_num_user_id, (uid,))
            worker.start()
            threads.append(worker)
        for work in threads:
            work.join(1)
            if work.isAlive():
                logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
                threads.append(work)

        return new_uid_list

    def parse_user_info_url(self, uid_list):
        uid_list = list(set(uid_list))
        url_list = []
        num_uid = [uid for uid in uid_list if uid.isdigit()]
        eg_uid = [uid for uid in uid_list if not uid.isdigit()]
        if eg_uid:
            eg_uid_list = self.thread_uid_url(eg_uid)
            num_uid.extend(eg_uid_list)
        for uid in num_uid:
            if not uid.isdigit():
                uid = self.get_num_user_id(uid)
            url = "https://m.weibo.cn/api/container/getIndex?uid={}&type=uid&value={}".format(uid, uid)
            url_list.append(dict(url=url, uid=uid))
        return url_list


def get_handler(*args, **kwargs):
    return WeiBoSpider(*args, **kwargs)


if __name__ == '__main__':
    dic = {
        "weibo_index": "test",
        "q": "山东学伴",
        "date": "2019-07-12:2019-07-12"
    }
    wb = WeiBoSpider(dic)
    wb.query()
    import requests

    url = "https://s.weibo.com/weibo?q=%E5%B1%B1%E4%B8%9C%E5%A4%A7%E5%AD%A6%20%E5%AD%A6%E4%BC%B4&typeall=1&suball=1&timescope=custom:2019-07-12-15:2019-07-12-16&Refer=SWeibo_box&page=43"
    headers = {
        "Cookie": "SINAGLOBAL=8384335893100.7295.1557877372731; _s_tentry=-; Apache=9740578615610.205.1558339344679; ULV=1558339344686:3:3:1:9740578615610.205.1558339344679:1558083191060; WBtopGlobal_register_version=5c10f3128cf400c5; login_sid_t=99aadbd8be375bfd49605a861612787d; cross_origin_proto=SSL; SSOLoginState=1562893121; _ga=GA1.2.609809681.1563456706; __gads=ID=2b6aa8d947ce3406:T=1563456712:S=ALNI_MaV0LX0uYYXaL1FFZMIkwhkNNc8uA; wvr=6; UOR=,,login.sina.com.cn; ALF=1597110683; SCF=AgnprrOYzqx7n34kk2eRqbO18FWwG_wVe61JBaKm22XPA62E0qcqbUUBOa3eaFDRiDBMwoxtCwFRZXu_SbNOz7Y.; SUB=_2A25wVLZxDeThGeBG41sX8S_KyT2IHXVTI6C5rDV8PUNbmtBeLUvTkW9NQfzpE0Rv1t-nmCOZz80h53XnfmjPwklz; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5vrGsUJFj6SLfcIHcZdOBA5JpX5KzhUgL.FoqR1h.ceK2ceo22dJLoI0eLxKqL1K.LBoBLxKqL1-eL1h.LxKqL1KMLBoqLxK-LBKBL1-2LxKBLB.2L1K2Eeh2Xeh2t; SUHB=05iqWHVTE9dws9"
    }
    resp = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(resp.text, "html.parser").find_all("div", attrs={"class": "card-wrap", "mid": True})
    print(resp)
    for i in soup:
        data = wb.parse_weibo_detail(i, "asfdsfa")
        print(data)
