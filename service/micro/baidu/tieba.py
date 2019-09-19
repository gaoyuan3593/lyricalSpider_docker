#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random
import time
import json
import re
import threadpool

from urllib import parse

from bs4 import BeautifulSoup
from service.core.utils.http_ import Requester
from service.exception import retry
from service.exception.exceptions import *
from service import logger
from service.micro.utils import ua
from service.micro.utils.cookie_utils import dict_to_cookie_jar

from service.db.utils.elasticsearch_utils import ElasticsearchClient, BAIDUTIEBA
from datetime import datetime, timedelta


class TiebaSpider(object):
    __name__ = 'bai du tie ba'

    def __init__(self):
        self.requester = Requester(timeout=20)
        self.es = ElasticsearchClient()

    def filter_keyword(self, id, _type):
        try:
            result = self.es.get(BAIDUTIEBA, _type, id)
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
            _type = data.get("type")
            if self.filter_keyword(id, _type):
                logger.info("Data already exists id: {}".format(id))
                return
            self.es.insert(BAIDUTIEBA, _type, data, id)
            logger.info("save to es success [ index : {}, data={}]！".format(BAIDUTIEBA, data))
        except Exception as e:
            logger.exception(e)
            raise e

    def random_num(self):
        return random.uniform(0.1, 0.5)

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_weibo_hot_seach(self):
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
        keyword_url_list = []
        try:
            response = self.requester.get(url=url, header_dict=headers)
            data_obj = BeautifulSoup(response.text, "lxml")
            data_list = data_obj.find_all("div", attrs={"id": "pl_top_realtimehot"})
            hot_list = data_list[0].find_all("tr")[1:]
            for raw in hot_list:
                keyword = raw.contents[3].contents[1].text
                url = 'http://tieba.baidu.com/f/search/res?isnew=1&ie=utf-8&kw=&qw={}&rn=10&un=&only_thread=1&sm=1'.format(
                    parse.quote(keyword))
                keyword_url_list.append(dict(url=url, keyword=keyword))
            return keyword_url_list
        except Exception as e:
            self.requester.use_proxy(tag="same")
            raise HttpInternalServerError

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
            time.sleep(1)
            self.requester.use_proxy(tag="same")
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
        tiezi_url_list, author_url = [], None
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
                tiezi_time = obj.find("font", attrs={"class": "p_green p_date"}).text.strip()  # 发布时间
                is_photo = obj.find_all("div", attrs={"class": "p_mediaCont"})
                if is_photo:
                    pics = 1  # 是否有图片
                    imgs = [i.next.attrs.get("original") for i in is_photo if i.next.attrs.get("original")]  # 图片链接
                tiezi_url = "https://tieba.baidu.com{}".format(title_obj.attrs.get("href"))
                resp_data = dict(
                    title=title,  # 贴子标题
                    content=content,  # 贴子内容，也就是楼主发布的内容
                    tieba=tieba,  # 所属贴吧
                    author=author,  # 作者
                    tiezi_time=tiezi_time,  # 发布时间
                    pics=pics,  # 是否有图片
                    imgs=imgs,  # 图片链接
                    b_keywold=keyword,  # 关键字
                    type="detail",
                    tid=tid,  # 贴子id
                    fid=fid  # 作者id
                )
                self.save_one_data_to_es(resp_data, tid)
                if author_url:
                    if len(author_url) > 38:
                        self.get_author_detail(author_url, fid)
                tiezi_url_list.append(dict(
                    keyword=keyword,
                    tiezi_url=tiezi_url,
                    tid=tid,
                    fid=fid
                ))
            return tiezi_url_list
        except Exception as e:
            logger.exception(e)
            return tiezi_url_list

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_author_detail(self, author_url, author_id):
        """
        获取作者信息
        :return: dict
        """
        if not author_url:
            return
        logger.info('Processing get author detail ！')
        headers = {
            'User-Agent': ua(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'tieba.baidu.com',
        }
        try:
            resp = self.requester.get(author_url, header_dict=headers)
            if "用户名" in resp.text and "吧龄" in resp.text:
                logger.info("get author detail success author_id: {}".format(author_id))
                self.parse_author_detail(resp.text, author_id)
            elif resp.encoding == 'ISO-8859-1':
                try:
                    resp_text = resp.text.encode("iso-8859-1").decode("utf-8")
                except Exception as e:
                    resp_text = resp.text.encode("iso-8859-1").decode("gbk")
                if "抱歉，您访问的用户已被屏蔽。" in resp_text:
                    return
                elif "很抱歉，您要访问的页面不存在。" in resp_text:
                    return
            else:
                raise InvalidResponseError

        except Exception as e:
            time.sleep(self.random_num())
            raise InvalidResponseError

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_tiezi_data_url(self, _dic):
        """
        获取回复页的url
        :return: dict
        """
        if not _dic:
            return
        page_url_list = []
        url = _dic.get("tiezi_url")
        logger.info('Processing get tiezi data url ！')
        headers = {
            'User-Agent': ua(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'tieba.baidu.com',
        }
        try:
            time.sleep(0.2)
            resp = self.requester.get(url, header_dict=headers).text
            if "发表回复" in resp:
                logger.info("get author detail success url: {}".format(url))
                page_num = re.findall(r'</span>回复贴，共<span class="red">(\d+)?</span>页</li>', resp)[0]
                if int(page_num) > 1:
                    for i in range(2, int(page_num) + 1):
                        page_url = "{}?pn={}".format(url.split("?")[0], i)
                        page_url_list.append(dict(
                            page_url=page_url,
                            keyword=_dic.get("keyword"),
                            tid=_dic.get("tid"),
                        ))
                self.parse_replay_detail(resp)
                return page_url_list
            elif "很抱歉，该贴已被删除。" in resp:
                logger.info("is tiezi detele  url: {}".format(url))
                return None
            elif "很抱歉，该吧被合并您所访问的贴子无法显示。" in resp:
                logger.info("The post that was merged with the post you visited cannot be displayed.  url: {}"
                            .format(url))
                return None
            else:
                raise InvalidResponseError

        except Exception as e:
            time.sleep(self.random_num())
            raise InvalidResponseError

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_next_data(self, _dic):
        """
        获取回复页的url
        :return: dict
        """
        if not _dic:
            return
        page_url_list = []
        url = _dic.get("page_url")
        logger.info('Processing get tiezi data url ！')
        headers = {
            'User-Agent': ua(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'tieba.baidu.com',
        }
        try:
            resp = self.requester.get(url, header_dict=headers).text
            if "发表回复" in resp:
                logger.info("get author detail success url: {}".format(url))
                self.parse_replay_detail(resp)
                return page_url_list
            elif "很抱歉，该贴已被删除。" in resp:
                logger.info("is tiezi detele  url: {}".format(url))
                return None
            elif "很抱歉，该吧被合并您所访问的贴子无法显示。" in resp:
                logger.info("The post that was merged with the post you visited cannot be displayed.  url: {}"
                            .format(url))
                return None
            else:
                self.requester.use_proxy(tag="same")
                raise InvalidResponseError

        except Exception as e:
            time.sleep(self.random_num())
            raise InvalidResponseError

    def parse_author_detail(self, resp, author_id):
        """
        解析作者详情
        :return: list
        """
        if not resp:
            return
        pics, img_url, is_share, is_vip, vip_days = "", [], "", None, None
        follow_count, fan_count, gender = None, None, None
        try:
            resp_obj = BeautifulSoup(resp, 'html.parser')
            user_info = resp_obj.find("div", attrs={"class": "userinfo_userdata"}).text.strip()
            user = re.search(r"用户名:(.*?)吧龄", user_info)
            user = user.group(1) if user else None
            tieba_age = re.search(r"吧龄:(\d+.\d+年)", user_info) or re.search(r"吧龄:(\d+年)", user_info)
            tieba_age = tieba_age.group(1) if tieba_age else None
            tiezi_num = re.search(r"发贴:(\d+)?", user_info)
            tiezi_num = tiezi_num.group(1) if tiezi_num else None
            vip_days_obj = re.search(r"会员天数:(\d+.*)?", user_info)
            if vip_days_obj:
                vip_days = vip_days_obj.group(1)
                is_vip = 1
            nick_name = resp_obj.find("div", attrs={"class": "userinfo_title"}).text.strip()
            _p = resp_obj.find_all("span", attrs={"class": "concern_num"})
            text = resp_obj.find("div", attrs={"class": "right_aside"}).text.strip()
            gender = "male" if "关注他的人" in text else "female"
            if _p:
                if len(_p) > 1:
                    follow, fan = _p[0].text, _p[1].text
                    follow_count = re.findall(r"\d+", follow)[0]
                    fan_count = re.findall(r"\d+", fan)[0]
                else:
                    if "关注他的人" or "关注她的人" in text:
                        fan = _p[0].text
                        fan_count = re.findall(r"\d+", fan)[0]
                    else:
                        follow = _p[0].text
                        follow_count = re.findall(r"\d+", follow)[0]
            profile_image_url = resp_obj.find("a", attrs={"class": "userinfo_head"}).next.attrs.get("src")
            data = dict(
                user=user,  # 用户名
                nick_name=nick_name,  # 昵称
                gender=gender,  # 性别
                tieba_age=tieba_age,  # 吧龄
                tiezi_num=tiezi_num,  # 发帖数
                vip_days=vip_days,  # vip天数
                is_vip=is_vip,  # 是否是会员
                author_id=author_id,  # 用户id,
                follow_count=follow_count,  # 关注数
                fan_count=fan_count,  # 粉丝数
                profile_image_url=profile_image_url,  # 头像url
                type="user"
            )
            self.save_one_data_to_es(data, author_id)
        except Exception as e:
            logger.info(" article is delete article_id: ")
            logger.exception(e)

    def parse_replay_detail(self, resp):
        """
        解析作者详情
        :return: list
        """
        if not resp:
            return
        pics, img_url, replay_text = "", [], None
        try:
            resp_obj = BeautifulSoup(resp, 'lxml')
            _tiezi_list = resp_obj.find("div", attrs={"id": "j_p_postlist"})
            tiezi_list = _tiezi_list.find_all("div", attrs={"class": "l_post j_l_post l_post_bright "}) or \
                         _tiezi_list.find_all("div", attrs={"class": "l_post l_post_bright j_l_post clearfix "})
            landlord = resp_obj.find("div", attrs={"class": "l_post j_l_post l_post_bright noborder "})
            if landlord:
                tiezi_list.append(landlord)
            for replay in tiezi_list:
                _replay = replay.find("div", attrs={"class": "d_post_content j_d_post_content clearfix"}) or \
                          replay.find("div",
                                      attrs={
                                          "class": "d_post_content j_d_post_content d_post_content_bold clearfix"}) or \
                          replay.find(
                              "div",
                              attrs={"class": "d_post_content j_d_post_content d_post_content_bold"})
                if _replay:
                    replay_text = _replay.text.strip()
                    _pics = _replay.find_all("img")
                    if _pics:
                        pics = 1
                        img_url = [tag.attrs.get("src") for tag in _pics]
                data_info = json.loads(replay.attrs.get("data-field"))
                author_info = data_info.get("author")
                content_info = data_info.get("content")
                replay_id = content_info.get("post_id")
                data = dict(
                    user=author_info.get("user_name"),  # 用户名
                    date=content_info.get("date"),  # 评论时间
                    replay_text=replay_text,  # 评论内容
                    nick_name=author_info.get("user_nickname"),  # 昵称
                    level=author_info.get("level_id"),  # 在本贴吧的等级
                    level_name=author_info.get("level_name"),  # 等级头衔说明
                    cur_score=author_info.get("cur_score"),  # 经验值
                    name_u=author_info.get("name_u"),  # url编码的昵称
                    author_id=author_info.get("user_id"),  # 用户id,
                    replay_id=replay_id,  # 回复id
                    source=content_info.get("open_id"),  # 来源
                    platform=content_info.get("open_type"),  # 平台
                    replay_no=content_info.get("post_no"),  # 评论楼数
                    comment_num=content_info.get("comment_num"),  # 评论数
                    type="comment",
                    pics=pics,  # 是否有图片
                    img_url=img_url  # 图片url

                )
                self.save_one_data_to_es(data, replay_id)
        except Exception as e:
            logger.info(" article is delete article_id: ")
            logger.exception(e)


if __name__ == '__main__':
    from service.micro.utils.threading_ import WorkerThread
    from service.micro.utils.threading_parse import WorkerThreadParse

    url_list = []
    page_data_list = []
    tiezi_url_list = []
    replay_url_list = []
    threads = []
    tieba = TiebaSpider()

    keyword_list = tieba.get_weibo_hot_seach()
    for keyword in keyword_list:
        # try:
        #     url_list.extend(tieba.get_begin_page_url(keyword))
        # except Exception as e:
        #     continue
        worker = WorkerThreadParse(url_list, tieba.get_begin_page_url, (keyword,))
        worker.start()
        threads.append(worker)
    for work in threads:
        work.join(1)
        if work.isAlive():
            logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
            threads.append(work)
    # 获取所有页的html
    threads = []
    for url_dic in url_list:
        # try:
        #     page_data = tieba.get_page_url_data(url_dic)
        #     if page_data:
        #         page_data_list.append(page_data)
        # except:
        #     continue
        worker = WorkerThreadParse(page_data_list, tieba.get_page_url_data, (url_dic,))
        worker.start()
        threads.append(worker)
    for work in threads:
        work.join(1)
        if work.isAlive():
            logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
            threads.append(work)

    # 解析 发帖的内容
    threads = []
    for resp_dic in page_data_list:
        dic = tieba.parse_tiezi_detail(resp_dic)
        tiezi_url_list.extend(dic)
    #     worker = WorkerThreadParse(tiezi_url_list, tieba.parse_tiezi_detail, (resp_dic,))
    #     worker.start()
    #     threads.append(worker)
    # for work in threads:
    #     work.join(1)
    #     if work.isAlive():
    #         logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
    #         threads.append(work)

    # 获取 贴子内的 回复内容
    threads = []
    for tiezi_url_dic in tiezi_url_list:
        # data_url = tieba.get_tiezi_data_url(tiezi_url_dic)
        # if data_url:
        #     replay_url_list.extend(data_url)
        worker = WorkerThreadParse(replay_url_list, tieba.get_tiezi_data_url, (tiezi_url_dic,))
        worker.start()
        threads.append(worker)
    for work in threads:
        work.join(1)
        if work.isAlive():
            logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
            threads.append(work)

    for repaly in replay_url_list:
        # data = tieba.get_next_data(repaly)
        # print(data)
        worker = WorkerThreadParse([], tieba.get_next_data, (repaly,))
        worker.start()
        threads.append(worker)
    for work in threads:
        work.join(1)
        if work.isAlive():
            logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
            threads.append(work)
