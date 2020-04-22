#! /usr/bin/python3
# -*- coding: utf-8 -*-
import hashlib
import random
import time
import re
import gc
import json
from datetime import datetime
from urllib.parse import quote
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
from service.db.utils.elasticsearch_utils import es_client, h_es_client
from service.db.utils.es_mappings import WEIBO_DETAIL_MAPPING
from service.micro.sina.utils.sina_mid import mid_to_str

INDEX_TYPE = "wei_bo"
_index_mapping = {
    INDEX_TYPE:
        {
            "properties": WEIBO_DETAIL_MAPPING
        },

}


class WeiBoTeacherSpider(object):
    __name__ = 'Weibo teacher keyword'

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
        self.es_index = self.params.get("index")
        self.name_cn = self.params.get("name_cn")
        self.name_en = self.params.get("name_en")
        self.cookie = dict_to_cookie_jar(self.get_cookie())
        self.requester = Requester(cookie=self.cookie, timeout=15)
        self.es = es_client
        self.h_es = h_es_client

    def get_cookie(self):
        redis_cli = RedisClient('cookies', 'weibo')
        return redis_cli.return_choice_cookie()

    def next_cookie(self):
        cookie = dict_to_cookie_jar(self.get_cookie())
        self.requester = Requester(cookie=cookie)

    def random_num(self):
        return random.uniform(1, 3)

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
        """
        将为爬取的数据存入es中
        :param data_list: 数据
        :return:
        """
        try:
            _type = INDEX_TYPE
            if self.filter_keyword(id, _type, data):
                return
            self.es.insert(self.es_index, _type, data, id)
            self.h_es.insert(self.es_index, _type, data, id)
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

    def query(self):
        logger.info('Processing get weibo key word ！')
        try:
            q = self.params.get("q")
            self.es.create_index(self.es_index, _index_mapping)
            self.h_es.create_index(self.es_index, _index_mapping)
            url_list = [
                dict(
                    url="https://s.weibo.com/weibo?q={}&wvr=6&b=1&Refer=SWeibo_box".format(q),
                    keyword=q
                )
            ]
            threads = []
            wb_data_list = []
            page_data_url_list, page_html_url_list = [], []
            html_list = self.url_threads(url_list)
            if html_list:
                for data in html_list:
                    page_data_url_list.extend(self.parse_weibo_page_url(data))
            else:
                return dict(
                    status=1,
                    index=None,
                    message="微博暂无数据"
                )
            for page_url_data in page_data_url_list:
                # 获取每页内容的html
                url = page_url_data.get("url")
                if not url:
                    page_html_url_list.append(page_url_data)
                    continue
                keyword = page_url_data.get("keyword")
                try:
                    page_html_url_list.append(self.get_weibo_page_data(url, keyword))
                except Exception as e:
                    continue

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

            for wb_data in wb_data_list:
                # 解析微博详情
                if not wb_data:
                    continue
                keyword = wb_data.get("keyword")
                for data in wb_data.get("data"):
                    try:
                        self.parse_weibo_detail(data, keyword)
                    except Exception as e:
                        continue
            return dict(
                status=200,
                index=self.es_index,
                message="微博爬取成功！"
            )
        except Exception as e:
            logger.exception(e)
            raise e

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
            time.sleep(self.random_num())
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
                raise HttpInternalServerError
        except Exception as e:
            self.next_cookie()
            self.requester.use_proxy()
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
                contents = content[1].text.split("收起全文")[0].strip()
            else:
                contents = content[0].text.strip()
            if "该账号因被投诉违反法律法规和《微博社区公约》的相关规定，现已无法查看。" in contents:
                return
            if keyword not in contents:
                return
            topic = re.findall("#(.*?)#", contents)  # 关键字
            if "O网页链接" in contents or "随笔" in contents:
                has_href = 1
            if "转赞" in weibo_time:
                weibo_time = weibo_time.split("转赞")[0].strip()
            if self.name_cn:
                if self.name_cn not in contents:
                    return
            if self.name_en:
                if self.name_en not in contents:
                    return
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
                key_user_id_list=key_user_list,  # @用户id 列表
                forward_user_id_list=forward_user_url_list,  # 转发链 用户id列表
                b_keyword=keyword,
                topic_list=topic,  # 双#号话题
                is_has_href=has_href,  # 是否有网页链接
                is_pics=pics,  # 是否有图片
                is_videos=videos,  # 是否有视频
                crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")  # 爬取时间
            )
            self.save_one_data_to_es(resp_dada, id=weibo_id)
        except Exception as e:
            logger.exception(e)
            return {}

    def comment_str_to_int(self, _str):
        if _str.split(" ")[1].isdigit():
            return int(_str.split(" ")[1])
        return None

    def repost_str_to_int(self, _str):
        if _str.split(" ")[2].isdigit():
            return int(_str.split(" ")[2])
        return None


def get_handler(*args, **kwargs):
    return WeiBoTeacherSpider(*args, **kwargs)


if __name__ == '__main__':
    from apscheduler.schedulers.blocking import BlockingScheduler
    import pytz
    from datetime import datetime, timedelta

    tz = pytz.timezone('America/New_York')


    def foo():
        for i in ["李涛"]:
            dic = {
                "index": "li_tao",
                "q": i,
                "date": "2020-02-28:2020-02-29"
            }
            wb = WeiBoTeacherSpider(dic)
            wb.query()


    foo()
