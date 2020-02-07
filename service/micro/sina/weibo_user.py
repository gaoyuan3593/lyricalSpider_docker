#! /usr/bin/python3
# -*- coding: utf-8 -*-

import re
import requests
from urllib.parse import quote
from bs4 import BeautifulSoup
from service.exception import retry
from service.exception.exceptions import *
from service import logger
from service.micro.news.utils.proxies_util import get_proxies
from service.db.utils.elasticsearch_utils import es_client


class WeiBoUsereSpider(object):
    __name__ = 'Weibo user '

    def __init__(self, params):
        self.user_name = params.get("user_name")
        self.s = requests.session()
        self.es = es_client

    def use_proxies(self):
        self.s.proxies = get_proxies()

    @retry(max_retries=5, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=0.5)
    def get_user_resp(self):
        logger.info('Processing get user id data ！')
        try:
            url = "https://s.weibo.com/user?q={}&sudaref=s.weibo.com&display=0&retcode=6102&Refer=SUer_box".format(
                quote(self.user_name))
            headers = {
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0",
                'Connection': 'keep-alive',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Host': 's.weibo.com',
                'Upgrade-Insecure-Requests': '1'
            }
            response = self.s.get(url=url, headers=headers, verify=False)
            if "抱歉，未找到“{}”相关结果。".format(self.user_name) in response.text or "请尽量输入常用词" in response.text:
                return dict(
                    status=200,
                    message="抱歉，未找到用户“{}”相关结果。".format(self.user_name)
                )
            if self.user_name in response.text and response.status_code == 200:
                logger.info("get user resp success user_name:{}".format(self.user_name))
                return response.text
            else:
                logger.error('get weibo user id failed !')
                raise HttpInternalServerError
        except Exception as e:
            logger.exception(e)
            self.use_proxies()
            raise HttpInternalServerError

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def query(self):
        logger.info('Processing get weibo user name= {} ！'.format(self.user_name))
        user_resp = self.get_user_resp()
        if isinstance(user_resp, dict):
            logger.info("Temporarily no user information. data: {}".format(user_resp))
            return dict(
                status=200,
                msg="暂无用户 : {} 信息".format(self.user_name),
                result=None
            )
        user_data = self.parse_user_data(user_resp)
        if not user_data:
            return dict(
                status=200,
                msg="暂无 user_id : {} 信息".format(self.user_name),
                result=None
            )
        else:
            logger.info(" get weibo user data success data: {}".format(user_data))
            return dict(
                status=200,
                msg="success",
                result=user_data
            )

    def parse_user_data(self, resp):
        if not resp:
            return
        data_list, tag_list = [], []
        verified = ""
        soup = BeautifulSoup(resp, "lxml")
        div_tag_list = soup.find_all("div", attrs={"class": "card card-user-b s-pg16 s-brt1"})
        for div in div_tag_list:
            try:
                a_tag = div.find("a", attrs={"class": "s-btn-c"})
                uid = a_tag.attrs.get("uid")
                user_name = div.find("a", attrs={"class": "name"}).text
                city = div.find("p").text.strip().split("\n")[0]
                follow_count = re.findall(r"关注(\d+万?)", div.text)[0]
                fan_count = re.findall(r"粉丝(\d+[万,亿]?)", div.text)[0]
                weibo_count = re.findall(r"微博(\d+万?)", div.text)[0]
                profile_image_url = div.find("div", attrs={"class": "avator"}).find("img").attrs.get("src")
                sex = div.find("i", attrs={"class": "icon-sex icon-sex-female"})
                gender = "female" if sex else "male"
                verified_y = div.find("i", attrs={"class": "icon-vip icon-vip-y"})
                verified_b = div.find("i", attrs={"class": "icon-vip icon-vip-b"})
                verified_g = div.find("i", attrs={"class": "icon-vip icon-vip-g"})
                if verified_b:
                    verified = "blue"
                elif verified_y or verified_g:
                    verified = "yellow"

                introduction = re.findall(r"简介：(.*)?", div.text)
                job_data = re.findall(r"职业信息：(.*)?", div.text)
                edu_data = re.findall(r"教育信息：(.*)?", div.text)
                p_list = div.find_all("p")
                for p in p_list:
                    if "标签" in p.text:
                        tag_list = [a.text for a in p.find_all("a")]
                data_list.append(
                    dict(
                        user_name=user_name,
                        uid=uid,
                        city=city,
                        follow_count=follow_count,
                        fan_count=fan_count,
                        weibo_count=weibo_count,
                        tag=tag_list,
                        gender=gender,
                        verified=verified,
                        introduction="".join(introduction),
                        job_data="".join(job_data),
                        edu_data="".join(edu_data),
                        profile_image_url=profile_image_url,
                    )
                )
            except Exception as e:
                logger.exception(e)
                raise e
        return data_list


def get_handler(*args, **kwargs):
    return WeiBoUsereSpider(*args, **kwargs)


if __name__ == '__main__':
    dic = {
        "user_name": "人民日报",
    }
    wb = WeiBoUsereSpider(dic)
    wb.query()
