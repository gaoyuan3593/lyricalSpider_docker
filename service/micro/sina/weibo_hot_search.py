#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random
import time
import requests
import re
import json
import hashlib
from urllib.parse import quote
from datetime import datetime
from bs4 import BeautifulSoup
from service.core.utils.http_ import Requester
from service.db.utils.redis_utils import RedisClient, WEIBO_COMMENT_QQ, WEIBO_REPOST_QQ
from service.exception import retry
from service.exception.exceptions import *
from service import logger
from service.micro.utils import ua
from service.micro.utils.cookie_utils import dict_to_cookie_jar
from service.micro.utils.math_utils import str_to_format_time
from service.db.utils.elasticsearch_utils import es_client, h_es_client, WEIBO_HOT_SEARCH, HOT_SEARCH_WEIBO
from service.micro.utils.threading_ import WorkerThread
from service.micro.sina.utils.sina_mid import mid_to_str
from service.db.utils.es_mappings import HOT_SEARCH_KEYWORD_WEIBO_MAPPING, WEIBO_LEAD_MAPPING


class WeiBoHotSpider(object):
    __name__ = 'Weibo hot search'

    def __init__(self, cookie=None):
        self.cookie = dict_to_cookie_jar(self.get_cookie())
        self.requester = Requester(cookie=self.cookie)
        self.es = es_client
        self.h_es = h_es_client
        self.create_index()

    def get_cookie(self):
        redis_cli = RedisClient('cookies', 'weibo')
        return redis_cli.return_choice_cookie()

    def next_cookie(self):
        cookie = dict_to_cookie_jar(self.get_cookie())
        self.requester = Requester(cookie=cookie)

    def create_index(self):
        _index_mapping = {
            "index_type":
                {
                    "properties": HOT_SEARCH_KEYWORD_WEIBO_MAPPING
                },
        }
        self.es.create_index(HOT_SEARCH_WEIBO, _index_mapping)
        self.h_es.create_index(HOT_SEARCH_WEIBO, _index_mapping)

    def random_num(self):
        return random.uniform(0.1, 1)

    def filter_keyword(self, index, id, _type, data=None):
        try:
            result = self.es.get(index, _type, id)
            if result.get("found"):
                if _type == "repost_type":
                    pass
                elif _type == "index_type":
                    data_list = []
                    raw_data = result.get("_source")
                    raw_heat = raw_data.get("result")
                    current_heat = data.get("result")
                    if current_heat[0].get("heat") != raw_heat[-1].get("heat"):
                        data_list.append(current_heat[0])
                        raw_heat.extend(data_list)
                        self.es.update(HOT_SEARCH_WEIBO, data.get("type"), id=id, body=raw_data)
                        self.h_es.update(HOT_SEARCH_WEIBO, data.get("type"), id=id, body=raw_data)
                elif _type == "user_type":
                    return True
                else:
                    if id == "25eb6af784f38841f8d707fcd16290f7":
                        print(id)
                    self.es.update(index, _type, id, data)
                    self.h_es.update(index, _type, id, data)
                    logger.info("update success  data : {}".format(data))
                return True
            return False
        except Exception as e:
            logger.exception(e)
            raise e

    def search_keyword(self, keyword):
        body = {
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "b_keyword": keyword
                            }
                        }
                    ],
                    "must_not": [],
                    "should": []
                }
            },
            "from": 0,
            "size": 10,
            "sort": [],
            "aggs": {}
        }
        try:
            result = self.es.dsl_search(WEIBO_HOT_SEARCH, "detail_type", body)
        except Exception as e:
            return False
        return result if result.get("hits").get("hits") else False

    def save_one_data_to_es(self, index, data, id=None):
        """
        将为爬取的数据存入es中
        :param data_list: 数据
        :return:
        """
        try:
            _type = data.get("type")
            if self.filter_keyword(index, id, _type, data):
                logger.info("Weibo Data update success id: {}..........".format(id))
                return
            self.es.insert(index, _type, data, id)
            self.h_es.insert(index, _type, data, id)
            logger.info("save to es success [ index : {}, data={}]！".format(index, data))
        except Exception as e:
            logger.exception(e)
            raise e

    def add_data_to_redis(self, _type, _str):
        """
        将数据存到redis队列中
        :param _type:
        :param _str:
        :return:
        """
        if _type is "comment":
            weibo_id, user_id, count = _str.split("|")
            for i in range(1, int(count)):
                url = "https://weibo.cn/comment/{}?uid={}&page={}".format(weibo_id, user_id, i)
                case_info = "{}|{}|{}".format(weibo_id, user_id, url)
                WEIBO_COMMENT_QQ.put(case_info)
                logger.info("save to redis success!!! case_info={}".format(case_info))
        elif _type is "repost":
            weibo_id, user_id, count = _str.split("|")
            for i in range(1, int(count)):
                url = "https://weibo.cn/repost/{}?uid={}&page={}".format(weibo_id, user_id, i)
                case_info = "{}|{}|{}".format(weibo_id, user_id, url)
                WEIBO_REPOST_QQ.put(case_info)
                logger.info("save to redis success!!! case_info={}".format(case_info))

    @retry(max_retries=7, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_hot_search_list(self):
        logger.info('Processing get weibo hot search list!')
        # url = 'https://s.weibo.com/top/summary?cate=realtimehot&sudaref=s.weibo.com&display=0&retcode=6102'
        url = 'https://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr=6'
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 's.weibo.com'
        }
        try:
            response = requests.get(url=url, headers=headers, verify=False,  timeout=10)
            # response = self.requester.get(url=url, header_dict=headers, is_not_redirct=False)
            if '热搜榜' in response.text and response.status_code == 200:
                logger.info("get weibo hot list success...")
                return self.parse_hot_search_data(response.text)
            else:
                logger.error('get weibo hot search list failed !')
                raise HttpInternalServerError
        except Exception as e:
            logger.exception(e)
            self.next_cookie()
            raise HttpInternalServerError

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=2)
    def get_weibo_page_data(self, data):
        """
        获取微博热搜首页的每条热搜的html
        :return: dict
        """
        logger.info('Processing get weibo key word ！')
        try:
            if not data:
                return {}
            url = data.get("url")
            headers = {
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
                'Connection': 'keep-alive',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Host': 's.weibo.com',
            }
            response = self.requester.get(url=url, header_dict=headers)
            if "查看更多结果。还没有账号？" in response.text:
                logger.error('login out!')
                self.next_cookie()
                raise HttpInternalServerError
            elif "微博内容" in response.text:
                logger.info("get_weibo_page_data success !!!")
                return dict(data=response.text, keyword=data.get("keyword"))
            else:
                logger.error('get weibo detail not data !')
                return
        except Exception as e:
            self.requester.use_proxy()
            raise HttpInternalServerError

    def parse_weibo_html(self, data):
        """
        解析每页的20条微博
        :return: list
        """
        if not data:
            return
        response = data.get("data")
        try:
            resp_obj = BeautifulSoup(response, 'html.parser')
            raw_data = resp_obj.find_all("div", attrs={"class": "card-wrap", "mid": True})
            if raw_data:
                logger.info("parse one page data success")
                return dict(data=raw_data, keyword=data.get("keyword"))
            return {}
        except Exception as e:
            logger.exception(e)
            return {}

    def parse_weibo_page_url(self, data):
        """
        解析当前热搜的所有页的url
        :return: list
        """
        if not data:
            return
        response = data.get("data")
        try:
            resp_obj = BeautifulSoup(response, 'html.parser')
            page_url_obj = resp_obj.find("span", attrs={"class": "list"})
            if page_url_obj:
                page_url_list = page_url_obj.find_all("li")
                url_list = [dict(url="https://s.weibo.com" + obj.contents[0].attrs.get("href"),
                                 keyword=data.get("keyword")
                                 ) for obj in page_url_list]
                if url_list:
                    logger.info("parse_weibo_page_url success url_list : {}".format(url_list))

                    return url_list
            else:
                return [
                    dict(keyword=data.get("keyword"),
                         url="https://s.weibo.com/weibo?q={}&Refer=top&sudaref=s.weibo.com&display=0&retcode=6102".format(
                             data.get("keyword"))
                         )
                ]

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
                            pass
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
                contents = content[1].text.split("收起全文")[0].strip()
            else:
                contents = content[0].text.strip()
            comment_num = self.comment_str_to_int(weibo_num[1].text)
            repost_num = self.repost_str_to_int(weibo_num[0].text)
            if "该账号因被投诉违反法律法规和《微博社区公约》的相关规定，现已无法查看。" in contents:
                return
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
                    if "@" in contents:
                        user_key_list = content[0].find_all("a")
                        key_user_data = self.parse_key_user_list(user_key_list)  # 获取@用户id
                        if key_user_data:
                            key_user_list = key_user_data
                except Exception as e:
                    pass
            if "转赞" in weibo_time:
                weibo_time = weibo_time.split("转赞")[0].strip()
            resp_dada = dict(
                time=str_to_format_time(weibo_time),  # 发微时间
                platform=platform,  # 平台
                contents=contents,  # 内容
                id=weibo_id,  # 微博id
                mid=mid,  # 微博id
                user_id=user_id,  # 用户id
                like=self.comment_str_to_int(weibo_num[2].text),  # 点赞数
                comment_num=self.comment_str_to_int(weibo_num[1].text),  # 评论数
                repost_num=self.repost_str_to_int(weibo_num[0].text),  # 转发数
                is_forward=1 if is_forward else 0,  # 是否转发
                forward_weibo_id=is_forward_weibo_id,  # 转发原微博id
                type="detail_type",
                key_user_id_list=key_user_list,  # @用户id 列表
                forward_user_id_list=forward_user_url_list,  # 转发链 用户id列表
                b_keyword=keyword,
                topic_list=topic,  # 双#号话题
                is_has_href=has_href,  # 是否有网页链接
                is_pics=pics,  # 是否有图片
                is_videos=videos,  # 是否有视频
                crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")  # 爬取时间
            )
            self.save_one_data_to_es(WEIBO_HOT_SEARCH, resp_dada, id=weibo_id)
            if comment_num or repost_num:
                # 有评论或转发数 存入redis
                self.parse_comment_or_repost_url(weibo_id, user_id, comment_num, repost_num)
            try:
                if self.filter_keyword(WEIBO_HOT_SEARCH, user_id, "user_type"):
                    logger.info("user id is exist user id: {}".format(user_id))
                    return
                user_url_list = self.parse_user_info_url([user_id])
                user_data = self.get_user_info(user_url_list[0])
                self.get_profile_user_info(user_data)
            except Exception as e:
                pass
            return
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
            "User-Agent": ua(),
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "accept-encoding": "gzip, deflate, br",
        }
        try:
            logger.info('Processing get comment data!')
            random_time = self.random_num()
            time.sleep(random_time)
            self.next_cookie()
            resp = self.requester.get(url, header_dict=headers).text
            if "首页" in resp and "消息" in resp:
                logger.info("get_comment_data success weibo_id:{}".format(weibo_id))
                return dict(data=resp, type="comment_type", weibo_id=weibo_id, user_id=user_id)
            else:
                logger.error("get_comment_data falied")
                self.requester.use_proxy()
                raise HttpInternalServerError
        except Exception as e:
            time.sleep(1)
            self.next_cookie()
            raise HttpInternalServerError

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_repost_data(self, url, weibo_id, user_id):
        """
       获取转发信息
       :param url: 转发页url
       :return:
       """
        headers = {
            "user-agent": ua()
        }
        try:
            resp = self.requester.get(url, header_dict=headers)
            self.next_cookie()
            if "首页" in resp and "消息" in resp.text:
                return dict(data=resp.text, type="repost_type", weibo_id=weibo_id, user_id=user_id)
            elif "charset=utf-8" in resp.text:
                resp.encoding = "utf-8"
                return dict(data=resp.text, type="repost_type", weibo_id=weibo_id, user_id=user_id)
            else:
                self.requester.use_proxy()
                raise HttpInternalServerError
        except Exception as e:
            self.next_cookie()
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
                logger.info("get user info Successfully user_id= {}".format(uid))
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
                self.save_one_data_to_es(WEIBO_HOT_SEARCH, info_data, id=uid)
            else:
                p_dic = dict(city=None, gender=None, introduction=None, grade=None, registration=None,
                             birthday=None)
                user_dic = dict(p_dic, **profile_data.get("data"))
                self.save_one_data_to_es(WEIBO_HOT_SEARCH, user_dic, id=uid)
            return True
        except Exception as e:
            time.sleep(1)
            self.next_cookie()
            self.requester.use_proxy()
            raise HttpInternalServerError

    def parse_search_data(self, obj):
        """
        暂时没有用到
        :param obj:
        :return:
        """
        return_list = list()
        try:
            data_list = obj.find_all("ul", attrs={"class": "list_a"})[0]
            hot_list = data_list.find_all("li")[1:]
            for raw in hot_list:
                index = raw.contents[1].contents[1].text.strip()
                keyword = str(raw.contents[1].contents[3].contents[0])
                search_num = raw.contents[1].contents[3].contents[1].text.strip()
                mark = ""
                w_url = "https://s.weibo.com" + raw.contents[1].attrs.get("href")
                return_list.append({keyword: dict(
                    index=index,
                    keyword=keyword,
                    search_num=search_num,
                    mark=mark,
                    w_url=w_url
                )})

            return return_list
        except Exception as e:
            raise RequestFailureError

    def parse_comment_or_repost_url(self, weibo_id, user_id, comment_num=None, repost_num=None):
        try:
            if comment_num:
                count = 2 if comment_num < 10 else comment_num
                count = 51 if count > 50 else count
                self.add_data_to_redis("comment", "{}|{}|{}".format(weibo_id, user_id, count))
            if repost_num:
                count = 2 if repost_num < 10 else repost_num  # 最多页数显示一万数据
                count = 101 if count > 100 else count
                self.add_data_to_redis("repost", "{}|{}|{}".format(weibo_id, user_id, count))
            return
        except Exception as e:
            pass

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
                    self.requester.use_proxy()
                    raise HttpInternalServerError
        return list(set(user_id_list))

    @retry(max_retries=5, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_lead_data(self, keyword):
        logger.info("Begin get lead data.....")
        url = "https://s.weibo.com/weibo?q={}&Refer=SWeibo_box".format(quote("#{}#".format(keyword)))
        headers = {
            'User-Agent': ua(),
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*'
                      ';q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 's.weibo.com',
        }
        try:
            resp = self.requester.get(url, header_dict=headers)
            if '微博搜索' in resp.text and resp.status_code == 200:
                logger.info("get lead data success.... ")
                return self.parse_lead_data(resp.text)
            else:
                self.requester.use_proxy()
                raise HttpInternalServerError
        except Exception as e:
            logger.exception(e)
            self.next_cookie()
            raise HttpInternalServerError

    def parse_lead_data(self, resp):
        if not resp:
            return
        soup = BeautifulSoup(resp, "lxml")
        obj = soup.find("div", attrs={"class": "card card-topic-lead s-pg16"})
        if not obj:
            return
        else:
            text = obj.find("p").text.split("导语：")[1].strip()
            return text

    def parse_hot_search_data(self, raw_data):
        if not raw_data:
            return None
        return_list, url_list = list(), list()
        data_obj = BeautifulSoup(raw_data, "lxml")
        try:
            data_list = data_obj.find_all("div", attrs={"id": "pl_top_realtimehot"})
            if not data_list:
                resp = self.parse_search_data(data_obj)
                return resp
            hot_list = data_list[0].find_all("tr")[1:]
            for raw in hot_list:
                len_num = len(raw.contents[3].contents)
                index = raw.contents[1].text.strip() if raw.contents[1].text.strip() else "置顶"
                keyword = raw.contents[3].contents[1].text
                is_crawl = 1 if self.search_keyword(keyword) else None
                search_num = 0 if len_num <= 3 else int(raw.contents[3].contents[3].text)
                mark = raw.contents[5].text.strip()
                r_url = raw.contents[3].contents[1].attrs.get("href")
                if "javascript:void(0);" in r_url:
                    w_url = "https://s.weibo.com" + raw.contents[3].contents[1].attrs.get("href_to")
                else:
                    w_url = "https://s.weibo.com" + raw.contents[3].contents[1].attrs.get("href")
                m2 = hashlib.md5()
                m2.update(keyword.encode("utf-8"))
                id = m2.hexdigest()
                time = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
                lead_text = self.get_lead_data(keyword)
                return_list = dict(
                    index=index,
                    id=id,
                    b_keyword=keyword,
                    result=[
                        dict(
                            heat=search_num,
                            time=time  # 爬取时间
                        )
                    ],
                    mark=mark,
                    w_url=w_url,
                    type="index_type",
                    text=keyword,
                    lead_text=lead_text if lead_text else "",
                    is_crawl=is_crawl
                )
                url_list.append(dict(url=w_url, keyword=keyword))
                self.save_one_data_to_es(HOT_SEARCH_WEIBO, return_list, id)
            return url_list
        except IndexError as e:
            logger.exception(e)
            raise RequestFailureError

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

    def parse_comment_data(self, data):
        """
        解析评论信息
        :param div_obj: 标签对象
        :return: dict
        """
        div_list, user_id_list, key_user_list = [], [], []
        try:
            user_id_list.append(data.get("user_id"))
            html_data = data.get("data")
            if isinstance(html_data, str):
                resp_obj = BeautifulSoup(html_data, "html.parser")
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
                    # comment_contents = "".join(div_obj.text.split("举报")[0].split(":")[1:])
                    comment_contents = comment[2].strip()
                else:
                    comment_contents = comment[1].strip(),  # 评论内容
                comment_id = div_obj.attrs.get("id").split("_")[1].strip()  # 评论id
                user_name = div_obj.find("a").text.strip(),  # 用户名
                le_list = div_obj.find("a").attrs.get("href").split("/"),  # 用户id
                user_id = le_list[0][1] if len(le_list[0]) == 2 else le_list[0][2]
                resp_dada = dict(
                    time=str_to_format_time(comment_time),  # 评论时间
                    platform=platform,  # 平台
                    contents="".join(comment_contents) if isinstance(comment_contents,
                                                                     tuple) else comment_contents,  # 评论内容
                    id=comment_id,  # 评论id
                    user_id=user_id,  # 用户id
                    user_name="".join(user_name) if isinstance(user_name, tuple) else user_name,  # 用户名
                    weibo_id=data.get("weibo_id"),  # 原微博id
                    type=data.get("type"),
                    like=comment_like,
                    key_user_id_list=key_user_list,
                    crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")
                )
                user_id_list.append(user_id)
                self.save_one_data_to_es(WEIBO_HOT_SEARCH, resp_dada, id=comment_id)
            return list(set(user_id_list))
        except Exception as e:
            return list(set(user_id_list))

    def parse_repost_data(self, data):
        """
        解析转发信息
        :param div_obj: 标签对象
        :return: dict
        """
        div_list, user_id_list, key_user_list = [], [], []
        try:
            user_id_list.append(data.get("user_id"))
            html_data = data.get("data")
            if isinstance(html_data, str):
                resp_obj = BeautifulSoup(html_data, "lxml")
                div_list = resp_obj.find_all("div", attrs={"class": "c"})[4:]
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
                repost_contents = "".join(div_obj.text.split("赞")[0].split(":")[1:]).strip(),  # 转发内容
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
                    time=str_to_format_time(repost_time),  # 转发时间
                    platform=platform,  # 平台
                    contents="".join(repost_contents).strip() if isinstance(repost_contents,
                                                                            tuple) else repost_contents,  # 转发内容
                    user_id=user_id,  # 用户id
                    user_name="".join(user_name) if isinstance(user_name, tuple) else user_name,  # 用户名
                    weibo_id=data.get("weibo_id"),  # 原微博id
                    type=data.get("type"),
                    like=repost_like,
                    key_user_id_list=key_user_list,
                    crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")
                )
                user_id_list.append(user_id)
                self.save_one_data_to_es(WEIBO_HOT_SEARCH, resp_dada, id=user_id)
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
            user_info, verified = {}, None
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
                tags=tags,  # 标签
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
                    gender = k.get("item_content")
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


