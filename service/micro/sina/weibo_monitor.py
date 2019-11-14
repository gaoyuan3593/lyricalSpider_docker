#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random
import time
import re
import json
from urllib.parse import quote
from datetime import datetime
from bs4 import BeautifulSoup
from service.core.utils.http_ import Requester
from service.exception import retry
from service.exception.exceptions import *
from service import logger
from service.micro.utils import ua
from service.micro.sina.utils.sina_mid import mid_to_str, str_to_mid
from service.micro.utils.cookie_utils import dict_to_cookie_jar
from service.micro.utils.math_utils import str_to_format_time, weibo_date_next
from service.db.utils.redis_utils import RedisClient
from service.micro.utils.threading_ import WorkerThread
from service.db.utils.elasticsearch_utils import ElasticsearchClient
from service.db.utils.es_mappings import (WEIBO_DETAIL_MAPPING, WEIBO_COMMENT_MAPPING, WEIBO_REPOST_MAPPING,
                                          WEIBO_USERINFO_MAPPING)

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


class WeiBoMonitorSpider(object):
    __name__ = 'Weibo monitor account'

    def __init__(self, params=None):
        self.params = params
        self.es_index = self.params.get("weibo_index")
        self.user_id = self.params.get("weibo_user_id")
        self.cookie = dict_to_cookie_jar(self.get_cookie())
        self.requester = Requester(cookie=self.cookie)
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

    def query(self):
        logger.info('Processing get weibo user id= {} ！'.format(self.user_id))
        detail_list = []
        threads = []
        comment_list, repost_list = [], []
        self.es.create_index(self.es_index, _index_mapping)
        url_list = self.search_weibo_user_page()
        for url in url_list:
            try:
                user_resp = self.get_user_page_data(url)
                detail_list.extend(user_resp)
            except Exception as e:
                print(e)
                url_list.append(url)
                continue
        #     worker = WorkerThread(detail_list, self.get_user_page_data, (url,))
        #     worker.start()
        # for work in threads:
        #     work.join(1)

        comment_url_list, repost_url_list = self.parse_comment_or_repost_url(detail_list)

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

        return dict(
            status=200,
            index=self.es_index,
            message="微博爬取成功！"
        )

    @retry(max_retries=5, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=1)
    def search_weibo_user_page(self):
        """
        获取微博用户页
        :return:
        """
        logger.info('Processing search weibo user id {} ！'.format(self.user_id))
        try:
            url = "https://weibo.cn/u/{}".format(self.user_id)
            headers = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "zh-CN,zh;q=0.9",
                "cache-control": "max-age=0",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
            }
            response = self.requester.get(url=url, header_dict=headers)
            if "charset=GBK" in response.text:
                self.next_cookie()
                raise RequestFailureError
            elif self.user_id in response.text and response.status_code == 200:
                url_list, flag_list = [], []
                soup = BeautifulSoup(response.text, "lxml")
                div_list = soup.find_all("div", attrs={"id": True})[:-1]
                for div in div_list:
                    str_id = div.attrs.get("id")
                    weibo_id = str_id.split("_")[1]
                    result = self.es.get(self.es_index, "detail_type", weibo_id)
                    if result.get("found"):
                        flag_list.append(weibo_id)
                # if len(flag_list) >= 5:
                #     for i in range(1, 3):
                #         url = "https://weibo.cn/u/{}?page={}".format(self.user_id, i)
                #         url_list.append(url)
                else:
                    try:
                        page = soup.find("div", attrs={"id": "pagelist"})
                        if page:
                            num = re.findall(r"(\d+)页", page.text)[0]
                            for i in range(1, int(num) + 1):
                                url = "https://weibo.cn/u/{}?page={}".format(self.user_id, i)
                                url_list.append(url)
                        else:
                            url_list.append("https://weibo.cn/u/{}?page={}".format(self.user_id, 1))
                    except Exception as e:
                        logger.exception(e)
                        raise HttpInternalServerError
                return url_list

            else:
                logger.error('get weibo user name failed !')
                raise HttpInternalServerError
        except Exception as e:
            self.next_cookie()
            self.requester.use_proxy()
            raise HttpInternalServerError

    @retry(max_retries=5, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=1)
    def get_user_page_data(self, url, flag=True):
        """
        获取微博用户每页的内容
        :return:
        """
        logger.info('Processing search get_user_page_data url={} ！'.format(url))
        try:
            headers = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "zh-CN,zh;q=0.9",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
            }
            response = self.requester.get(url=url, header_dict=headers)
            if "charset=GBK" in response.text:
                self.next_cookie()
                raise RequestFailureError
            elif self.user_id in response.text and response.status_code == 200:
                logger.info("get_user_page_data success ！！！")
                if flag:
                    return self.parse_weibo_detail(response.text)
                else:
                    return response.text
            else:
                logger.error('get weibo user name failed !')
                raise HttpInternalServerError
        except Exception as e:
            self.next_cookie()
            self.requester.use_proxy()
            raise HttpInternalServerError

    def parse_weibo_detail(self, resp):
        if not resp:
            return
        try:
            is_forward_weibo_id, key_user_list, forward_user_url_list, data_list = "", [], [], []
            has_href, pics, videos, is_forward = 0, 0, 0, 0
            soup = BeautifulSoup(resp, "lxml")
            div_list = soup.find_all("div", attrs={"id": True})[:-1]
            for tag in div_list:
                weibo_id = tag.attrs.get("id").split("M_")[1]
                mid = str_to_mid(weibo_id)
                if "转发理由" in tag.text and "转发了" in tag.text:
                    is_forward = 1  # 是否是转发微博
                    is_forward_weibo_id = \
                        tag.find("a", attrs={"class": "cc"}).attrs.get("href").split("/")[-1].split("?")[0]
                    _content = re.findall(r"转发理由:(.*)赞", tag.text)
                    if _content:
                        contents = _content[0].strip()
                    content = tag.contents[1]
                else:
                    content = tag.find("span", attrs={"class": "ctt"})
                    if "全文" in content.text:
                        a_tag = content.find("a")
                        if "全文" in a_tag.text:
                            con_url = "https://weibo.cn" + a_tag.get("href")
                            con_resp = self.get_user_page_data(con_url, flag=False)
                            con_soup = BeautifulSoup(con_resp, "lxml")
                            contents = con_soup.find("span", attrs={"class": "ctt"}).text.strip()
                        else:
                            contents = content.text.strip()
                    else:
                        contents = content.text.strip()
                topic = re.findall("#(.*?)#", contents)  # 关键字
                try:
                    is_data = tag.find("span", attrs={"class": "ct"}).text.split("来自")
                    if len(is_data) >= 2:
                        weibo_time, platform = is_data
                    else:
                        weibo_time, platform = is_data[0], "微博 weibo.com"
                except:
                    weibo_time, platform = "", "微博 weibo.com"

                like_num = re.findall(r"赞\[(\d+)\] 转发", tag.text)
                comment_num = re.findall(r"评论\[(\d+)\] 收藏", tag.text)
                repost_num = re.findall(r"转发\[(\d+)\] 评论", tag.text)
                is_photo = tag.find("img")
                if is_photo:
                    pics = 1
                try:
                    is_videos = tag.contents[1].contents[0].attrs.get("href")
                    if is_videos:
                        if "video" in is_videos:
                            videos = 1
                except:
                    videos = 0
                if "请戳右边" in contents:
                    has_href = 1
                try:
                    user_key_list = content.find_all("a")
                    if "//@" in contents:
                        forward_user_url_list = self.parse_key_user_list(user_key_list)  # 解析转发用户链列表
                    elif "@" in contents:
                        key_user_list = self.parse_key_user_list(user_key_list)  # 获取@用户id
                except Exception as e:
                    key_user_list = []
                    forward_user_url_list = []

                resp_dada = dict(
                    weibo_time=str_to_format_time(weibo_time),  # 发微时间
                    platform=platform,  # 平台
                    contents=contents,  # 内容
                    weibo_id=weibo_id,  # 微博id
                    mid=mid,  # 微博id
                    user_id=self.user_id,  # 用户id
                    like_num=int(like_num[0]),  # 点赞数
                    com_num=int(comment_num[0]),  # 评论数
                    repost_num=int(repost_num[0]),  # 转发数
                    is_forward=1 if is_forward else 0,  # 是否转发
                    is_forward_weibo_id=is_forward_weibo_id,  # 转发原微博id
                    type="detail_type",
                    key_user_list=key_user_list,  # @ 用户id 列表
                    forward_user_url_list=forward_user_url_list,  # 转发链 用户id列表
                    topic=topic,  # 双#号话题
                    has_href=has_href,  # 是否有网页链接
                    pics=pics,  # 是否有图片
                    videos=videos,  # 是否有视频
                    crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")  # 爬取时间
                )
                self.save_one_data_to_es(resp_dada, weibo_id)
                data_list.append(
                    dict(com_num=resp_dada.get("com_num"),
                         repost_num=resp_dada.get("repost_num"),
                         weibo_id=resp_dada.get("weibo_id"))
                )
        except Exception as e:
            logger.exception(e)
            return {}
        return data_list

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
            self.requester.use_proxy()
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
            self.requester.use_proxy()
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
                self.save_one_data_to_es(info_data, uid)
            else:
                p_dic = dict(city="其他", gender="其他", introduction=None, grade=None, registration=None,
                             birthday=None)
                user_dic = dict(p_dic, **profile_data.get("data"))
                self.save_one_data_to_es(user_dic, uid)
            return True
        except Exception as e:
            time.sleep(0.5)
            self.requester.use_proxy()
            raise HttpInternalServerError

    def parse_comment_or_repost_url(self, data_list):
        comment_url_list, repost_url_list = list(), list()
        try:
            data_list = list(filter(None, data_list))
            for data in data_list:
                comment_num = data.get("com_num")
                weibo_id = data.get("weibo_id")
                repost_num = data.get("repost_num")
                if comment_num:
                    count = 2 if comment_num < 10 else comment_num // 10 + 2
                    comment_url_list.append(dict(user_id=self.user_id, weibo_id=weibo_id, url_list=[
                        "https://weibo.cn/comment/{}?&uid={}&page={}".format(weibo_id, self.user_id, i) for i in
                        range(1, count)]))
                if repost_num:
                    count = 2 if repost_num < 10 else repost_num // 10 + 2
                    repost_url_list.append(dict(user_id=self.user_id, weibo_id=weibo_id, url_list=[
                        "https://weibo.cn/repost/{}?uid={}&page={}".format(weibo_id, self.user_id, i) for i in
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
                url = "https://weibo.cn" + i.get("href")
                try:
                    headers = {
                        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                        "accept-encoding": "gzip, deflate, br",
                        "accept-language": "zh-CN,zh;q=0.9",
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
                    }
                    user_resp = self.requester.get(url, header_dict=headers)
                    if "首页" in user_resp.text:
                        uid = re.findall(r"uid=(\d+)?", user_resp.text)[0]
                        user_id_list.append(uid)
                    else:
                        raise HttpInternalServerError
                except Exception as e:
                    self.next_cookie()
                    self.requester.use_proxy()
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
                self.save_one_data_to_es(resp_dada, comment_id)
                user_url_list = self.parse_user_info_url([user_id])
                user_data = self.get_user_info(user_url_list[0])
                self.get_profile_user_info(user_data)
        except Exception as e:
            logger.exception(e)
            raise e

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
                self.save_one_data_to_es(resp_dada, user_id)
                user_url_list = self.parse_user_info_url([user_id])
                user_data = self.get_user_info(user_url_list[0])
                self.get_profile_user_info(user_data)
        except Exception as e:
            logger.exception(e)
            raise e

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
    return WeiBoMonitorSpider(*args, **kwargs)


if __name__ == '__main__':
    dic = {
        "weibo_index": "weibo_tian_jin_ri_bao_3546332963",
        # "weibo_user_id": "6218430096",
        "weibo_user_id": "3546332963",
        "date": "2019-08-01:2019-08-03"
    }
    wb = WeiBoMonitorSpider(dic)
    wb.query()
