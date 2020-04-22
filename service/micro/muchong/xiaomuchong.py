#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random
import time
import re
from urllib.parse import quote
from bs4 import BeautifulSoup
from service.core.utils.http_ import Requester
from service.exception import retry
from service.exception.exceptions import *
from service import logger
from service.micro.utils import ua
from service.db.utils.elasticsearch_utils import es_client, h_es_client
from datetime import datetime, timedelta
from service.db.utils.es_mappings import MUCHONG_DETAIL_MAPPING

INDEX_TYPE = "xiao_mu_chong"

_index_mapping = {
    INDEX_TYPE:
        {
            "properties": MUCHONG_DETAIL_MAPPING
        },
}


class XiaoMuChongSpider(object):
    __name__ = 'xiao mu chong'

    def __init__(self, params=None):
        self.params = params
        self.es_index = self.params.get("index")
        self.name_cn = self.params.get("name_cn")
        self.name_en = self.params.get("name_en")
        self.requester = Requester(timeout=20)
        self.es = es_client
        self.h_es = h_es_client

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
            _type = INDEX_TYPE
            if self.filter_keyword(id, _type):
                logger.info("Data already exists id: {}".format(id))
                return
            self.es.insert(self.es_index, _type, data, id)
            self.h_es.insert(self.es_index, _type, data, id)
            logger.info("save to es success [ index : {}, data={}]！".format(self.es_index, data))
        except Exception as e:
            logger.exception(e)
            raise e

    def random_num(self):
        return random.uniform(0.1, 0.5)

    def query(self):
        acticle_url_list, acticle_detail_list = [], []
        keyword = self.params.get("q")
        keyword_dic = self.parse_url_kewword(keyword)
        self.es.create_index(self.es_index, _index_mapping)
        self.h_es.create_index(self.es_index, _index_mapping)
        url_list = self.get_begin_page_url(keyword_dic)
        acticle_url_list = self.get_page_data(url_list)
        if not acticle_url_list:
            return dict(
                status=1,
                index=None,
                message="小木虫暂无数据"
            )
        for url_dic in acticle_url_list:
            try:
                acticle_data = self.get_acticle_detail(url_dic)
                if acticle_data:
                    acticle_detail_list.append(acticle_data)
            except:
                continue

        for data in acticle_detail_list:
            self.parse_mochong_article_detail(data)

        return dict(
            status=200,
            index=self.es_index,
            message="小木虫获取成功！"
        )

    def parse_url_kewword(self, keyword):
        s = self.retrun_gb2312(keyword)
        return dict(
            url='http://muchong.com/bbs/search.php?wd={}&fid=&mode=3'.format(s),
            keyword=keyword
        )

    def retrun_gb2312(self, keyword):
        s = ""
        for c in keyword:
            st = c.encode("gb2312").hex()
            a, b = st[:2], st[2:]
            s += "%{}%{}".format(a.upper(), b.upper())
        return s

    @retry(max_retries=7, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_begin_page_url(self, dic):
        """
        获取开始页的内容
        :return: dict
        """
        logger.info('Processing get bai du zixun key word ！')
        url_list = []
        keyword = dic.get("keyword")
        url = dic.get("url")
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
            'Connection': 'keep-alive',
            'Host': "muchong.com",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
        }
        try:
            resp = self.requester.get(url, header_dict=headers).text
            if "小木虫论坛" in resp:
                logger.info("get_begin_page_url sussess！！！！ ")
                page = int(re.findall(r"共搜索到 (\d+) ", resp)[0])
                count = page // 25 + 1
                for i in range(0, count):
                    url_list.append(dict(
                        url='http://muchong.com/bbs/search.php?wd={}&fid=0&search_type=&adfilter=0&mode=3&page={}'.
                            format(self.retrun_gb2312(keyword), i + 1),
                        keyword=keyword
                    ))
                return url_list
        except Exception as e:
            self.requester.use_proxy()
            raise e

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=2)
    def get_page_data(self, url_list):
        """
        获取每个关键词的下页内容
        :return: dict
        """
        data_list = []
        logger.info('Processing parse next url！')
        for dic in url_list:
            keyword = dic.get("keyword")
            url = dic.get("url")
            headers = {
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
                'Connection': 'keep-alive',
                'Host': "muchong.com",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'Accept-Encoding': 'gzip, deflate',
            }
            try:
                resp = self.requester.get(url, header_dict=headers).text
                if "小木虫论坛" in resp:
                    logger.info("get_begin_page_url sussess！！！！ ")
                    soup = BeautifulSoup(resp, "lxml")
                    tr_list = soup.find("div", attrs={"class": "forum_body"}).find_all("tr")

                    for tr in tr_list:
                        sort = tr.find("td", attrs={"class": "sort"}).text.strip()
                        title = tr.find("th", attrs={"class": "t_new"}).text.strip()
                        author = tr.find("td", attrs={"class": "by"}).text.strip()
                        date = tr.find_all("td")[-1].text.strip()
                        desc = tr.find("div").text.strip()
                        url = tr.find("th", attrs={"class": "t_new"}).find("a").attrs.get("href")
                        id = url.split("/")[-1]
                        data_list.append(
                            dict(
                                id=id,
                                title=title,
                                sort=sort,
                                author=author,
                                date=date,
                                desc=desc,
                                keyword=keyword,
                                url=url,
                            )
                        )
                else:
                    raise HttpInternalServerError
            except Exception as e:
                self.requester.use_proxy()
                raise HttpInternalServerError
        return data_list

    @retry(max_retries=5, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_acticle_detail(self, url_dic):
        """
        获取小木虫的文章详情
        :return: dict
        """
        if not url_dic:
            return
        url = url_dic.get("url")
        logger.info('Processing get acticle deail url！')
        headers = {
            'User-Agent': ua(),
            'Connection': 'keep-alive',
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'muchong.com'
        }
        try:
            resp = self.requester.get(url, header_dict=headers).text
            if "该内容需要登录查看" in resp:
                headers.update(
                    cookie="_ga=GA1.2.1526571606.1583112009; guest_view_tid=14074150; last_r_mail=71116455%40qq.com; last_r_username=15522900097; last_r_hash=WFlcWVdcXUVTUVlsQxBxAl9YXF4lFBxbAAcD; Hm_lvt_2207ecfb7b2633a3bc5c4968feb58569=1583112011,1583563283; _discuz_in=1; _discuz_uid=21384635; _discuz_pw=24addf4190519a26; last_ip=202.113.11.215_21384635; discuz_tpl=qing; _discuz_cc=27851826531054377; view_tid=14077542; Hm_lpvt_2207ecfb7b2633a3bc5c4968feb58569=1583563471"
                    )
                resp = self.requester.get(url, header_dict=headers).text
                logger.info("get acticle seccuss acticle_url :{}".format(url))
                url_dic.update(resp=resp)
                return url_dic
            if "小木虫论坛" in resp:
                logger.info("get acticle seccuss acticle_url :{}".format(url))
                url_dic.update(resp=resp)
                return url_dic
            else:
                raise HttpInternalServerError
        except Exception as e:
            self.requester.use_proxy()
            raise HttpInternalServerError

    def parse_mochong_article_detail(self, resp):
        """
        解析文章详情
        :return: list
        """
        if not resp:
            return
        keyword = resp.get("keyword")
        try:
            resp_obj = BeautifulSoup(resp.get("resp"), 'html.parser')
            article_text = resp_obj.find("div", attrs={"class": "t_fsz"}).text.strip()  # 文章内容
            if keyword not in article_text:
                return
            if self.name_cn:
                if self.name_cn not in article_text:
                    return
            if self.name_en:
                if self.name_en not in article_text:
                    return
            article_time = datetime.strptime(resp.get("date"), "%Y-%m-%d %H:%M")
            article_id = resp.get("id")
            data = dict(
                title=resp.get("title"),  #标题
                author=resp.get("author"), # 作者
                description=resp.get("desc"), # 文章简介
                time=article_time,  # 文章时间
                b_keyword=keyword,
                contents=article_text, # 文章内容
                id=article_id,  # 文章id
                link=resp.get("url"),  # 文章链接
                crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")  # 爬取时间
            )
            self.save_one_data_to_es(data, article_id)
        except Exception as e:
            logger.info(" article is delete article_id: ")
            logger.exception(e)


if __name__ == '__main__':
    acticle_detail_list = []
    user_id_list = []
    acticle_url_list = []

    dic = {
        "index": "li_tao",
        "q": "李涛",
    }
    bjh = XiaoMuChongSpider(dic)
    bjh.query()