if __name__ == "__main__":

    wb = WeiBoHotSpider()
    threads = []
    data_list, page_data_url_list = [], []
    html_list, wb_data_list = [], []
    weibo_detail_list, comment_or_repost_list = [], []
    com_or_re_data_list, user_id_list = [], []
    user_info_list = []

    url_list = wb.get_hot_search_list()
    for url_data in url_list:
        # 获取每条热搜页的html
        data_list.append(wb.get_weibo_page_data(url_data, ))
    threads = []
    if data_list:
        for data in data_list:
            # 解析每个热搜的所有页的url
            worker = WorkerThread(page_data_url_list, wb.parse_weibo_page_url, (data,))
            worker.start()
            threads.append(worker)
        for work in threads:
            work.join(1)
            if work.isAlive():
                logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
                threads.append(work)
        threads = []
    if page_data_url_list:
        for page_url_data in page_data_url_list:
            # 获取每页内容的html
            try:
                html_list.append(wb.get_weibo_page_data(page_url_data))
            except Exception as e:
                logger.exception(e)
                continue

    if html_list:
        for html_data in html_list:
            # 解析每页的20微博内容
            worker = WorkerThread(wb_data_list, wb.parse_weibo_html, (html_data,))
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
            try:
                wb.parse_weibo_detail(data, keyword)
            except Exception as e:
                logger.exception(e)
                continue
