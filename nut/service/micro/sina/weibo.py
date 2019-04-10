#! /usr/bin/python3
# -*- coding: utf-8 -*-

import time
import re
from service.core.utils.http_ import Requester
from service.exception import retry
from service.exception.exceptions import *
from service import logger
from service.micro.sina.list_task import save_pages_req_to_redis, save_pages_to_redis
from service.micro.utils import ua
from service.micro.utils.cookie_utils import dict_to_cookie_jar
from bs4 import BeautifulSoup
from service.db.utils.redis_utils import RedisClient


class WeiBoSpider(object):
    __name__ = 'Weibo kek word'

    def __init__(self, params, cookie=None):
        self.params = params
        self.headers = {
            'User-Agent': ua(),
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 's.weibo.com',
        }
        self.cookie = dict_to_cookie_jar(self.get_cookie())
        self.requester = Requester(cookie=self.cookie)

    def get_cookie(self):
        redis_cli = RedisClient('cookies', 'weibo')
        return redis_cli.return_choice_cookie()

    def next_cookie(self):
        cookie = dict_to_cookie_jar(self.get_cookie())
        self.requester = Requester(cookie=cookie)

    @retry(max_retries=3,
           exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError, ServiceUnavailableError
                       ), time_to_sleep=3)
    def run(self):
        """
        获取关键词列表！
        :return:
        """
        logger.info('Processing get weibo key word ！')
        url = "https://s.weibo.com/weibo?q=%s&typeall=1&suball=1&Refer=g" % (self.params)
        try:
            response = self.requester.get(url=url, header_dict=self.headers)
            if '微博搜索' in response.text and response.status_code == 200:
                page_url_list = self.get_page_url(response)
                #self.seperate_page(page_url_list)
                one_page = self.get_weibo_details(response)
            else:
                logger.error('get weibo hot search list failed !')
                raise HttpInternalServerError
        except Exception as e:
            self.next_cookie()
            raise HttpInternalServerError

    def seperate_page(self, page_list):
        """
        将为爬取的url存入redis中
        :param page_list: 所有页码的url列表
        :return:
        """
        if not page_list:
            return None
        list(map(lambda x: save_pages_to_redis(x), page_list))

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_weibo_details(self, response):
        """
        获取每页20条的微博详情,评论，转发
        :return:
        """
        data_list, comment_data, forward_data, original_weibo = [], [], [], None
        try:
            resp_obj = BeautifulSoup(response.text, 'html.parser')
            raw_data = resp_obj.find_all("div", attrs={"class": "card-wrap"})[:20]
            for raw in raw_data:
                comment_info_list, forward_info_list = [], []
                r_data = raw.contents[1]
                mid = raw.attrs.get("mid")  # 微博id
                is_forward = r_data.find_all("div", attrs={"class": "con"})  # 是否是转发微博
                if len(is_forward):
                    original_weibo = is_forward[0].text.strip()
                weibo = r_data.find_all("p", attrs={"class": "from"})[0]
                weibo_num = r_data.find_all("div", attrs={"class": "card-act"})[0].contents[1].find_all("li")[1:]
                com_num = self.comment_str_to_int(weibo_num[1].text)  # 判断是否有 评论
                forward_num = self.repost_str_to_int(weibo_num[0].text)  # 判断是否有 转发
                if com_num:
                    comment_url = self.parse_weibo_type_url(weibo, "comment")  # 评论url
                    comment_data = self.get_comment_user_data(comment_url, mid)
                    comment_info_list = comment_data.get("user_info")
                if forward_num:
                    forward_url = self.parse_weibo_type_url(weibo, "forward")  # 转发url
                    forward_data = self.get_forward_user_data(forward_url, mid)
                    forward_info_list = forward_data.get("user_info")
                raw_id = raw.contents[1].contents[1].contents[5].find_all("a", {"class": "name"})[0]
                content = r_data.find_all("p", attrs={"class": "txt"})
                contents = content[1].text.strip() if len(content) >= 2 else content[0].text.strip()
                user_id = raw_id.attrs.get("href").split("/")[3].split("?")[0]
                weibo_user_info = self.get_user_info(user_id)
                resp_dada = dict(
                    weibo_time=weibo.contents[1].text.strip(),  # 发微时间
                    platform=weibo.contents[3].text.strip() if len(weibo) > 3 else "",  # 平台
                    contents=contents,  # 内容
                    weibo_id=raw_id.text,  # 微博id
                    user_id=user_id,  # 用户id
                    like_num=self.comment_str_to_int(weibo_num[2].text),  # 点赞数
                    com_num=com_num,  # 评论数
                    forward_num=self.repost_str_to_int(weibo_num[0].text),  # 转发数
                    is_forward="是" if is_forward else "否",  # 是否转发
                    original_weibo=original_weibo,  # 转发原微博
                    comment=comment_data,  # 评论详情
                    forward=forward_data,  # 转发详情
                    weibo_user_info=weibo_user_info,  # 发微人的个人信息
                    user_info=comment_info_list + forward_info_list  # 评论人和转发人的信息
                )
                data_list.append(resp_dada)

            return data_list
        except Exception as e:
            pass

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_comment_user_data(self, url, mid):
        """
       获取评论信息
       :param url:
       :return:
       """
        page_data, page_user_id_list, user_id_list = [], [], []
        try:
            resp = self.requester.get(url).text
        except:
            raise HttpInternalServerError
        try:
            resp_obj = BeautifulSoup(resp, "html.parser")
            page_num = int(resp_obj.find("input", attrs={"name": "mp"}).attrs.get("value"))
            if page_num:
                page_data, page_user_id_list = self.get_more_comment_detail(page_num, url, mid)
            div_list = resp_obj.find_all("div", attrs={"id": True})[2:-1]
            comment_data, user_id_list = self.parse_comment_data(div_list, mid)
            data_list = page_data + comment_data
            user_info_list = self.get_other_user_info(page_user_id_list + user_id_list)
            return dict(comment=data_list, user_info=user_info_list)
        except Exception as e:
            return {}

    def get_other_user_info(self, user_list):
        """
        处理获取用户信息
        :param user_list:
        :return:
        """
        if not user_list:
            return
        user_info_list = [self.get_user_info(user_id) for user_id in user_list]
        return list(filter(None, user_info_list))

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_more_comment_detail(self, page, url, mid):
        """
        爬取根据page其他评论详情
        :param page: 页码
        :return:
        """
        data_list, user_list = [], []
        for i in range(2, (page + 1)):
            url = url + "&page={}".format(i)
            try:
                response = self.requester.get(url).text
                comment_data_list, user_id_list = self.parse_comment_data(response, mid)
                data_list.extend(comment_data_list), user_list.extend(user_id_list)
            except Exception as e:
                raise HttpInternalServerError
        return data_list, list(set(user_list))

    def get_forward_user_data(self, url, mid):
        """
        获取转发信息
        :param url:
        :return:
        """
        page_data, page_user_id_list, user_id_list = [], [], []
        try:
            resp = self.requester.get(url).text
        except:
            raise HttpInternalServerError
        try:
            resp_obj = BeautifulSoup(resp, "html.parser")
            page_num = int(resp_obj.find("input", attrs={"name": "mp"}).attrs.get("value"))
            if page_num:
                page_data, page_user_id_list = self.get_more_forward_detail(page_num, url, mid)
            div_list = resp_obj.find_all("div", attrs={"class": "c"})[3:]
            forward_data, user_id_list = self.parse_comment_data(div_list, mid)
            data_list = page_data + forward_data
            user_info_list = self.get_other_user_info(page_user_id_list + user_id_list)
            return dict(forward=data_list, user_info=user_info_list)
        except Exception as e:
            return {}

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_more_forward_detail(self, page, url, mid):
        """
        爬取根据page其他转发详情
        :param page: 页码
        :return:
        """
        data_list, user_list = [], []
        for i in range(2, (page + 1)):
            url = url + "&page={}".format(i)
            try:
                response = self.requester.get(url).text
                forward_data_list, user_id_list = self.parse_forward_data(response, mid)
                data_list.extend(forward_data_list), user_list.extend(user_id_list)
            except Exception as e:
                raise HttpInternalServerError
        return data_list, list(set(user_list))

    def parse_weibo_type_url(self, obj, _type):
        """
        :param obj: 标签对象
        :return: 评论url
        """
        flag_url = ""
        try:
            flag_url = obj.contents[1].attrs.get("href").split("?")[0].replace("om", "n")
        except:
            pass
        return "https:{}?type=comment".format(flag_url) if _type == "comment" else "https:{}?type=repost".format(
            flag_url)

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_page_contents(self, url):
        """
        :param url: 每页微博的url
        :return: html源码
        """
        if not url:
            return
        try:
            response = self.requester.get(url, header_dict=self.headers).text
            if "微博搜索" in response:
                return response
            else:
                raise HttpInternalServerError
        except Exception as e:
            raise e

    def get_page_url(self, html):
        """
        :param page_obj: 标签对象
        :return: 所有页码url
        """
        try:
            resp_obj = BeautifulSoup(html.text, 'html.parser')
            page_url_obj = resp_obj.find("span", attrs={"class": "list"})
            page_url_list = page_url_obj.find_all("li")[1:]
            url_list = ["https://s.weibo.com" + obj.contents[0].attrs.get("href") for obj in page_url_list]
            return url_list
        except Exception as e:
            raise e

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, ServiceUnavailableError), time_to_sleep=3)
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
            time.sleep(0.5)
            response = self.requester.get(url, header_dict=headers).json()
            if response.get("ok") == 1:
                user_data, containerid = self.parse_user_info(response.get("data", None))
                time.sleep(0.3)
                pro_url = "https://m.weibo.cn/api/container/getIndex?uid={}&type=uid&value={}" \
                          "&containerid={}".format(uid, uid, containerid)
                resp = self.requester.get(pro_url, header_dict=headers).json()
                profile_data = self.parse_profile_info(resp)
                return dict(user_data, **profile_data)

            else:
                return None
        except Exception as e:
            self.next_cookie()
            return None

    def parse_user_info(self, data):
        """
        解析个人信息
        :param data: json
        :param uid: 用户id
        :return:
        """
        try:
            user_info = {}
            fan_data = data.get("userInfo")
            con_id_list = data.get("tabsInfo").get("tabs")
            con_id = "".join([i.get("containerid") for i in con_id_list if i.get("tab_type") == "profile"])
            fan_count = fan_data.get("followers_count")  # 粉丝数
            follow_count = fan_data.get("follow_count")  # 关注数
            profile_image_url = fan_data.get("profile_image_url")  # 头像地址
            user_name = fan_data.get("screen_name")  # 用户名
            user_id = fan_data.get("id")  # 用户名
            container_id = con_id + "_-_INFO"
            user_info.update(
                user_id=user_id,
                fan_count=fan_count,
                follow_count=follow_count,
                profile_image_url=profile_image_url,
                user_name=user_name,
            )
            return user_info, container_id

        except Exception as e:
            return {}

    def parse_comment_data(self, data, mid):
        """
        解析评论信息
        :param div_obj: 标签对象
        :param mid: 微博 id
        :return: dict
        """
        try:
            div_list, comment_list, user_id_list = None, [], []
            if isinstance(data, list):
                div_list = data
            elif isinstance(data, str):
                resp_obj = BeautifulSoup(data, "html.parser")
                div_list = resp_obj.find_all("div", attrs={"id": True})[2:-1]
            for div_obj in div_list:
                if len(div_obj.contents) >= 11 and len(div_obj.contents) != 13:
                    if len(div_obj.contents) > 13:
                        comment_time = div_obj.contents[13].text.strip()[:-4].strip()  # 评论时间
                        platform = div_obj.contents[13].text.strip()[-4:].strip()  # 平台
                        comment_contents = div_obj.contents[5].text.strip(),  # 评论内容
                        comment_id = div_obj.contents[7].attrs.get("href").split("&")[0].split("=")[1].strip()  # 评论id
                    else:
                        comment_time = div_obj.contents[11].text.strip()[:-4].strip()
                        platform = div_obj.contents[11].text.strip()[-4:].strip()
                        comment_contents = div_obj.contents[3].text.strip(),  # 评论内容
                        comment_id = div_obj.contents[5].attrs.get("href").split("&")[0].split("=")[1].strip()
                    user_name = div_obj.contents[1].text.strip(),  # 用户名
                    le_list = div_obj.contents[1].attrs.get("href").split("/"),  # 用户id
                    user_id = le_list[0][1] if len(le_list[0]) == 2 else le_list[0][2]
                    resp_dada = dict(
                        comment_time=comment_time,  # 评论时间
                        platform=platform,  # 平台
                        comment_contents="".join(comment_contents) if isinstance(comment_contents,
                                                                                 tuple) else comment_contents,  # 评论内容
                        commet_id=comment_id,  # 评论id
                        user_id=user_id,  # 用户id
                        user_name="".join(user_name) if isinstance(user_name, tuple) else user_name,  # 用户名
                        mid=mid,  # 原微博id
                    )
                    user_id_list.append(user_id)
                    comment_list.append(resp_dada)
            return comment_list, list(set(user_id_list))
        except Exception as e:
            return [], []

    def parse_forward_data(self, data, mid):
        """
        解析转发信息
        :param div_obj: 标签对象
        :param mid: 微博 id
        :return: dict
        """
        try:
            div_list, forward_list, user_id_list = None, [], []
            if isinstance(data, list):
                div_list = data
            elif isinstance(data, str):
                resp_obj = BeautifulSoup(data, "html.parser")
                div_list = resp_obj.find_all("div", attrs={"class": "c"})[3:]
            for div_obj in div_list:
                if len(div_obj.contents) > 11:
                    _platform = div_obj.find("span", attrs={"class": "ct"}).text
                    forward_time = _platform.split("来自")[0].strip()  # 转发时间
                    platform = _platform.split("来自")[1].strip()  # 平台
                    forward_contents = div_obj.text,  # 转发内容
                    user_name = div_obj.contents[1].text.strip(),  # 用户名
                    le_list = div_obj.contents[1].attrs.get("href").split("/"),  # 用户id
                    user_id = le_list[0][1] if len(le_list[0]) == 2 else le_list[0][2]
                    resp_dada = dict(
                        forward_time=forward_time,  # 转发时间
                        platform=platform,  # 平台
                        forward_contents="".join(forward_contents) if isinstance(forward_contents,
                                                                                 tuple) else forward_contents,  # 转发内容
                        user_id=user_id,  # 用户id
                        user_name="".join(user_name) if isinstance(user_name, tuple) else user_name,  # 用户名
                        mid=mid,  # 原微博id
                    )
                    user_id_list.append(user_id)
                    forward_list.append(resp_dada)
            return forward_list, list(set(user_id_list))
        except Exception as e:
            return [], []

    def parse_profile_info(self, data):
        """
        解析简介，性别，所在地等等
        :param data: json
        :return:
        """
        if data.get("ok") == 0:
            return []
        resp_data = data.get("data").get("cards")[0:2]
        city, gender, introduction, grade, register_time, birthday = "", "", "", "", "", ""  # 所在地 性别 简介
        for i in resp_data:
            for k in i.get("card_group"):
                if k.get("item_name") == "简介":
                    introduction = k.get("item_content")
                elif k.get("item_name") == "性别":
                    gender = k.get("item_content")
                elif k.get("item_name") == "所在地":
                    city = k.get("item_content")
                elif k.get("item_name") == "等级":
                    grade = k.get("item_content")
                elif k.get("item_name") == "注册时间":
                    register_time = k.get("item_content")
                elif k.get("item_name") == "生日":
                    birthday = k.get("item_content")
        return dict(city=city, gender=gender, introduction=introduction, grade=grade, register_time=register_time,
                    birthday=birthday)

    def comment_str_to_int(self, _str):
        if _str.split(" ")[1].isdigit():
            return int(_str.split(" ")[1])
        return None

    def repost_str_to_int(self, _str):
        if _str.split(" ")[2].isdigit():
            return int(_str.split(" ")[2])
        return None

    def write_data_to_es(self, data):
        if not data:
            logger.error("weibo hot search not data !")


if __name__ == "__main__":
    wb = WeiBoSpider("检验员人好")
    url_list = wb.run()
    # url = wb.get_page_url(url_list)
    wb.seperate_page(url_list)
    # data = wb.get_user_info("2812335943")
