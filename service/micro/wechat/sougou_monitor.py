#! /usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
print(curPath)
rootPath = os.path.split(curPath)[0]
print(os.path.split(rootPath)[0])
sys.path.append(os.path.split(os.path.split(rootPath)[0])[0])
print(sys.path)

import base64
import random
import time
import json
import re
from urllib.parse import quote
import hashlib
from datetime import datetime
from bs4 import BeautifulSoup
from service.core.utils.http_ import Requester
from service.db.utils.redis_utils import RedisClient
from service.exception import retry
from service.exception.exceptions import *
from service import logger
from service.micro.utils import ua
from service.micro.utils.cookie_utils import dict_to_cookie_jar, cookie_jar_to_dict
from service.micro.utils.math_utils import wechat_date_next, to_json
from service.db.utils.elasticsearch_utils import ElasticsearchClient
from service.db.utils.es_mappings import WECHAT_DETAIL_MAPPING
from service.micro.utils.threading_ import WorkerThread

_index_mapping = {
    "detail_type":
        {
            "properties": WECHAT_DETAIL_MAPPING
        },
}


class SouGouMonitorSpider(object):
    __name__ = 'Sou Gou Monitor'

    def __init__(self, params=None):
        self.params = params
        self.ua = ua()
        self.cookies = self.get_cookie()
        self.requester = Requester(cookie=dict_to_cookie_jar(self.cookies), timeout=20)
        self.es_index = self.params.get("wechat_index")
        self.account = self.params.get("account")
        self.es = ElasticsearchClient()

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

    def retrun_md5(self, s):
        m = hashlib.md5()
        m.update(s.encode("utf-8"))
        return m.hexdigest()

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
        data = self.get_gongzhonghao_data()
        if data:
            self.es.create_index(self.es_index, _index_mapping)
            article_data = self.get_article_url(data)
            self.get_weixin_article_details(article_data)

        return dict(
            status=200,
            index=self.es_index,
            message="搜狗微信获取成功！"
        )

    @retry(max_retries=5, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_gongzhonghao_data(self):
        logger.info("{} Begin get gong zhong hao...".format(self.__name__))
        url = "https://weixin.sogou.com/weixin?type=1&s_from=input&query={}&ie=utf8&_sug_=n&_sug_type_=".format(
            quote(self.account))
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 'weixin.sogou.com',
            'Referer': "https://weixin.sogou.com/weixin?type=1&s_from=input&query={}&ie=utf8&_sug_=n&_sug_type_=".format(quote(self.account))
        }
        try:
            resp = self.requester.get(url, header_dict=headers)
            if 'charset="utf-8"' in resp.text:
                resp.encoding = "utf-8"
                if "用户您好，我们的系统检测到您网络中存在异常访问请求" in resp.text:
                    captcha_code = self.get_captcha_code(self.account)
                    is_ok = self.verify_captcha_code(captcha_code, self.account)
                    self.requester.use_proxy(tag="same")
                    raise RequestFailureError
            elif self.account in resp.text and resp.text.find("account_article_0"):
                soup = BeautifulSoup(resp.text, "html")
                li_obj = soup.find("li", attrs={"id": "sogou_vr_11002301_box_0"})
                title = li_obj.find("a", attrs={"uigs": "account_article_0"}).text.strip()
                zifuchuo = re.findall(r"timeConvert\('(\d+)'\)", li_obj.text)
                aid = self.retrun_md5(zifuchuo[0])
                if self.filter_keyword(aid, "detail_type"):
                    logger.info("{} article_id: {} is existed".format(self.__name__, aid))
                    return
                article_date = datetime.strptime(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(zifuchuo[0]))),"%Y-%m-%d %H:%M:%S")
                url = 'https://weixin.sogou.com' + li_obj.find("a", attrs={"uigs": "account_article_0"}).attrs.get("href")
                b = random.randint(0, 99)
                a = url.index('url=')
                a = url[a + 25 + b:a + 26 + b:]
                url += '&k=' + str(b) + '&h=' + a
                wechat_num = soup.find("label", attrs={"name": "em_weixinhao"}).text.strip()
                profile_meta = soup.find("dd").text.strip()
                data = dict(
                    title=title,
                    article_date=article_date,
                    url=url,
                    aid=aid,
                    wechat_num=wechat_num,
                    profile_meta=profile_meta
                )
                return data
            else:
                logger.info("gei wechat gong zhong hao failed")
                self.next_cookie()
                self.requester.use_proxy()
                raise RequestFailureError
        except Exception as e:
            logger.exception(e)
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

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=2)
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

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=2)
    def ocr_captcha_code(self, base_str):
        url = 'https://nmd-ai.juxinli.com/ocr_captcha'
        headers = {'Content-Type': 'application/json'}
        data = {
            "image_base64": base_str,
            "app_id": "71116455&VIP@NzExMTY0NTUmVklQ",
            "ocr_code": "0000"
        }
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
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
                'Connection': 'keep-alive',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Host': "mp.weixin.qq.com",
                #'Referer': "https://weixin.sogou.com/weixin?type=1&s_from=input&query={}&ie=utf8&_sug_=n&_sug_type_=".format(quote(self.account))
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
                self.requester.use_proxy(tag="same")
                raise HttpInternalServerError
            elif "观看" in response.text:
                return
            elif "用户您好，我们的系统检测到您网络中存在异常访问请求" in response.text:
                captcha_code = self.get_captcha_code(self.account)
                is_ok = self.verify_captcha_code(captcha_code, self.account)
                self.next_cookie()
                self.requester.use_proxy()
                raise RequestFailureError
            else:
                logger.error('get weibo detail failed !')
                self.requester.use_proxy()
                raise HttpInternalServerError
        except Exception as e:
            time.sleep(self.random_num())
            raise HttpInternalServerError

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=2)
    def get_article_url(self, data):
        logger.info('Processing get sougou weichat article url ！')
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
                'Host': "weixin.sogou.com",
                'Referer': "https://weixin.sogou.com/weixin?type=1&s_from=input&query={}&ie=utf8&_sug_=n&_sug_type_=".format(
                    quote(self.account))
            }
            response = self.requester.get(url=url, header_dict=headers)
            response.encoding = "utf-8"
            if 'meta content="always" name="referrer"' in response.text:
                url = "".join(re.findall(r"'(.*)'", response.text)[1:])
                data.update(url=url)
                return data
            elif "用户您好，我们的系统检测到您网络中存在异常访问请求" in response.text:
                captcha_code = self.get_captcha_code(self.account)
                is_ok = self.verify_captcha_code(captcha_code, self.account)
                self.next_cookie()
                self.requester.use_proxy()
                raise RequestFailureError
            else:
                logger.error('get weibo detail failed !')
                self.requester.use_proxy()
                raise HttpInternalServerError
        except Exception as e:
            time.sleep(self.random_num())
            raise HttpInternalServerError

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
            article_text = resp_obj.find("div", attrs={"id": "js_content"}).text.strip()  # 文章内容
            img = resp_obj.find_all("img", attrs={"data-ratio": True})  # 是否有图片
            if img:
                pics = 1
                img_url = [soup.attrs.get("data-src") for soup in img]
            article_id = resp.get("aid")
            data = dict(
                title=resp.get("title"),
                author=self.account,
                article_date=resp.get("article_date"),
                article_text=article_text,
                article_id=resp.get("aid"),
                type="detail_type",
                pics=pics,
                img_url=img_url,
                wechat_num=resp.get("wechat_num"),
                profile_meta=resp.get("profile_meta"),  #功能介绍
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


def get_handler(*args, **kwargs):
    return SouGouMonitorSpider(*args, **kwargs)


if __name__ == "__main__":

    from datetime import datetime, timedelta

    from apscheduler.schedulers.blocking import BlockingScheduler

    def wechat():
        data = {"account": "人民日报", "wechat_index": "wechat_ren_min_ri_bao_2803301701"}
        data2 = {"account": "新华网", "wechat_index": "wechat_xin_hua_wang_2810373291"}
        for da in [data, data2]:
            weichat = SouGouMonitorSpider(da)
            begin_url_list = weichat.query()
            print(begin_url_list)

    wechat()
    import pytz

    tz = pytz.timezone('America/New_York')
    sched = BlockingScheduler({'apscheduler.job_defaults.max_instances': '50'})

    # 微博热搜定时任务
    sched.add_job(wechat, 'interval', minutes=60, next_run_time=datetime.now(tz) + timedelta(seconds=5))
    # 中国知网定时任务
    # sched.add_job(run_cnki_tasks, 'interval', days=7)

    sched.start()
