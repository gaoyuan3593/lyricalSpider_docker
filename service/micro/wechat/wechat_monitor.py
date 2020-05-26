#! /usr/bin/python3
# -*- coding: utf-8 -*-
import base64
import hashlib
import random
import time
import json
import re
from urllib.parse import quote
import uuid
from datetime import datetime
from bs4 import BeautifulSoup
from service.core.utils.http_ import Requester
from service.exception import retry
from service.exception.exceptions import *
from service import logger
from service.micro.utils import ua
from service.db.utils.elasticsearch_utils import es_client, h_es_client
from service.db.utils.es_mappings import WECHAT_DETAIL_MAPPING

_index_mapping = {
    "detail_type":
        {
            "properties": WECHAT_DETAIL_MAPPING
        },
}


class WeChatMonitor(object):
    __name__ = 'wechat monitor'

    def __init__(self, params=None):
        self.params = params
        self.ua = ua()
        self.token = "1548857430"
        self.cookies = "noticeLoginFlag=1; ua_id=agMPRAvAG8aPJ8dnAAAAAPFiplZP1irqMdiJMqQJkVw=; pgv_pvi=8984983552; pgv_si=s1645932544; cert=n1UcbUh6kqCG70vKDn5AwwWr4EEWr4sX; mm_lang=zh_CN; _qpsvr_localtk=0.8973135076599092; RK=BchRjkuzdA; ptcz=a6c4c9d42a1aff9cd94a2da8fb7862c68d56cf54a7dd150866fbf85de1be770b; uin=o0071116455; pgv_pvid=392578576; pgv_info=ssid=s3002772968; rewardsn=; wxtokenkey=777; pac_uid=1_71116455; XWINDEXGREY=0; o_cookie=71116455; skey=@1CEw5SYhL; rv2=805592F071148749416BCDD0FB32D0BE2E0A2DF24B543B541C; property20=5D623FD5D75942D9F50FB5B671AD55AC60DF3265926BD1D35CF5E56BF381E48C4F3B61F75CE5FDC8; openid2ticket_o9EnQ1MiSUMOFekBXRXNhaGX65r0=q/wpFhbVLga507Gq8nQhTdMg47/nOH3sJ0wZUgXJoWs=; uuid=f272920cd37cb53b670e71771f823e69; rand_info=CAESIOAPehWhGDgQtAR0QgqK5LlSnZCEg2V1JYcnGWTHLiRz; slave_bizuin=3570420212; data_bizuin=3570420212; bizuin=3570420212; data_ticket=PiEXQ9GuD6Kx2wuQgLfO63AHAEbyYMZHk5jqv5OzTKGgiw0Ytg1EeykMGTVWkA+1; slave_sid=THVhZmpCaHVPVDM4aFNweWtVVUhuZ1dMdURVM1BQT1diQ3d6MUdCeHNkdUZpTVcwZGIzVElZbm8wa0V4S2huY1lsczVXb1AxbDkzcGoxbVVDb0xHdjJsS2Z1T082WlpPeUY3cTFVX3MzY09TUlBFZUV3OFVRQ0k5REs5WTJXOTNTUkdjSTI3U1NRbVpYekhj; slave_user=gh_34143ab2721d; xid=5994df8b8182ed16d2f88c88b644bc35"
        self.requester = Requester(timeout=20)
        self.es_index = self.params.get("wechat_index")
        self.account = self.params.get("account")
        self.es = es_client
        self.h_es = h_es_client

    def retrun_md5(self, s):
        m = hashlib.md5()
        m.update(s.encode("utf-8"))
        return m.hexdigest()

    def random_num(self):
        return random.uniform(13, 25)

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
                logger.info("{} Data already exists id: {}".format(self.__name__, id))
                return
            self.es.insert(self.es_index, _type, data, id)
            self.h_es.insert(self.es_index, _type, data, id)
            logger.info("{} save to es success [ index : {}, data={}]！".format(self.__name__, self.es_index, data))
        except Exception as e:
            logger.exception(e)
            raise e

    def query(self):
        url_list = self.get_weixin_gongzhonghao()
        self.es.create_index(self.es_index, _index_mapping)
        for url in url_list:
            try:
                article_url_list = self.get_weixin_page_data(url)
                if article_url_list:
                    for article_data in article_url_list:
                        self.get_weixin_article_details(article_data)
                else:
                    return
            except Exception as e:
                continue

        return dict(
            status=200,
            index=self.es_index,
            message="微信获取成功！"
        )

    @retry(max_retries=5, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_weixin_gongzhonghao(self):
        logger.info('{} Processing get get weixin gong zhong hao!'.format(self.__name__))
        url = "https://mp.weixin.qq.com/cgi-bin/searchbiz?action=search_biz&token={}&lang=zh_CN&f=json&ajax=1&query={}&begin=0&count=1".format(
            self.token, quote(self.account))
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 'mp.weixin.qq.com',
            "Cookie": self.cookies
        }
        try:
            response = self.requester.get(url=url, header_dict=headers).json()
            if not response.get("list"):
                return dict(
                    status=200,
                    message="抱歉，未找到“{}”公众号。".format(self.account)
                )
            elif response.get("list"):
                data = response.get("list")
                logger.info("get wei xin gong zhong hao success data: {}".format(data))
                fake_id = data[0].get("fakeid")
                url_list = self.parse_weixin_page_url(fake_id)
                return url_list
            else:
                logger.error('get wei xin gong zhong hao failed !')
                self.requester.use_proxy()
                raise HttpInternalServerError
        except Exception as e:
            time.sleep(self.random_num())
            raise RequestFailureError

    @retry(max_retries=5, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=2)
    def get_weixin_page_data(self, url=None, fake_id=None):
        """
        获取公众号html
        :return: dict
        """
        logger.info('Processing get wei xin page data ')
        try:
            if not url:
                url = "https://mp.weixin.qq.com/cgi-bin/appmsg?token={}&lang=zh_CN&f=json&ajax=1&action=list_ex&begin=0&count=5&query=&fakeid={}&type=9".format(
                    self.token, fake_id)
            headers = {
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
                'Connection': 'keep-alive',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Host': 'mp.weixin.qq.com',
                "Upgrade-Insecure-Requests": "1",
                "Cookie": self.cookies
            }
            time.sleep(self.random_num())
            response = self.requester.get(url=url, header_dict=headers).json()
            if response.get("app_msg_list"):
                if not fake_id:
                    logger.info("{} get weixin page data success url: {}".format(self.__name__, url))
                    art_list = self.parse_weixin_article_url(response)
                    if art_list:
                        return art_list
                    else:
                        return
                else:
                    return response
            elif 'freq control' in response.get("base_resp").get("err_msg"):
                logger.error("Please control the request frequency！")
                time.sleep(3600)
                raise HttpInternalServerError
            else:
                logger.error('get wei xin page data failed !')
                self.requester.use_proxy()
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
            time.sleep(2)
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
            elif "观看" in response.text or "发布到看一看" in response.text:
                return
            elif resp_obj.find("div", attrs={"id": "img_list"}):
                return
            else:
                logger.error('get wechat detail failed !')
                self.requester.use_proxy()
                raise HttpInternalServerError
        except Exception as e:
            time.sleep(self.random_num())
            raise HttpInternalServerError

    def parse_weixin_page_url(self, fake_id):
        """
        解析所有页的url
        :return: list
        """
        resp = self.get_weixin_page_data(fake_id=fake_id)
        count = resp.get("app_msg_cnt")
        num = count // 10
        # page_num = 401 if num >= 400 else num
        url_list = []
        begin = 0
        for i in range(num):
            url = "https://mp.weixin.qq.com/cgi-bin/appmsg?token={}&lang=zh_CN&f=json&ajax=1&action=list_ex&begin={}&count=5&query=&fakeid={}&type=9".format(
                self.token, begin, fake_id)
            url_list.append(url)
            begin += 5
        return url_list

    def parse_weixin_article_url(self, resp):
        """
        解析所有文章详情的urla
        :return: list
        """
        if not resp:
            return
        data_list = []
        try:
            for data in resp.get("app_msg_list"):
                title = data.get("title")
                create_time = data.get("create_time")
                str_id = str(create_time) + title
                aid = self.retrun_md5(str_id)
                if self.filter_keyword(aid, "detail_type"):
                    print("已存在 title :{}".format(title))
                    return data_list
                url = data.get("link")
                cover = data.get("cover")
                article_date = datetime.strptime(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(create_time)),
                                                 "%Y-%m-%d %H:%M:%S")
                data_list.append(dict(
                    aid=aid,
                    title=title,
                    url=url,
                    cover=cover,
                    article_date=article_date,
                ))
            return data_list
        except Exception as e:
            logger.exception(e)

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
            if resp_obj.find_all("iframe"):
                [s.extract() for s in resp_obj("iframe")]
            article_text = resp_obj.find("div", attrs={"id": "js_content"}).text.strip()  # 文章内容
            wechat_num = resp_obj.find_all("span", attrs={"class": "profile_meta_value"})[0].text.strip()  # 微信号
            profile_meta = resp_obj.find_all("span", attrs={"class": "profile_meta_value"})[1].text.strip()  # 功能介绍
            img = resp_obj.find_all("img", attrs={"data-ratio": True})  # 是否有图片
            if img:
                pics = 1
                img_url = [soup.attrs.get("data-src") for soup in img]
            article_id = resp.get("aid")
            data = dict(
                title=resp.get("title"),
                author=self.account,
                time=resp.get("article_date"),
                contents=article_text,
                id=article_id,
                type="detail_type",
                is_pics=pics,
                img_url_list=img_url,
                wechat_num=wechat_num,
                profile_meta=profile_meta,
                is_share=is_share,  # 是否是分享
                link=resp.get("url"),  # 文章链接
                crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")  # 爬取时间
            )
            self.save_one_data_to_es(data, article_id)
        except Exception as e:
            logger.info(" article is delete article_id: ")
            logger.exception(e)


if __name__ == "__main__":
    from service.micro.wechat import ALL_WECHAT

    for dic in ALL_WECHAT:
        weichat = WeChatMonitor(dic)
        weichat.query()
