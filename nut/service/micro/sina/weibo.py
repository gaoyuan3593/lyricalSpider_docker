#! /usr/bin/python3
# -*- coding: utf-8 -*-
import datetime
import time
import re
from service.core.utils.http_ import Requester
from service.exception import retry
from service.exception.exceptions import *
from service import logger
from service.micro.sina.list_task import save_pages_to_redis, page_qq
from service.micro.utils import ua
from service.micro.utils.cookie_utils import dict_to_cookie_jar
from bs4 import BeautifulSoup
from service.db.utils.redis_utils import RedisClient
from service.micro.utils.threading_ import WorkerThread


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
        self.cookie = dict_to_cookie_jar(self.get_cookie())
        self.requester = Requester(cookie=self.cookie)

    def get_cookie(self):
        redis_cli = RedisClient('cookies', 'weibo')
        return redis_cli.return_choice_cookie()

    def next_cookie(self):
        cookie = dict_to_cookie_jar(self.get_cookie())
        self.requester = Requester(cookie=cookie)

    def get_redis_page_url(self):
        b_data = page_qq.get_nowait()
        if b_data:
            return b_data.decode("utf-8")
        return None

    def seperate_page(self, page_list, keyword):
        """
        将为爬取的url存入redis中
        :param page_list: 所有页码的url列表
        :return:
        """
        if not page_list:
            return None
        return list(map(lambda x: save_pages_to_redis(keyword, x), page_list))

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
                es.insert("weibo_keyword_details", "weibo_keyword", data)
        except Exception as e:
            pass

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def run(self):
        logger.info('Processing get weibo key word ！')
        try:
            url = "https://s.weibo.com/weibo?q=%s&typeall=1&suball=1&Refer=g" % (self.params)
            response = self.requester.get(url=url, header_dict=self.headers)
            page_url_list = self.parse_page_url(response)
            if page_url_list:
                return page_url_list
            raise HttpInternalServerError
        except Exception as e:
            self.next_cookie()
            raise HttpInternalServerError

    @retry(max_retries=5, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_home_page_data(self, url=None):
        """
        获取微博内容页
        :return:
        """
        logger.info('Processing get weibo key word ！')
        try:
            if not url:
                url = "https://s.weibo.com/weibo?q=%s&typeall=1&suball=1&Refer=g" % (self.params)
            response = self.requester.get(url=url, header_dict=self.headers)
            if '微博搜索' in response.text and response.status_code == 200:
                data_list = self.get_weibo_details(response.text)
                if data_list:
                    return data_list
                return None
            else:
                logger.error('get weibo detail failed !')
                raise HttpInternalServerError
        except Exception as e:
            self.next_cookie()
            raise HttpInternalServerError

    @retry(max_retries=5, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_weibo_page_data(self, url=None):
        """
        获取微博内容页
        :return:
        """
        logger.info('Processing get weibo key word ！')
        try:
            if not url:
                url = "https://s.weibo.com/weibo?q={}&typeall=1&suball=1&Refer=g".format(self.params)
            response = self.requester.get(url=url, header_dict=self.headers)
            if '微博搜索' in response.text and response.status_code == 200:
                return dict(data=response.text)
            else:
                logger.error('get weibo detail failed !')
                raise HttpInternalServerError
        except Exception as e:
            self.next_cookie()
            raise HttpInternalServerError

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_weibo_details(self, data):
        """
        获取每页20条的微博详情,评论，转发
        :return:
        """
        data_list, comment_data, forward_data, original_weibo = [], [], [], None
        if not data:
            return
        if isinstance(data, str):
            response = data
        else:
            response = data.get("data")
        try:
            resp_obj = BeautifulSoup(response, 'html.parser')
            raw_data = resp_obj.find_all("div", attrs={"class": "card-wrap"})[:20]
            for raw in raw_data:
                comment_info_list, forward_info_list = [], []
                r_data = raw.contents[1]
                mid = raw.attrs.get("mid")  # 微博id
                is_forward = r_data.find_all("div", attrs={"class": "con"})  # 是否是转发微博
                if len(is_forward):
                    original_weibo = is_forward[0].text.strip()
                weibo = r_data.find("p", attrs={"class": "from"})
                weibo_num = r_data.find_all("div", attrs={"class": "card-act"})[0].contents[1].find_all("li")[1:]
                com_num = self.comment_str_to_int(weibo_num[1].text)  # 判断是否有 评论
                forward_num = self.repost_str_to_int(weibo_num[0].text)  # 判断是否有 转发
                if com_num:
                    comment_url = self.parse_weibo_type_url(weibo, "comment")  # 评论url
                    comment_data = self.get_comment_user_data(comment_url, mid)
                    comment_info_list = comment_data.get("user_info", [])
                if forward_num:
                    forward_url = self.parse_weibo_type_url(weibo, "forward")  # 转发url
                    forward_data = self.get_forward_user_data(forward_url, mid)
                    forward_info_list = forward_data.get("user_info", [])
                raw_id = raw.contents[1].contents[1].contents[5].find_all("a", {"class": "name"})[0]
                content = r_data.find_all("p", attrs={"class": "txt"})
                contents = content[1].text.strip() if len(content) >= 2 else content[0].text.strip()
                user_id = raw_id.attrs.get("href").split("/")[3].split("?")[0]
                user_info_list = comment_info_list + forward_info_list
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
                    user_info=user_info_list,  # 评论人和转发人的信息
                    type="detail_type",
                    keyword=self.params
                )
                data_list.append(resp_dada)
            return data_list
        except Exception as e:
            logger.exception(e)
            return data_list

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_comment_user_data(self, url, mid):
        """
       获取评论信息
       :param url:
       :return:
       """
        page_data, page_user_id_list, user_id_list, user_info_list, threads, page_data_list = [], [], [], [], [], []
        headers = {
            "User-Agent": ua()
        }
        try:
            time.sleep(1)
            resp = self.requester.get(url, header_dict=headers).text
        except:
            raise HttpInternalServerError
        try:
            resp_obj = BeautifulSoup(resp, "html.parser")
            if not resp_obj.find("div", attrs={"id": "cmtfrm"}):
                raise HttpInternalServerError
            page_num_obj = resp_obj.find("input", attrs={"name": "mp"})
            if page_num_obj:
                page_num = int(page_num_obj.attrs.get("value"))
                if page_num >= 2:
                    for index in range(2, (page_num + 1)):
                        _url = url + "&page={}".format(index)
                        worker = WorkerThread(page_data_list, self.get_more_comment_detail, (_url, mid))
                        worker.start()
                    if page_data_list:
                        page_data = list(filter(None, [data.get("data") for data in page_data_list]))
                        page_id_list = list(filter(None, [data.get("user_list") for data in page_data_list]))
                        for i in page_id_list:
                            [page_user_id_list.append(k) for k in i]
            div_list = resp_obj.find_all("div", attrs={"id": True})[2:-1]
            comment_data, user_id_list = self.parse_comment_data(div_list, mid)
            data_list = page_data + comment_data
            if len(page_user_id_list + user_id_list) >= 10:
                for uid in list(set(page_user_id_list + user_id_list)):
                    worker = WorkerThread(user_info_list, self.get_user_info, (uid,))
                    worker.start()
                    threads.append(worker)
                for work in threads:
                    work.join(1)
                    if work.isAlive():
                        threads.append(work)
            else:
                user_info_list = self.get_other_user_info(page_user_id_list + user_id_list)
            return dict(comment=data_list, user_info=user_info_list if user_info_list else [])
        except Exception as e:
            self.next_cookie()
            raise e

    @retry(max_retries=5, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_more_comment_detail(self, url, mid):
        """
        爬取根据page其他评论详情
        :param page: 页码
        :return:
        """
        data_list, user_list = [], []
        headers = {
            "User-Agent": ua()
        }
        try:
            response = self.requester.get(url, header_dict=headers).text
            comment_data_list, user_id_list = self.parse_comment_data(response, mid)
            data_list.extend(comment_data_list), user_list.extend(user_id_list)
        except Exception as e:
            raise HttpInternalServerError
        return dict(data=data_list, user_list=list(set(user_list)))

    @retry(max_retries=5, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_forward_user_data(self, url, mid):
        """
        获取转发信息
        :param url:
        :return:
        """
        page_data, page_user_id_list, user_id_list, user_info_list, threads = [], [], [], [], []
        headers = {
            "User-Agent": ua()
        }
        try:
            resp = self.requester.get(url, header_dict=headers).text
        except:
            raise HttpInternalServerError
        try:
            resp_obj = BeautifulSoup(resp, "html.parser")
            page_num_obj = resp_obj.find("input", attrs={"name": "mp"})
            if page_num_obj:
                page_num = int(page_num_obj.attrs.get("value"))
                page_data, page_user_id_list = self.get_more_forward_detail(page_num, url, mid)
            div_list = resp_obj.find_all("div", attrs={"class": "c"})[3:]
            forward_data, user_id_list = self.parse_forward_data(div_list, mid)
            data_list = page_data + forward_data
            if len(page_user_id_list + user_id_list) >= 10:
                for uid in list(set(page_user_id_list + user_id_list)):
                    worker = WorkerThread(user_info_list, self.get_user_info, (uid,))
                    worker.start()
                    threads.append(worker)
                for work in threads:
                    work.join(1)
                    if work.isAlive():
                        threads.append(work)
            else:
                user_info_list = self.get_other_user_info(page_user_id_list + user_id_list)
            return dict(forward=data_list, user_info=user_info_list if user_info_list else [])
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
            headers = {
                "User-Agent": ua()
            }
            try:
                response = self.requester.get(url, header_dict=headers).text
                forward_data_list, user_id_list = self.parse_forward_data(response, mid)
                data_list.extend(forward_data_list), user_list.extend(user_id_list)
            except Exception as e:
                self.next_cookie()
                raise HttpInternalServerError
        return data_list, list(set(user_list))

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
            time.sleep(0.5)
            response = self.requester.get(url, header_dict=headers).json()
            if response.get("ok") == 1:
                user_data, containerid = self.parse_user_info(response.get("data", None))
                time.sleep(0.5)
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
            time.sleep(0.5)
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

    def parse_page_url(self, html):
        """
        :param page_obj: 标签对象
        :return: 所有页码url
        """
        try:
            resp_obj = BeautifulSoup(html.text, 'html.parser')
            page_url_obj = resp_obj.find("span", attrs={"class": "list"})
            page_url_list = page_url_obj.find_all("li")
            url_list = ["https://s.weibo.com" + obj.contents[0].attrs.get("href") for obj in page_url_list]
            return url_list
        except Exception as e:
            raise e

    def parse_user_info(self, data):
        """
        解析个人信息
        :param data: dict
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
                type="user_type"
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
                if len(div_obj.contents) >= 11:
                    _platform = div_obj.find("span", attrs={"class": "ct"}).text
                    comment_time = _platform.split("来自")[0].strip()  # 转发时间
                    platform = _platform.split("来自")[1].strip()  # 平台
                    comment_contents = div_obj.text.split("举报")[0].strip(),  # 评论内容
                    comment_id = div_obj.attrs.get("id").split("_")[1].strip()  # 评论id
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
                        type="comment_type"
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
                _platform = div_obj.find("span", attrs={"class": "ct"}).text
                forward_time = _platform.split("来自")[0].strip()  # 转发时间
                platform = _platform.split("来自")[1].strip()  # 平台
                forward_contents = div_obj.text.split("赞")[0].strip(),  # 转发内容
                if len(div_obj.contents) > 11:
                    user_name = div_obj.contents[1].text.strip(),  # 用户名
                    le_list = div_obj.contents[1].attrs.get("href").split("/"),  # 用户id
                    user_id = le_list[0][1] if len(le_list[0]) == 2 else le_list[0][2]
                else:
                    user_name = div_obj.contents[0].text.strip(),  # 用户名
                    le_list = div_obj.contents[0].attrs.get("href").split("/"),  # 用户id
                    user_id = le_list[0][1] if len(le_list[0]) == 2 else le_list[0][2]
                resp_dada = dict(
                    forward_time=forward_time,  # 转发时间
                    platform=platform,  # 平台
                    forward_contents="".join(forward_contents) if isinstance(forward_contents,
                                                                             tuple) else forward_contents,  # 转发内容
                    user_id=user_id,  # 用户id
                    user_name="".join(user_name) if isinstance(user_name, tuple) else user_name,  # 用户名
                    mid=mid,  # 原微博id
                    type="repost_type"
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
                    city = k.get("item_content")
                elif k.get("item_name") == "等级":
                    grade = k.get("item_content")
                elif k.get("item_name") == "注册时间":
                    sign_time = None if not k.get("item_content") else k.get("item_content")
                elif k.get("item_name") == "生日":
                    birthday = k.get("item_content")
        return dict(city=city, gender=gender, introduction=introduction, grade=grade, registration=sign_time,
                    birthday=birthday)

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

    def comment_str_to_int(self, _str):
        if _str.split(" ")[1].isdigit():
            return int(_str.split(" ")[1])
        return None

    def repost_str_to_int(self, _str):
        if _str.split(" ")[2].isdigit():
            return int(_str.split(" ")[2])
        return None

    def parse_url_to_split(self, _str):
        if _str:
            keyword, page_url = tuple(_str.split("|"))
            return keyword, page_url
        return None

    def write_data_to_es(self, data):
        if not data:
            logger.error("weibo hot search not data !")


if __name__ == "__main__":
    import threading

    wb = WeiBoSpider("检验员人好")
    # wb = WeiBoSpider("孙怡方否认怀二胎")
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # url_list = wb.run()
    resp = wb.get_home_page_data()
    wb.save_data_to_es(resp)

    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
