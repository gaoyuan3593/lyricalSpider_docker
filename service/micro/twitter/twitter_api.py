#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random
import time
import json
import threadpool

from urllib import parse

from bs4 import BeautifulSoup
from service.core.utils.http_ import Requester
from service.exception import retry
from service.exception.exceptions import *
from service import logger
from service.micro.utils import ua
from service.micro.utils.cookie_utils import dict_to_cookie_jar, cookie_jar_to_dict
from service.micro.utils.math_utils import str_to_format_time
from service.micro.utils.threading_ import WorkerThread
from service.db.utils.elasticsearch_utils import es_client
from datetime import datetime
from service.micro.utils.threading_ import WorkerThread


class TwitterSpider(object):
    __name__ = 'Twitter Spider'

    def __init__(self, keyword):
        self.keyword = keyword
        self.requester = Requester(timeout=15)
        self.es_name = "twitter_{}".format(self.keyword).lower()
        self.es = es_client

    def random_num(self):
        return random.uniform(0.1, 1)

    def update_cookie(self, cookie):
        cookie = cookie_jar_to_dict(cookie)
        cookies_obj = dict_to_cookie_jar(json.dumps(cookie))
        self.requester = Requester(cookie=cookies_obj, timeout=15)

    def filter_keyword(self, _type, _dic, data=None):
        mapping = {
            "query": {
                "bool":
                    {
                        "must":
                            [{
                                "term": _dic}],
                        "must_not": [],
                        "should": []}},
            "sort": [],
            "aggs": {}
        }
        try:
            result = self.es.dsl_search("test", _type, mapping)
            if result.get("hits").get("hits"):
                if _type == "detail_type":
                    self.es.update("test", _type, result.get("hits").get("hits")[0].get("_id"), data)
                    logger.info("data : {}, update success".format(data))
                    return True
                else:
                    logger.info("dic : {} is existed".format(_dic))
                    return True
            return False
        except Exception as e:
            return False

    def save_one_data_to_es(self, data, dic):
        """
        将为爬取的数据存入es中
        :param data_list: 数据
        :return:
        """
        try:
            _type = data.get("type")
            if self.filter_keyword(_type, dic, data):
                logger.info("is existed  dic: {}".format(dic))
                return
            self.es.insert("test", _type, data)
            logger.info(" save to es success data= {}！".format(data))
        except Exception as e:
            raise e

    @retry(max_retries=7, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_twitter_page_data(self):
        """
        获取推特的人物首页
        :return: dict
        """
        logger.info('Processing get weibo key word ！')
        url = "https://twitter.com/{}".format(self.keyword)
        headers = {
            'user-Agent': ua(),
            'connection': 'keep-alive',
            "content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-Encoding': 'gzip, deflate',
        }

        try:
            resp = self.requester.get(url, header_dict=headers)
            # print(cookie_jar_to_dict(resp.cookies))
            self.update_cookie(resp.cookies)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, "html")
                data_table = soup.find_all("li", attrs={"class": "js-stream-item stream-item stream-item "})
                data_min_position = soup.find("div", attrs={"class": "stream-container"}).attrs.get("data-min-position")
                twitter_count = int(soup.find("span", attrs={"class": "ProfileNav-value"}).attrs.get("data-count"))
                if not data_table:
                    raise HttpInternalServerError
                logger.info("get twitter page data sussess！！！！ ")
                dic = dict(twitter_count=twitter_count, data_min_position=data_min_position, items_html=resp.text)
                return dic
            else:
                raise HttpInternalServerError
        except Exception as e:
            self.requester.use_proxy()
            raise HttpInternalServerError

    def parse_page_data(self, data_dic):
        if not data_dic:
            return
        data_list = []
        is_twitter = ""
        resp = data_dic.get("items_html")
        if not data_dic.get("twitter_count"):
            resp = self.add_body_tag(resp)
        soup = BeautifulSoup(resp, "html")
        data_table = soup.find_all("li", attrs={"class": "js-stream-item stream-item stream-item "})
        for tag in data_table:
            try:
                twitter_id = tag.attrs.get("data-item-id")  # 推特id
                profile_tweet_url = "https://twitter.com" + tag.find("a", attrs={
                    "class": "tweet-timestamp js-permalink js-nav js-tooltip"}).attrs.get(
                    "href")  # 回复的url + ?conversation_id={}
                like_soup = tag.find_all("span", attrs={"class": "ProfileTweet-actionCount"})[:3]
                is_retweeted = tag.find("span", attrs={"class": "js-retweet-text"})  # 是否是转推
                if is_retweeted:
                    is_twitter = 1
                twitter_user = tag.find("div", attrs={"class": "stream-item-header"}).find("strong", attrs={
                    "class": "fullname show-popup-with-id u-textTruncate "}).text
                text = tag.find("div", attrs={"class": "js-tweet-text-container"}).text.strip()  # 内容
                try:
                    date = tag.find("div", attrs={"class": "stream-item-header"}).find("span", attrs={
                        "class": "_timestamp js-short-timestamp "})  # # 发推时间戳
                    if not date:
                        date = tag.find("div", attrs={"class": "stream-item-header"}).find("span", attrs={
                            "class": "_timestamp js-short-timestamp js-relative-timestamp"})
                    _twitter_date = date.attrs.get("data-time")
                    twitter_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(_twitter_date)))  # 发推时间
                except:
                    twitter_date = ""
                comment_num = like_soup[0].attrs.get("data-tweet-stat-count")  # 评论数
                repost_num = like_soup[1].attrs.get("data-tweet-stat-count")  # 转发数
                like_num = like_soup[2].attrs.get("data-tweet-stat-count")  # 点赞数
                resp_dada = dict(twitter_user=twitter_user, twitter_date=twitter_date, text=text,
                                 comment_num=comment_num,
                                 repost_num=repost_num, type="detail_type", profile_tweet_url=profile_tweet_url,
                                 like_num=like_num, is_twitter=is_twitter, twitter_id=twitter_id)
                data_list.append(resp_dada)
                dic = {"twitter_id.keyword": twitter_id}
                self.save_one_data_to_es(resp_dada, dic)
            except Exception as e:
                continue

        return data_list

    def parse_comment_data(self, data_dic):
        if not data_dic:
            return
        if data_dic.get("flag"):
            soup = BeautifulSoup(data_dic.get("items_html"), "html")
            data_table = soup.find_all("li", attrs={"class": "js-stream-item stream-item stream-item "})
        else:
            data_table = data_dic.get("tag")
        for tag in data_table:
            try:
                comment_id = tag.attrs.get("data-item-id")  # 推特id
                like_soup = tag.find_all("span", attrs={"class": "ProfileTweet-actionCount"})[:3]
                twitter_user = tag.find("div", attrs={"class": "stream-item-header"}).find("strong", attrs={
                    "class": "fullname show-popup-with-id u-textTruncate "}).text
                text = tag.find("div", attrs={"class": "js-tweet-text-container"}).text.strip()  # 内容
                try:
                    date = tag.find("div", attrs={"class": "stream-item-header"}).find("span", attrs={
                        "class": "_timestamp js-short-timestamp "})  # # 发推时间戳
                    if not date:
                        date = tag.find("div", attrs={"class": "stream-item-header"}).find("span", attrs={
                            "class": "_timestamp js-short-timestamp js-relative-timestamp"})
                    _twitter_date = date.attrs.get("data-time")
                    comment_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(_twitter_date)))  # 评论时间
                except:
                    comment_date = ""
                comment_num = like_soup[0].attrs.get("data-tweet-stat-count")  # 评论数
                repost_num = like_soup[1].attrs.get("data-tweet-stat-count")  # 转发数
                like_num = like_soup[2].attrs.get("data-tweet-stat-count")  # 点赞数
                resp_dada = dict(twitter_user=twitter_user, comment_date=comment_date, text=text,
                                 comment_num=comment_num,
                                 repost_num=repost_num, type="comment_type",
                                 like_num=like_num, twitter_id=data_dic.get("twitter_id"), comment_id=comment_id)
                dic = {"comment_id.keyword": comment_id}
                self.save_one_data_to_es(resp_dada, dic)
            except Exception as e:
                continue

    @retry(max_retries=7, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_twitter_data(self, data_min_position):
        url = "https://twitter.com/i/profiles/show/{}/timeline/tweets?include_available_features=1&include_entities=1&max_position={}&reset_error_state=false".format(
            self.keyword, data_min_position)
        headers = {
            'user-Agent': ua(),
            'connection': 'keep-alive',
            "content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-Encoding': 'gzip, deflate',
        }
        try:
            resp = self.requester.get(url, header_dict=headers)
            if resp.status_code == 200:
                resp_dic = resp.json()
                return resp_dic
        except Exception as e:
            self.requester.use_proxy()
            raise HttpInternalServerError

    @retry(max_retries=7, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_comment_data(self, data_min_position, twitter_id):
        url = "https://twitter.com/i/{}/conversation/{}?include_available_features=1&include_entities=1&max_position={}&reset_error_state=false".format(
            self.keyword, twitter_id, data_min_position)
        headers = {
            'user-Agent': ua(),
            'connection': 'keep-alive',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-encoding': 'gzip, deflate',
            'x-overlay-request': "true",
            'x-previous-page-name': 'profile',
            'x-requested-with': 'XMLHttpRequest',
            'x-twitter-active-user': 'yes'
        }
        try:
            resp = self.requester.get(url, header_dict=headers)
            if resp.status_code == 200:
                resp_dic = resp.json()
                soup = BeautifulSoup(resp_dic.get("items_html"), "html")
                flag_tag = soup.find_all("li", attrs={"class": "js-stream-item stream-item stream-item "})
                if flag_tag:
                    return dict(tag=flag_tag, twitter_id=twitter_id)
        except Exception as e:
            self.requester.use_proxy()
            raise HttpInternalServerError

    @retry(max_retries=4, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=1)
    def get_profile_tweet_data(self, url, twitter_id):

        headers = {
            'user-Agent': ua(),
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-Encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9'
        }
        try:
            resp = self.requester.get(url, header_dict=headers)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, "html")
                data_min_position = soup.find("div", attrs={"class": "stream-container"}).attrs.get("data-min-position")
                flag_tag = soup.find_all("li", attrs={"class": "js-stream-item stream-item stream-item "})
                if flag_tag:
                    return dict(resp=resp.text, data_min_position=data_min_position, twitter_id=twitter_id)
            else:
                raise HttpInternalServerError
        except Exception as e:
            self.requester.use_proxy()
            raise HttpInternalServerError

    def add_body_tag(self, resp):
        _str = """
            <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
            <html xmlns="http://www.w3.org/1999/xhtml">
            <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <title>Fake Title</title>
            <body>
                {}
            </body>
            </head>
            </html>
            """.format(resp)
        return _str


if __name__ == '__main__':
    twitter = TwitterSpider("realDonaldTrump")
    # twitter = TwitterSpider("SecPompeo")
    # twitter = TwitterSpider("gaoyuan12322138")

    twitter_data_list, threads = [], []
    parse_data_list, profile_tweet_data_list = [], []
    comment_list = []
    one_data = twitter.get_twitter_page_data()
    twitter_count = one_data.get("twitter_count")
    data_min_position = one_data.get("data_min_position")
    page = twitter_count // 20 + 1
    for i in range(1, page):
        # 获取推特的html
        try:
            raw_data = twitter.get_twitter_data(data_min_position)
            data_min_position = raw_data.get("min_position")
            twitter_data_list.append(raw_data)
        except Exception as e:
            continue
    threads = []
    twitter_data_list.append(one_data)


    def callback(obj, data):
        parse_data_list.extend(data)


    pool = threadpool.ThreadPool(20)
    tasks = threadpool.makeRequests(twitter.parse_page_data, twitter_data_list, callback)
    for task in tasks:
        pool.putRequest(task)
    pool.wait()

    for url_dic in parse_data_list:
        # 获取 评论首页html
        url = url_dic.get("profile_tweet_url")
        twitter_id = url_dic.get("twitter_id")
        worker = WorkerThread(profile_tweet_data_list, twitter.get_profile_tweet_data, (url, twitter_id))
        worker.start()
        threads.append(worker)
    for work in threads:
        work.join(1)
        if work.isAlive():
            logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
            threads.append(work)

    threads = []
    for pro_dic in profile_tweet_data_list:
        # 获取评论其他页html
        pro_position = pro_dic.get("data_min_position")
        twitter_id = pro_dic.get("twitter_id")
        comment_list.append(dict(twitter_id=twitter_id, items_html=pro_dic.get("resp"), flag=True))
        if pro_position:
            for i in range(1, 20):  #
                try:
                    worker = WorkerThread(comment_list, twitter.get_comment_data, (pro_position, twitter_id))
                    worker.start()
                    threads.append(worker)
                except Exception as e:
                    continue
            for work in threads:
                work.join(1)
                if work.isAlive():
                    logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
                    threads.append(work)
            threads = []
    for comment_data in comment_list:
        worker = WorkerThread([], twitter.parse_comment_data, (comment_data,))
        worker.start()
