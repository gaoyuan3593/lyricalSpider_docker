#! /usr/bin/python3
# -*- coding: utf-8 -*-

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


class SouGouGongZhongHaoSpider(object):
    __name__ = 'Sou Gou G ong Zhong Hao'

    def __init__(self, params=None):
        self.params = params
        self.ua = ua()
        self.cookies = self.get_cookie()
        self.requester = Requester(cookie=dict_to_cookie_jar(self.cookies), timeout=20)
        self.account = self.params.get("account")

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

    def query(self):
        data = self.get_gongzhonghao_data()
        if data:
            return dict(
                status=200,
                msg="success",
                result=data
            )
        else:
            return dict(
                status=200,
                msg="暂无公众号信息"
            )

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=0.5)
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
            'Referer': "https://weixin.sogou.com/weixin?type=1&s_from=input&query={}&ie=utf8&_sug_=n&_sug_type_=".format(
                quote(self.account))
        }
        try:
            data_list = []
            resp = self.requester.get(url, header_dict=headers)
            if 'charset="utf-8"' in resp.text:
                resp.encoding = "utf-8"
                if "用户您好，我们的系统检测到您网络中存在异常访问请求" in resp.text:
                    captcha_code = self.get_captcha_code(self.account)
                    is_ok = self.verify_captcha_code(captcha_code, self.account)
                    raise RequestFailureError
            elif self.account in resp.text and resp.text.find("account_article_0"):
                soup = BeautifulSoup(resp.text, "lxml")
                li_obj_list = soup.find_all("li", attrs={"id": True})
                i = 0
                for li_obj in li_obj_list:
                    try:
                        title = li_obj.find("a", attrs={"uigs": "account_article_{}".format(i)}).text.strip()
                    except:
                        continue
                    gong_zhong_hao = li_obj.find("a", attrs={"uigs": "account_name_{}".format(i)}).text.strip()
                    zifuchuo = re.findall(r"timeConvert\('(\d+)'\)", li_obj.text)
                    aid = self.retrun_md5(zifuchuo[0])
                    article_date = datetime.strptime(
                        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(zifuchuo[0]))), "%Y-%m-%d %H:%M:%S")
                    url = 'https://weixin.sogou.com' + li_obj.find("a", attrs={"uigs": "account_article_{}".format(i)}).attrs.get(
                        "href")
                    b = random.randint(0, 99)
                    a = url.index('url=')
                    a = url[a + 25 + b:a + 26 + b:]
                    url += '&k=' + str(b) + '&h=' + a
                    wechat_num = li_obj.find("label", attrs={"name": "em_weixinhao"}).text.strip()
                    profile_meta = li_obj.find("dd").text.strip()
                    data = dict(
                        gong_zhong_hao=gong_zhong_hao,
                        title=title,
                        article_date=article_date,
                        url=url,
                        aid=aid,
                        wechat_num=wechat_num,
                        profile_meta=profile_meta
                    )
                    data_list.append(data)
                    i += 1
                return data_list
            else:
                logger.info("gei wechat gong zhong hao failed")
                self.next_cookie()
                self.requester.use_proxy()
                raise RequestFailureError
        except Exception as e:
            logger.exception(e)
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
        result_data = to_json(response.text)
        logger.info("result_data : {}".format(result_data))
        result_code = result_data.get('code', None)
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


def get_handler(*args, **kwargs):
    return SouGouGongZhongHaoSpider(*args, **kwargs)
