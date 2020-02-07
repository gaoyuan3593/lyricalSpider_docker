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
from service.micro.utils.cookie_utils import dict_to_cookie_jar
from service.micro.utils.math_utils import wechat_date_next, to_json
from service.db.utils.elasticsearch_utils import es_client
from service.db.utils.es_mappings import WECHAT_DETAIL_MAPPING
from service.micro.utils.threading_ import WorkerThread

_index_mapping = {
    "detail_type":
        {
            "properties": WECHAT_DETAIL_MAPPING
        },
}


class SouGouKeywordSpider(object):
    __name__ = 'Sou Gou hot search'

    def __init__(self, params=None):
        self.params = params
        self.ua = ua()
        self.cookies = self.get_cookie()
        self.requester = Requester(cookie=dict_to_cookie_jar(self.cookies), timeout=20)
        self.es_index = self.params.get("wechat_index")
        self.es = es_client

    def get_cookie(self):
        redis_cli = RedisClient('cookies', 'wechat')
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
        return random.uniform(1, 3)

    def filter_keyword(self, id, _type):
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
            _type = data.get("type")
            if self.filter_keyword(id, _type):
                logger.info("Data already exists id: {}".format(id))
                return
            self.es.insert(self.es_index, _type, data, id)
            logger.info("save to es success [ index : {}, data={}]！".format(self.es_index, data))
        except Exception as e:
            logger.exception(e)
            raise e

    def query(self):
        threads = []
        data_list, article_url_list, url_list = [], [], []

        begin_url_list = wechat_date_next(self.params)
        for keyword_dic in begin_url_list:
            try:
                url_list.extend(self.get_weixin_page_url(keyword_dic))
            except Exception as e:
                continue
        if not url_list:
            return dict(
                status=1,
                index=None,
                message="搜狗微信暂无数据"
            )
        for url_data in url_list:
            try:
                data = self.get_weixin_page_data(url_data)
                if data:
                    data_list.append(data)
            except Exception as e:
                continue
        if data_list:
            for data in data_list:
                # 解析所有页的文章url
                #article_url_list.extend(self.parse_weixin_article_url(data))
                worker = WorkerThread(article_url_list, self.parse_weixin_article_url, (data,))
                worker.start()
                threads.append(worker)
            for work in threads:
                work.join(1)
                if work.isAlive():
                    logger.info('Worker thread: failed to join, and still alive, and rejoin it.')
                    threads.append(work)
        self.es.create_index(self.es_index, _index_mapping)
        for article_data in article_url_list:
            try:
                self.get_weixin_article_details(article_data)
            except Exception as e:
                continue
        return dict(
            status=200,
            index=self.es_index,
            message="搜狗微信获取成功！"
        )

    @retry(max_retries=5, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_weixin_page_url(self, data):
        url = data.get("url")
        keyword = data.get("keyword")
        logger.info('Processing get get weixin page url keyword : {}!'.format(keyword))
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 'weixin.sogou.com',
            'Referer': "https://weixin.sogou.com/weixin?type=2&s_from=input&query={}&ie=utf8&_sug_=n&_sug_type_=".format(
                quote(keyword))
        }
        try:
            response = self.requester.get(url=url, header_dict=headers)
            response.encoding = "utf-8"
            if "没有找到相关的微信公众号文章。" in response.text:
                return dict(
                    status=200,
                    message="抱歉，未找到“{}”相关结果。".format(keyword)
                )
            if '以下内容来自微信公众平台' in response.text:
                url_list = self.parse_weixin_page_url(response.text, keyword, url)
                return url_list
            if "用户您好，我们的系统检测到您网络中存在异常访问请求。" in response.text:
                captcha_code = self.get_captcha_code(keyword)
                is_ok = self.verify_captcha_code(captcha_code, keyword)
                raise RequestFailureError
            else:
                logger.error('get weibo hot search list failed !')
                raise HttpInternalServerError
        except Exception as e:
            time.sleep(self.random_num())
            self.requester.use_proxy()
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
            return self.verify_captcha_code(captcha_code, keyword)

    @retry(max_retries=5, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=2)
    def ocr_captcha_code(self, base_str):
        url = 'http://212.64.127.151:6002/ocr_captcha'
        headers = {'Content-Type': 'application/json'}
        data = {
            "image_base64": base_str,
            "app_id": "71116455",
            "ocr_code": "0000"
        }
        # url = 'https://nmd-ai.juxinli.com/ocr_captcha'
        # headers = {'Content-Type': 'application/json'}
        # data = {
        #     "image_base64": base_str,
        #     "app_id": "71116455&VIP@NzExMTY0NTUmVklQ",
        #     "ocr_code": "0000"
        # }
        try:
            req = self.requester.post(url=url, data_dict=data, submission_type="json", header_dict=headers).json()
            logger.info("get captcha code success resp :{}".format(req))
            if req.get("errorcode") == 0:
                return req.get("string")
            else:
                raise HttpInternalServerError
        except Exception as e:
            raise e

    @retry(max_retries=5, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=2)
    def get_weixin_page_data(self, data):
        """
        获取搜狗微信的每页html
        :return: dict
        """
        logger.info('Processing get wechat key word ！data: {}'.format(data))
        try:
            if not data:
                return {}
            url = data.get("url")
            keyword = data.get("keyword")
            try:
                page = int(url.split("page=")[1])
                if page == 1:
                    pass
                else:
                    page -= 1
            except:
                page = 1
            headers = {
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
                'Connection': 'keep-alive',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Host': 'weixin.sogou.com',
                "Upgrade-Insecure-Requests": "1",
                "Referer": "https://weixin.sogou.com/weixin?usip=&query={}&ft=2019-07-31&tsn=5&et=2019-07-31&interation=&type=2&wxid=&page={}&ie=utf8".format(quote(keyword), page)
            }
            time.sleep(self.random_num())
            response = self.requester.get(url=url, header_dict=headers)
            response.encoding = "utf-8"
            if "没有找到相关的微信公众号文章" in response.text:
                return
            elif "当前只显示100条结果，请您：" in response.text:
                logger.error("需要扫码登录")
                self.next_cookie()
                raise HttpInternalServerError
            elif keyword in response.text and '<ul class="searchnav" name="scroll-nav">' in response.text:
                logger.info("get weixin page data success ！！！ ")
                return dict(data=response.text, keyword=keyword, url=url)
            elif "用户您好，我们的系统检测到您网络中存在异常访问请求。" in response.text:
                self.requester.use_proxy()

                captcha_code = self.get_captcha_code(keyword)
                is_ok = self.verify_captcha_code(captcha_code, keyword)
                raise RequestFailureError
            else:
                logger.error('get weibo hot search list failed !')
                raise HttpInternalServerError
        except Exception as e:
            raise RequestFailureError

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
                'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
                'connection': 'keep-alive',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'zh-CN,zh;q=0.9',
                "upgrade-Insecure-Requests": "1",
            }
            time.sleep(self.random_num())
            response = self.requester.get(url=url, header_dict=headers)
            response.encoding = "utf-8"
            resp_obj = BeautifulSoup(response.text, 'html.parser')
            page_url_obj = resp_obj.find("div", attrs={"id": "meta_content"})
            if page_url_obj:
                logger.info("get weixin article details success ！！！")
                data.update(data=response.text)
                self.parse_weixin_article_detail(data)
            elif "你的访问过于频繁，需要从微信打开验证身份，是否需要继续访问当前页面？" in response.text:
                self.requester.use_proxy()
                raise HttpInternalServerError
            elif "观看" in response.text:
                return
            else:
                logger.error('get weibo detail failed !')
                self.requester.use_proxy()
                raise HttpInternalServerError
        except Exception as e:
            time.sleep(self.random_num())
            raise HttpInternalServerError

    def parse_weixin_page_url(self, resp, keyword, url):
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
                    page_url = "{}&page={}".format(url
                                                   , i)
                    url_list.append(dict(url=page_url, keyword=keyword))
                if url_list:
                    return url_list
            return []
        except Exception as e:
            url = "{}&page={}".format(url, 1)
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
                    if self.filter_keyword(article_id, "detail_type"):
                        continue
                    author = tag_soup.find("div", attrs={"class": "s-p"}).find("a").text.strip()  # 作者
                    time_chuo = tag_soup.find("span", attrs={"class": "s2"}).text
                    article_date = self.parse_time_chuo(time_chuo)  # 时间
                    task_date = self.params.get("date")
                    if not self.parse_crawl_date(article_date, task_date):
                        logger.info("Time exceeds start date data= [ article_date : {}, article_id : {}]".
                                    format(article_date, resp.get("article_id")))
                        return
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
        pics, img_url, is_share = 0, [], 0
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
                    return
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
                type="detail_type",
                pics=pics,
                img_url=img_url,
                wechat_num=wechat_num,
                profile_meta=profile_meta,
                is_share=is_share,  # 是否是分享
                article_url=resp.get("url"),  # 文章链接
                crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")  # 爬取时间
            )
            self.save_one_data_to_es(data, article_id)
        except Exception as e:
            logger.info(" article is delete article_id: ")
            logger.exception(e)

    def parse_time_chuo(self, _time):
        import time
        from datetime import datetime
        try:
            int_time = int(re.findall(r'(\d+)', _time)[0])
            time_array = time.localtime(int_time)
            _time = time.strftime("%Y-%m-%d %H:%M", time_array)
        except Exception as e:
            _time = datetime.now().strftime("%Y-%m-%d %H:%M")
        return datetime.strptime(_time, "%Y-%m-%d %H:%M")

    def parse_crawl_date(self, article_date, task_date):
        if not task_date:
            return
        if ":" in task_date:
            start_date, end_date = task_date.split(":")
            _end_date = datetime.strptime(end_date, "%Y-%m-%d")
            begin_date = datetime.strptime(start_date, "%Y-%m-%d")
            _article_date = datetime.strptime(article_date.strftime("%Y-%m-%d"), "%Y-%m-%d")
            if _article_date.__ge__(begin_date):
                if _article_date.__le__(_end_date):
                    return article_date
                else:
                    return None
            else:
                return None


if __name__ == "__main__":

    data = {"date": "2019-09-19:2019-09-19", "q": "华为mate30", "wechat_index": "wechat_hua_wei_mate30_fa_bu_hui_1568948505"}
    weichat = SouGouKeywordSpider(data)
    threads = []
    data_list, weixin_article_url_list = [], []
    article_detail_list, url_list = [], []

    begin_url_list = weichat.query()
