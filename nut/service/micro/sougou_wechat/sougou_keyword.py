#! /usr/bin/python3
# -*- coding: utf-8 -*-
import base64
import random
import time
import json
import re
from urllib.parse import quote
import uuid
from datetime import datetime
from bs4 import BeautifulSoup
from service.core.utils.http_ import Requester
from service.db.utils.redis_utils import RedisClient
from service.exception import retry
from service.exception.exceptions import *
from service import logger
from service.micro.utils import ua
from service.micro.utils.cookie_utils import dict_to_cookie_jar, cookie_jar_to_dict
from service.micro.utils.math_utils import sougou_str_to_format_time, to_json
from service.db.utils.elasticsearch_utils import ElasticsearchClient, SOUGOU_KEYWORD_DETAIL


class SouGouKeywordSpider(object):
    __name__ = 'Sou Gou hot search'

    def __init__(self):
        self.ua = ua()
        self.cookies = self.get_cookie()
        self.requester = Requester(cookie=dict_to_cookie_jar(self.cookies), timeout=15)
        self.es = ElasticsearchClient()

    def get_cookie(self):
        redis_cli = RedisClient('cookies', 'sougou_cookie')
        return redis_cli.return_choice_cookie()

    def next_cookie(self):
        cookie = dict_to_cookie_jar(self.get_cookie())
        self.requester = Requester(cookie=cookie, timeout=15)

    def update_cookie(self, snuid):
        cookie_dic = self.requester.cookie()
        cookie_dic.update(SNUID=snuid)
        cookie_dic = json.dumps(cookie_dic)
        self.requester = Requester(cookie=dict_to_cookie_jar(cookie_dic), timeout=15)

    def random_num(self):
        return random.uniform(1, 2)

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
            result = self.es.dsl_search(SOUGOU_KEYWORD_DETAIL, _type, mapping)
            if result.get("hits").get("hits"):
                if _type == "detail":
                    self.es.update(SOUGOU_KEYWORD_DETAIL, _type, result.get("hits").get("hits")[0].get("_id"), data)
                    logger.info("dic : {}, update success".format(_dic))
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
            self.es.insert(SOUGOU_KEYWORD_DETAIL, _type, data)
            logger.info(" save to es success data= {}！".format(data))
        except Exception as e:
            raise e

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
                url = 'https://weixin.sogou.com/weixin?type=2&s_from=input&query={}&ie=utf8&_sug_=n&_sug_type_='.format(
                    keyword)
                keyword_url_list.append(dict(url=url, keyword=keyword))
            return keyword_url_list
        except Exception as e:
            raise HttpInternalServerError

    @retry(max_retries=5, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_weixin_page_url(self, data):
        url = data.get("url")
        keyword = data.get("keyword")
        logger.info('Processing get get weixin page url!')
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 'weixin.sogou.com'
        }
        try:
            #time.sleep(self.random_num())
            response = self.requester.get(url=url, header_dict=headers)
            response.encoding = "utf-8"
            if "没有找到相关的微信公众号文章。" in response.text:
                return dict(
                    status=200,
                    message="抱歉，未找到“{}”相关结果。".format(keyword)
                )
            if '以下内容来自微信公众平台' in response.text:
                url_list = self.parse_weixin_page_url(response.text, keyword)
                return url_list
            if "用户您好，我们的系统检测到您网络中存在异常访问请求。" in response.text:
                captcha_code = self.get_captcha_code(keyword)
                is_ok = self.verify_captcha_code(captcha_code, keyword)
                if is_ok:
                    raise RequestFailureError
            else:
                logger.error('get weibo hot search list failed !')
                raise HttpInternalServerError
        except Exception as e:
            if e.code == 500006:
                raise e
            time.sleep(self.random_num())
            self.requester.use_proxy()
            self.requester.clear_cookie()
            self.next_cookie()
            raise RequestFailureError

    @retry(max_retries=3, exceptions=(CaptchaVerifiedError,), time_to_sleep=1)
    def get_captcha_code(self, keyword):
        logger.info('%s Processing recognize captcha code ' % (self.__name__,))
        url = "https://weixin.sogou.com/antispider/util/seccode.php"
        quo = "input&query={}&ie=utf8&_sug_=n&_sug_type_=".format(keyword)
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 'weixin.sogou.com',
            'Referer': "https://weixin.sogou.com/antispider/?from=/weixin?type=2&s_from={}".format(quote(quo))
        }
        resp = self.requester.get(url, header_dict=headers)
        if resp:
            res = base64.b64encode(resp.content).decode()
            captcha_code = self.ocr_captcha_code(res)
            return captcha_code

    def verify_captcha_code(self, captcha_code, keyword):
        url = "https://weixin.sogou.com/antispider/thank.php"
        quo = "input&query={}&ie=utf8&_sug_=n&_sug_type_=".format(keyword)
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 'weixin.sogou.com',
            'Referer': "https://weixin.sogou.com/antispider/?from=/weixin?type=2&s_from={}".format(quote(quo))
        }
        data = {
            "c": captcha_code,
            "r": "https://weixin.sogou.com/antispider/?from=/weixin?type=2&s_from={}".format(quote(quo)),
            "v": 5
        }
        response = self.requester.post(url, header_dict=headers, data_dict=data)
        response.encoding = "utf-8"
        data = to_json(response.text)
        result_code = data.get('code', None)
        if result_code == 0:
            snuid = data.get("id")
            self.update_cookie(snuid)
            return True
        else:
            logger.error('verify captcha code failed. ')
            captcha_code = self.get_captcha_code(keyword)
            self.verify_captcha_code(captcha_code, keyword)

    @retry(max_retries=5, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=2)
    def ocr_captcha_code(self, base_str):
        url = 'http://212.64.127.151:6002/ocr_captcha'
        headers = {'Content-Type': 'application/json'}
        data = {
            "image_base64": base_str,
            "app_id": "71116455",
            "ocr_code": "0000"
        }
        req = self.requester.post(url=url, data_dict=data, submission_type="json", header_dict=headers).json()
        logger.info("get captcha code success resp :{}".format(req))
        if req.get("errorcode") == 0:
            return req.get("string")
        else:
            raise HttpInternalServerError

    @retry(max_retries=5, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=2)
    def get_weixin_page_data(self, data):
        """
        获取搜狗微信的每页html
        :return: dict
        """
        logger.info('Processing get weibo key word ！')
        try:
            if not data:
                return {}
            url = data.get("url")
            keyword = data.get("keyword")
            headers = {
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
                'Connection': 'keep-alive',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Host': 'weixin.sogou.com',
                "Upgrade-Insecure-Requests": "1",
            }
            #time.sleep(self.random_num())
            response = self.requester.get(url=url, header_dict=headers)
            response.encoding = "utf-8"
            if "没有找到相关的微信公众号文章" in response.text:
                return
            if keyword in response.text and '<ul class="searchnav" name="scroll-nav">' in response.text:
                logger.info("get weixin page data success ！！！ ")
                return dict(data=response.text, keyword=keyword, url=url)
            else:
                logger.info("keyword not in data")
            if "当前只显示100条结果，请您：" in response.text:
                logger.error("需要扫码登录")
                raise HttpInternalServerError
            if "用户您好，我们的系统检测到您网络中存在异常访问请求。" in response.text:
                captcha_code = self.get_captcha_code(keyword)
                is_ok = self.verify_captcha_code(captcha_code, keyword)
                if is_ok:
                    raise RequestFailureError
            else:
                logger.error('get weixin page data failed !')
                raise HttpInternalServerError
        except Exception as e:
            if e.code == 500006:
                raise e
            time.sleep(self.random_num())
            self.requester.use_proxy()
            self.requester.clear_cookie()
            self.next_cookie()
            raise HttpInternalServerError

    @retry(max_retries=5, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=2)
    def get_weixin_article_details(self, data):
        """
        获取搜狗微信文章详情html
        :return: dict
        """
        logger.info('Processing get sougou weichat article details ！')
        try:
            if not data:
                return {}
            url = data.get("url")
            headers = {
                'user-agent': ua(),
                'connection': 'keep-alive',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'zh-CN,zh;q=0.9',
                "upgrade-Insecure-Requests": "1",
            }
            time.sleep(self.random_num())
            response = self.requester.get(url=url, header_dict=headers)
            response.encoding = "utf-8"
            if data.get("author") in response.text:
                logger.info("get weixin article details success ！！！")
                data.update(data=response.text)
                return data
            elif "你的访问过于频繁，需要从微信打开验证身份，是否需要继续访问当前页面？" in response.text:
                raise HttpInternalServerError
            else:
                logger.error('get weibo detail failed !')
                raise HttpInternalServerError
        except Exception as e:
            time.sleep(self.random_num())
            self.requester.use_proxy()
            self.requester.clear_cookie()
            self.next_cookie()
            raise HttpInternalServerError

    def parse_weixin_page_url(self, resp, keyword):
        """
        解析所有页的url
        :return: list
        """
        if not resp:
            return
        url_list = []
        try:
            resp_obj = BeautifulSoup(resp, 'html.parser')
            page_url_obj = resp_obj.find("ul", attrs={"class": "news-list"})
            if page_url_obj:
                text = resp_obj.find("div", attrs={"class": "mun"}).text
                _str = text.split("条")[0].split("约")[1]
                if "," in _str:
                    _str = _str.replace(",", "")
                page_num = int(_str) // 10 + 1
                page_num = 101 if page_num > 100 else page_num
                for i in range(1, page_num):
                    url = "https://weixin.sogou.com/weixin?query={}&s_from=hotnews&type=2&page={}&ie=utf8".format(
                        keyword, i)
                    url_list.append(dict(url=url, keyword=keyword))
                if url_list:
                    return url_list
            return []
        except Exception as e:
            url = "https://weixin.sogou.com/weixin?query={}&s_from=hotnews&type=2&page={}&ie=utf8".format(
                keyword, 1)
            return [dict(url=url, keyword=keyword)]

    def parse_weixin_article_url(self, resp):
        """
        解析所有文章详情的url
        :return: list
        """
        if not resp:
            return
        url_list = []
        try:
            keyword = resp.get("keyword")
            resp_obj = BeautifulSoup(resp.get("data"), 'html.parser')
            page_url_obj = resp_obj.find("ul", attrs={"class": "news-list"}).find_all("li")
            if page_url_obj:
                for tag_soup in page_url_obj:
                    article_id = tag_soup.attrs.get("d")
                    author = tag_soup.find("div", attrs={"class": "s-p"}).find("a").text.strip()  # 作者
                    time_chuo = tag_soup.find("span", attrs={"class": "s2"}).text
                    article_date = self.parse_time_chuo(time_chuo)  # 时间
                    url = tag_soup.find("div", attrs={"class": "txt-box"}).find("a").attrs.get("data-share")
                    data = dict(url=url,
                                keyword=keyword,
                                author=author,
                                article_date=article_date,
                                article_id=article_id
                                )
                    url_list.append(data)
                    logger.info("parse_weixin_article_url success data: {} ".format(data))
                if url_list:
                    return url_list
            return []
        except Exception as e:
            logger.exception(e)
            return []

    def parse_weixin_article_detail(self, resp):
        """
        解析文章详情
        :return: list
        """
        if not resp:
            return
        pics, img_url, is_share = "", [], ""
        try:
            resp_obj = BeautifulSoup(resp.get("data"), 'html.parser')
            if "阅读全文" in resp.get("data"):
                is_share = 1
                try:
                    url = resp_obj.find("a", attrs={"id": "js_share_source"}).attrs.get("href")
                    resp.update(url=url)
                    _data = self.get_weixin_article_details(resp)
                    resp_obj = BeautifulSoup(_data.get("data"), 'html.parser')
                except Exception as e:
                    pass
            title = resp_obj.find("h2", attrs={"id": "activity-name"}).text.strip()  # 文章标题
            article_text = resp_obj.find("div", attrs={"id": "js_content"}).text.strip()  # 文章内容
            wechat_num = resp_obj.find_all("span", attrs={"class": "profile_meta_value"})[0].text.strip()  # 微信号
            profile_meta = resp_obj.find_all("span", attrs={"class": "profile_meta_value"})[1].text.strip()  # 功能介绍
            img = resp_obj.find_all("img", attrs={"data-ratio": True})  # 是否有图片
            if img:
                pics = 1
                img_url = [soup.attrs.get("data-src") for soup in img]
            article_id = resp.get("article_id")
            data = dict(
                title=title,
                author=resp.get("author"),
                article_date=resp.get("article_date"),
                b_keyword=resp.get("keyword"),
                article_text=article_text,
                article_id=article_id,
                type="detail",
                pics=pics,
                img_url=img_url,
                wechat_num=wechat_num,
                profile_meta=profile_meta,
                is_share=is_share,  # 是否是分享
                article_url=resp.get("url"),  # 文章链接
            )
            dic = {"article_id.keyword": article_id}
            self.save_one_data_to_es(data, dic)
        except Exception as e:
            logger.info(" article is delete article_id: ")
            logger.exception(e)

    def parse_time_chuo(self, _time):
        import time
        import datetime
        try:
            int_time = int(re.findall(r'(\d+)', _time)[0])
            time_array = time.localtime(int_time)
            _time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
        except Exception as e:
            _time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        return _time


