#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random
import time
import json
from bs4 import BeautifulSoup
from service.core.utils.http_ import Requester
from service.db.utils.redis_utils import RedisClient
from service.exception import retry
from service.exception.exceptions import *
from service import logger
from service.micro.utils import ua
from service.micro.utils.cookie_utils import dict_to_cookie_jar
from service.micro.utils.math_utils import str_to_format_time


class WeiBoHotSpider(object):
    __name__ = 'Weibo hot search'

    def __init__(self, cookie=None):
        self.cookie = dict_to_cookie_jar(self.get_cookie())
        self.requester = Requester(cookie=self.cookie)
        self.headers = {
            'User-Agent': ua(),
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 's.weibo.com'
        }

    def get_cookie(self):
        redis_cli = RedisClient('cookies', 'weibo')
        return redis_cli.return_choice_cookie()

    def next_cookie(self):
        cookie = dict_to_cookie_jar(self.get_cookie())
        self.requester = Requester(cookie=cookie)

    def random_num(self):
        return random.uniform(1, 3)

    def save_data_to_es(self, data_list):
        """
        将为爬取的数据存入es中
        :param data_list: 数据
        :return:
        """
        try:
            from service.db.utils.elasticsearch_utils import ElasticsearchClient
            es = ElasticsearchClient()
            for data in data_list:
                mapping = {
                    "query": {
                        "bool":
                            {
                                "must":
                                    [{
                                        "term": {"b_keyword.keyword": data.get("b_keyword")}}],
                                "must_not": [],
                                "should": []}},
                    "sort": [],
                    "aggs": {}
                }
                result = es.dsl_search('weibo_hot_seach_details', "detail_type", mapping)
                result = json.loads(result)
                if not result.get("took"):
                    es.insert("weibo_hot_seach_details", data.get("type"), data)
                    logger.info(" save to es success ！")
        except Exception as e:
            raise e

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_hot_search_list(self):
        logger.info('Processing get weibo hot search list!')
        url = 'https://s.weibo.com/top/summary?Refer=top_hot'
        headers = {
            'User-Agent': ua(),
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 's.weibo.com'
        }
        try:
            response = self.requester.get(url=url, header_dict=headers)
            if '热搜榜' in response.text and response.status_code == 200:
                data_list, url_list = self.parse_hot_search_data(response.text)
                return data_list, url_list
            else:
                logger.error('get weibo hot search list failed !')
                raise HttpInternalServerError
        except Exception as e:
            raise RequestFailureError

    @retry(max_retries=5, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
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
            response = self.requester.get(url=url, header_dict=self.headers)
            if '微博搜索' in response.text and "下一页":
                return dict(data=response.text, keyword=data.get("keyword"))
            else:
                logger.error('get weibo detail failed !')
                raise HttpInternalServerError
        except Exception as e:
            if e.args:
                self.next_cookie()
                raise HttpInternalServerError
            else:
                return {}

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
                return dict(data=raw_data, keyword=data.get("keyword"))
            return {}
        except Exception as e:
            logger.exception(e)
            return {}

    def parse_weibo_page_url(self, data):
        """
        解析当前热搜的所有页的uel
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
                    return url_list
            return []
        except Exception as e:
            logger.exception(e)
            return []

    def parse_weibo_detail(self, tag_obj, keyword):
        if not tag_obj:
            return {}
        try:
            is_forward_weibo_id, key_user_list, forward_user_url_list = None, [], []
            mid = tag_obj.attrs.get("mid")  # 微博id
            is_forward = tag_obj.find_all("div", attrs={"class": "con"})  # 是否是转发微博
            if len(is_forward):
                is_forward_weibo_id = \
                    is_forward[0].find("p", {"class": "from"}).find("a").attrs.get("href").split("?")[0].replace(
                        "om",
                        "n").split(
                        "cn/")[1].split("/")[1]
            weibo = tag_obj.find("p", attrs={"class": "from"})
            weibo_num = tag_obj.find_all("div", attrs={"class": "card-act"})[0].contents[1].find_all("li")[
                        1:]  # 评论，转发，赞
            raw_id = tag_obj.find("a", {"class": "name", "suda-data": True})
            content = tag_obj.find_all("p", attrs={"class": "txt"})
            if len(content) == 2:
                contents = content[1].text.strip()
            else:
                contents = content[0].text.strip()
            user_key_list = content[0].find_all("a")
            key_user_data = self.parse_key_user_list(user_key_list)  # 获取@用户id
            if key_user_data:
                key_user_list = key_user_data
            user_id = raw_id.attrs.get("href").split("/")[3].split("?")[0]
            weio_id = \
                weibo.contents[1].attrs.get("href").split("?")[0].replace("om", "n").split("cn/")[1].split("/")[1]
            if "//@" in contents:
                forward_user_url_list = self.parse_forward_user_list(weio_id, user_id)  # 解析转发用户链列表
            weibo_time = weibo.contents[1].text.strip()
            if "转赞" in weibo_time:
                weibo_time = weibo_time.split("转赞")[0].strip()
            resp_dada = dict(
                weibo_time=str_to_format_time(weibo_time),  # 发微时间
                platform=weibo.contents[3].text.strip() if len(weibo) > 3 else "",  # 平台
                contents=contents,  # 内容
                weibo_id=weio_id,  # 微博id
                mid=mid,  # 微博id
                user_id=user_id,  # 用户id
                like_num=self.comment_str_to_int(weibo_num[2].text),  # 点赞数
                com_num=self.comment_str_to_int(weibo_num[1].text),  # 评论数
                repost_num=self.repost_str_to_int(weibo_num[0].text),  # 转发数
                is_forward="是" if is_forward else "否",  # 是否转发
                is_forward_weibo_id=is_forward_weibo_id,  # 转发原微博id
                type="detail_type",
                key_user_list=key_user_list,
                forward_user_url_list=forward_user_url_list,
                b_keyword=keyword
            )
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
            if "首页" in resp and "消息" in resp:
                return dict(data=resp, type="comment_type", weibo_id=weibo_id, user_id=user_id)
        except Exception as e:
            if e.args:
                self.next_cookie()
                raise HttpInternalServerError
            return {}

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
            if "首页" in resp and "消息" in resp:
                return dict(data=resp, type="repost_type", weibo_id=weibo_id, user_id=user_id)
        except Exception as e:
            if e.args:
                self.next_cookie()
                raise HttpInternalServerError
            return {}

    @retry(max_retries=5, exceptions=(HttpInternalServerError, TimedOutError, ServiceUnavailableError), time_to_sleep=3)
    def get_user_info(self, uid):
        """
        获取个人信息
        :param uid: 用户id
        :return: dict
        """
        url = "https://m.weibo.cn/api/container/getIndex?uid={}&type=uid&value={}".format(uid, uid)
        headers = {
            "User-Agent": ua()
        }
        try:
            random_time = self.random_num()
            time.sleep(random_time)
            response = self.requester.get(url, header_dict=headers).json()
            if response.get("ok") == 1:
                user_data, containerid = self.parse_user_info(response.get("data", None))
                profile_data = self.get_profile_user_info(uid, containerid)
                return dict(user_data, **profile_data)
            else:
                return {}
        except Exception as e:
            self.next_cookie()
            raise HttpInternalServerError

    @retry(max_retries=5, exceptions=(HttpInternalServerError, TimedOutError, ServiceUnavailableError), time_to_sleep=3)
    def get_profile_user_info(self, uid, containerid):
        """
        获取个人详细信息信息
        :param uid: 用户id
        :return: dict
        """
        try:
            headers = {
                "User-Agent": ua()
            }
            random_time = self.random_num()
            time.sleep(random_time)
            pro_url = "https://m.weibo.cn/api/container/getIndex?uid={}&type=uid&value={}" \
                      "&containerid={}".format(uid, uid, containerid)

            response = self.requester.get(pro_url, header_dict=headers).json()
            if response.get("ok") == 1:
                profile_data = self.parse_profile_info(response)
                return profile_data
            else:
                return {}
        except Exception as e:
            self.next_cookie()
            raise HttpInternalServerError

    def parse_search_data(self, obj):
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

    def parse_comment_or_repost_url(self, data_list):
        comment_url_list, repost_url_list = list(), list()
        try:
            for data in data_list:
                comment_num = data.get("com_num")
                weibo_id = data.get("weibo_id")
                user_id = data.get("user_id")
                repost_num = data.get("repost_num")
                if comment_num:
                    comment_url_list.append(dict(user_id=user_id, weibo_id=weibo_id, url_list=[
                        "https://weibo.cn/comment/{}?&uid={}&page={}".format(weibo_id, user_id, i) for i in
                        range(1, (comment_num + 1))]))
                if repost_num:
                    repost_url_list.append(dict(user_id=user_id, weibo_id=weibo_id, url_list=[
                        "https://weibo.cn/repost/{}?uid={}&page={}".format(weibo_id, user_id, i) for i in
                        range(1, (repost_num + 1))]))
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
                    url = "https://weibo.cn" + i.get("href").split("com")[1]
                else:
                    url = "https://weibo.cn" + i.get("href")
                headers = {
                    "User-Agent": ua()
                }
                try:
                    user_resp = self.requester.get(url, header_dict=headers).text
                except Exception as e:
                    self.next_cookie()
                    raise HttpInternalServerError
                try:
                    resp_obj = BeautifulSoup(user_resp, "html.parser")
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
                    return list(set(user_id_list))
        return list(set(user_id_list))

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
                search_num = "无" if len_num <= 3 else raw.contents[3].contents[3].text
                mark = raw.contents[5].text.strip()
                r_url = raw.contents[3].contents[1].attrs.get("href")
                if "javascript:void(0);" in r_url:
                    w_url = "https://s.weibo.com" + raw.contents[3].contents[1].attrs.get("href_to")
                else:
                    w_url = "https://s.weibo.com" + raw.contents[3].contents[1].attrs.get("href")
                return_list.append({keyword: dict(
                    index=index,
                    keyword=keyword,
                    search_num=search_num,
                    mark=mark,
                    w_url=w_url
                )})
                url_list.append(dict(url=w_url, keyword=keyword))

            return return_list, url_list
        except IndexError as e:
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

    @retry(max_retries=5, exceptions=(HttpInternalServerError, TimedOutError, ServiceUnavailableError), time_to_sleep=3)
    def parse_forward_user_list(self, w_id, u_id):
        """
        返回转发用户链的 用户id列表
        :param w_id: 微博id
        :param u_id: 用户id
        :return: list
        """
        forward_user_url = "https://weibo.cn/comment/{}?uid={}".format(w_id, u_id)
        user_id_list = []
        headers = {
            "User-Agent": ua()
        }
        try:
            user_resp = self.requester.get(forward_user_url, header_dict=headers).text
            if "首页" not in user_resp:
                raise HttpInternalServerError
        except Exception as e:
            self.next_cookie()
            raise HttpInternalServerError
        try:
            url_list = user_resp.split('//<a href="')
            forward_user_url_list = ["https://weibo.cn" + url.split('">')[0] for url in url_list if
                                     url.startswith("/n/")]
        except Exception as e:
            return []
        for url in forward_user_url_list:
            try:
                resp = self.requester.get(url, header_dict=headers).text
            except Exception as e:
                self.next_cookie()
                raise HttpInternalServerError
            try:
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
                return list(set(user_id_list))
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
        try:
            html_data = data.get("data")
            div_list, comment_list, user_id_list, key_user_list = None, [], [], []
            if isinstance(html_data, str):
                resp_obj = BeautifulSoup(html_data, "html.parser")
                div_list = resp_obj.find_all("div", attrs={"id": True})[2:-1]
            for div_obj in div_list:
                if len(div_obj.contents) >= 11:
                    key_user = div_obj.find_all("a")
                    _data = self.parse_key_user_list(key_user)
                    if _data:
                        key_user_list = _data
                    _platform = div_obj.find("span", attrs={"class": "ct"}).text
                    comment_time = _platform.split("来自")[0].strip()  # 评论时间
                    platform = _platform.split("来自")[1].strip()  # 平台
                    comment_contents = div_obj.text.split("举报")[0].strip(),  # 评论内容
                    comment_id = div_obj.attrs.get("id").split("_")[1].strip()  # 评论id
                    user_name = div_obj.contents[1].text.strip(),  # 用户名
                    le_list = div_obj.contents[1].attrs.get("href").split("/"),  # 用户id
                    user_id = le_list[0][1] if len(le_list[0]) == 2 else le_list[0][2]
                    resp_dada = dict(
                        comment_time=str_to_format_time(comment_time),  # 评论时间
                        platform=platform,  # 平台
                        comment_contents="".join(comment_contents) if isinstance(comment_contents,
                                                                                 tuple) else comment_contents,  # 评论内容
                        commet_id=comment_id,  # 评论id
                        user_id=user_id,  # 用户id
                        user_name="".join(user_name) if isinstance(user_name, tuple) else user_name,  # 用户名
                        weibo_id=data.get("weibo_id"),  # 原微博id
                        type=data.get("type"),
                        key_user_list=key_user_list
                    )
                    user_id_list.append(user_id)
                    comment_list.append(resp_dada)
            return comment_list, list(set(user_id_list))
        except Exception as e:
            return [], []

    def parse_repost_data(self, data):
        """
        解析转发信息
        :param div_obj: 标签对象
        :return: dict
        """
        html_data = data.get("data")
        try:
            div_list, repost_list, user_id_list, key_user_list = None, [], [], []
            if isinstance(html_data, str):
                resp_obj = BeautifulSoup(html_data, "html.parser")
                div_list = resp_obj.find_all("div", attrs={"class": "c"})[3:]
            for div_obj in div_list:
                _platform = div_obj.find("span", attrs={"class": "ct"}).text
                repost_time = _platform.split("来自")[0].strip()  # 转发时间
                platform = _platform.split("来自")[1].strip()  # 平台
                repost_contents = div_obj.text.split("赞")[0].strip(),  # 转发内容
                if len(div_obj.contents) > 11:
                    user_name = div_obj.contents[1].text.strip(),  # 用户名
                    le_list = div_obj.contents[1].attrs.get("href").split("/"),  # 用户id
                    user_id = le_list[0][1] if len(le_list[0]) == 2 else le_list[0][2]
                else:
                    user_name = div_obj.contents[0].text.strip(),  # 用户名
                    le_list = div_obj.contents[0].attrs.get("href").split("/"),  # 用户id
                    user_id = le_list[0][1] if len(le_list[0]) == 2 else le_list[0][2]
                key_user = div_obj.find_all("a")
                _data = self.parse_key_user_list(key_user)
                if _data:
                    key_user_list = _data
                resp_dada = dict(
                    repost_time=str_to_format_time(repost_time),  # 转发时间
                    platform=platform,  # 平台
                    repost_contents="".join(repost_contents) if isinstance(repost_contents,
                                                                           tuple) else repost_contents,  # 转发内容
                    user_id=user_id,  # 用户id
                    user_name="".join(user_name) if isinstance(user_name, tuple) else user_name,  # 用户名
                    weibo_id=data.get("weibo_id"),  # 原微博id
                    type=data.get("type"),
                    key_user_list=key_user_list
                )
                user_id_list.append(user_id)
                repost_list.append(resp_dada)
            return repost_list, list(set(user_id_list))
        except Exception as e:
            return [], []

    def parse_user_info(self, data):
        """
        解析个人信息
        :param data: dict
        :param uid: 用户id
        :return:
        """
        try:
            user_info, verified = {}, "无"
            fan_data = data.get("userInfo")
            con_id_list = data.get("tabsInfo").get("tabs")
            con_id = "".join([i.get("containerid") for i in con_id_list if i.get("tab_type") == "profile"])
            fan_count = fan_data.get("followers_count")  # 粉丝数
            follow_count = fan_data.get("follow_count")  # 关注数
            profile_image_url = fan_data.get("profile_image_url")  # 头像地址
            user_name = fan_data.get("screen_name")  # 用户名
            user_id = fan_data.get("id")  # 用户名
            container_id = con_id + "_-_INFO"
            verified_type = fan_data.get("verified_type")
            if verified_type == 0:
                verified = "yellow"
            elif verified_type == 1 or verified_type == 3:
                verified = "blue"
            user_info.update(
                user_id=user_id,
                fan_count=fan_count,
                follow_count=follow_count,
                profile_image_url=profile_image_url,
                user_name=user_name,
                verified=verified,
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
        city, gender, introduction, grade, sign_time, birthday = "", "", "", "", None, ""  # 所在地 性别 简介
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


if __name__ == "__main__":
    from service.micro.utils.threading_ import WorkerThread

    wb = WeiBoHotSpider()
    threads = []
    data_list, page_data_url_list = [], []
    html_list, wb_data_list = [], []
    weibo_detail_list, comment_or_repost_list = [], []
    com_or_re_data_list, user_id_list = [], []
    user_info_list = []

    resp, url_list = wb.get_hot_search_list()
    for url_data in url_list:
        # 获取每条热搜页的html
        worker = WorkerThread(data_list, wb.get_weibo_page_data, (url_data,))
        worker.start()
        threads.append(worker)
    for work in threads:
        work.join()
    threads = []
    if data_list:
        for data in data_list:
            # 解析每个热搜的所有页的url
            page_data_url_list.extend(wb.parse_weibo_page_url(data))
    if page_data_url_list:
        for page_url_data in page_data_url_list:
            # 获取每页内容的html
            worker = WorkerThread(html_list, wb.get_weibo_page_data, (page_url_data,))
            worker.start()
            threads.append(worker)
        for work in threads:
            work.join()
        threads = []
    if html_list:
        for html_data in html_list:
            # 解析每页的20微博内容
            worker = WorkerThread(wb_data_list, wb.parse_weibo_html, (html_data,))
            worker.start()
            threads.append(worker)
        for work in threads:
            work.join()
        threads = []
    for wb_data in wb_data_list:
        # 解析微博详情
        if not wb_data:
            continue
        keyword = wb_data.get("keyword")
        for data in wb_data.get("data"):
            worker = WorkerThread(weibo_detail_list, wb.parse_weibo_detail, (data, keyword))
            worker.start()
            threads.append(worker)
        for work in threads:
            work.join()
        threads = []

    # 发布微博的信息存入es
    wb.save_data_to_es(list(filter(None, weibo_detail_list)))

    comment_url_list, repost_url_list = wb.parse_comment_or_repost_url(weibo_detail_list)

    if comment_url_list or repost_url_list:
        for data in comment_url_list:  # 所有评论url
            weibo_id = data.get("weibo_id")
            user_id = data.get("user_id")
            for url in data.get("url_list"):
                worker = WorkerThread(comment_or_repost_list, wb.get_comment_data, (url, weibo_id, user_id))
                worker.start()
                threads.append(worker)
            for work in threads:
                work.join()
            threads = []
        for data in repost_url_list:  # 所有转发url
            weibo_id = data.get("weibo_id")
            user_id = data.get("user_id")
            for url in data.get("url_list"):
                worker = WorkerThread(comment_or_repost_list, wb.get_repost_data, (url, weibo_id, user_id))
                worker.start()
                threads.append(worker)
            for work in threads:
                work.join()
            threads = []
    # 解析所有评论和转发信息，评论和转发用户ld列表
    for data in comment_or_repost_list:
        if not data:
            continue
        if data.get("type") == "comment_type":
            comment_data_list, comment_user_id_list = wb.parse_comment_data(data)
            com_or_re_data_list.extend(comment_data_list)
            user_id_list.extend(comment_user_id_list)
        elif data.get("type") == "repost_type":
            repost_data_list, repost_user_id_list = wb.parse_repost_data(data)
            com_or_re_data_list.extend(repost_data_list)
            user_id_list.extend(repost_user_id_list)
    # 评论和转发信息存入es
    wb.save_data_to_es(com_or_re_data_list)

    # 获取用户个人信息
    for uid in user_id_list:
        worker = WorkerThread(user_info_list, wb.get_user_info, (uid,))
        worker.start()
        threads.append(worker)
    for work in threads:
        work.join()
    threads = []
    # y用户信息存入es
    wb.save_data_to_es(user_info_list)