if __name__ == "__main__":
    from service.micro.utils.threading_ import WorkerThread

    weichat = SouGouKeywordSpider()
    threads = []
    data_list, weixin_article_url_list = [], []
    article_detail_list, url_list = [], []

    keyword_list = weichat.get_weibo_hot_seach()
    for keyword_data in keyword_list:
        try:
            url_list.extend(weichat.get_weixin_page_url(keyword_data))
        except:
            continue
    #     worker = WorkerThread(url_list, weichat.get_weixin_page_url, (keyword_data,))
    #     worker.start()
    #     threads.append(worker)
    # for work in threads:
    #     work.join(1)
    #     if work.isAlive():
    #         logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
    #         threads.append(work)
    # threads = []
    for url_data in url_list[:100]:
        try:
            data = weichat.get_weixin_page_data(url_data)
            if data:
                data_list.append(data)
        except Exception as e:
            continue
    #     worker = WorkerThread(data_list, weichat.get_weixin_page_data, (url_data,))
    #     time.sleep(1)
    #     worker.start()
    #     threads.append(worker)
    # for work in threads:
    #     work.join(1)
    #     if work.isAlive():
    #         logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
    #         threads.append(work)
    # threads = []

    if data_list:
        for data in data_list:
            #解析所有页的文章url
            #weixin_article_url_list.extend(weichat.parse_weixin_article_url(data))
            worker = WorkerThread(weixin_article_url_list, weichat.parse_weixin_article_url, (data,))
            worker.start()
            threads.append(worker)
        for work in threads:
            work.join(1)
            if work.isAlive():
                logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
                threads.append(work)
    threads = []
    for article_data in weixin_article_url_list:
        worker = WorkerThread(article_detail_list, weichat.get_weixin_article_details, (article_data,))
        worker.start()
        threads.append(worker)
    for work in threads:
        work.join(1)
        if work.isAlive():
            logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
            threads.append(work)

    threads = []
    for article in article_detail_list:
        weichat.parse_weixin_article_detail(article)
    #     worker = WorkerThread([], weichat.parse_weixin_article_detail, (article,))
    #     worker.start()
    #     threads.append(worker)
    # for work in threads:
    #     work.join(1)
    #     if work.isAlive():
    #         logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
    #         threads.append(work)

