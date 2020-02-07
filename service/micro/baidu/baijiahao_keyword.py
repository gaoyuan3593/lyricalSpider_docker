#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random
import time
import re
import threadpool
from bs4 import BeautifulSoup
from service.core.utils.http_ import Requester
from service.exception import retry
from service.exception.exceptions import *
from service import logger
from service.micro.utils import ua
from service.db.utils.elasticsearch_utils import es_client
from datetime import datetime, timedelta
from service.db.utils.es_mappings import BAIJIAHAO_DETAIL_MAPPING

_index_mapping = {
    "detail_type":
        {
            "properties": BAIJIAHAO_DETAIL_MAPPING
        },
}


class BaiJiaHaoSpider(object):
    __name__ = 'bai jia hao'

    def __init__(self, params=None):
        self.params = params
        self.es_index = self.params.get("baijiahao_index")
        self.requester = Requester(timeout=20)
        self.es = es_client

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

    def random_num(self):
        return random.uniform(0.1, 0.5)

    def query(self):
        acticle_url_list, acticle_detail_list = [], []
        keyword = self.params.get("q")
        keyword_dic = self.parse_url_kewword(keyword)
        self.es.create_index(self.es_index, _index_mapping)
        data = self.get_begin_page_url(keyword_dic)
        acticle_url_list.extend(data)
        for url_dic in acticle_url_list:
            try:
                acticle_data = self.get_acticle_detail(url_dic)
                if acticle_data:
                    acticle_detail_list.extend(acticle_data)
            except:
                continue
        if not acticle_detail_list:
            return dict(
                status=1,
                index=None,
                message="百家号暂无数据"
            )
        for data in acticle_detail_list:
            self.parse_baijiahao_article_detail(data)


        return dict(
            status=200,
            index=self.es_index,
            message="百家号获取成功！"
        )

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
                url = 'https://www.baidu.com/s?tn=news&rtt=4&bsst=2&cl=2&wd={}'.format(
                    keyword)
                keyword_url_list.append(dict(url=url, keyword=keyword))
            return keyword_url_list
        except Exception as e:
            self.requester.use_proxy()
            raise HttpInternalServerError

    def parse_url_kewword(self, keyword):
        return dict(
            url='https://www.baidu.com/s?tn=news&rtt=4&bsst=2&cl=2&wd={}'.format(
                keyword),
            keyword=keyword
        )

    @retry(max_retries=7, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_begin_page_url(self, dic):
        """
        获取开始页的内容
        :return: dict
        """
        logger.info('Processing get bai du zixun key word ！')
        data = []
        keyword = dic.get("keyword")
        url = dic.get("url")
        headers = {
            'User-Agent': ua(),
            'Connection': 'keep-alive',
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
        }
        try:
            time.sleep(self.random_num())
            resp = self.requester.get(url, header_dict=headers).text
            if "charset=gb2312" in resp:
                resp = resp.encode('ISO-8859-1').decode("gbk")
                time.sleep(15)
                raise HttpInternalServerError
            elif keyword in resp:
                logger.info("get_begin_page_url sussess！！！！ ")
                one_page_data = self.parse_next_url(resp)
                page_url = one_page_data.get("next_page_url")
                if one_page_data:
                    data.append(dict(keyword=keyword, acticle_url_list=one_page_data.get("acticle_url_list")))
                    while True:
                        if not page_url:
                            return data
                        page_data = self.get_next_page_data(page_url, keyword)
                        if page_data:
                            page_url = page_data.get("next_page_url")
                            if not page_url:
                                return data
                        else:
                            continue
                        data.append(dict(keyword=keyword, acticle_url_list=page_data.get("acticle_url_list")))
        except Exception as e:
            self.requester.use_proxy()
            raise e

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=2)
    def get_next_page_data(self, next_page_url, keyword):
        """
        获取每个关键词的下页内容
        :return: dict
        """
        logger.info('Processing parse next url！')
        headers = {
            'User-Agent': ua(),
            'Connection': 'keep-alive',
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
        }
        try:
            # time.sleep(self.random_num())
            resp = self.requester.get(next_page_url, header_dict=headers).text
            if keyword in resp:
                logger.info("get_next_page_data success！！！！ ")
                url_data = self.parse_next_url(resp)
                return url_data
            elif "charset=gb2312" in resp:
                resp = resp.encode('ISO-8859-1').decode("gbk")
                time.sleep(15)
                raise HttpInternalServerError
            else:
                raise HttpInternalServerError
        except Exception as e:
            self.requester.use_proxy()
            raise HttpInternalServerError

    def parse_next_url(self, resp):
        """
         解析每个关键词的下页内容
        :return: dict
        """
        logger.info('Processing parse next url！')
        try:
            next_page_url = None
            soup = BeautifulSoup(resp, "html.parser")
            next_obj = soup.find_all("a", attrs={"class": "n"})
            for i in next_obj:
                if "下一页" in i.text:
                    next_page_url = "https://www.baidu.com{}".format(i.attrs.get("href"))
            acticle_list = soup.find_all("h3", attrs={"class": "c-title"})
            acticle_url_list = [
                obj.find("a").attrs.get("href")
                for obj in acticle_list
                if "baijiahao.baidu.com" in obj.find("a").attrs.get("href")
            ]
            return dict(acticle_url_list=acticle_url_list, next_page_url=next_page_url)
        except Exception as e:
            return {}

    @retry(max_retries=5, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_acticle_detail(self, url_dic):
        """
        获取百家号的文章详情
        :return: dict
        """
        data_list = []
        if not url_dic.get("acticle_url_list"):
            return
        for acticle_url in url_dic.get("acticle_url_list"):
            logger.info('Processing parse next url！')
            headers = {
                'User-Agent': ua(),
                'Connection': 'keep-alive',
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'Accept-Encoding': 'gzip, deflate',
                'Host': 'baijiahao.baidu.com'
            }
            try:
                resp = self.requester.get(acticle_url, header_dict=headers).text
                if "意见反馈" in resp and "帐号设置" in resp:
                    logger.info("get acticle seccuss acticle_url :{}".format(acticle_url))
                    article_id = re.findall(r"id=(\d+)?", acticle_url)[0]
                    data_list.append(
                        dict(
                            resp=resp,
                            article_id=article_id,
                            acticle_url=acticle_url,
                            keyword=url_dic.get("keyword")
                        )
                    )
                elif "文章暂时找不到了" in resp:
                    logger.info("acticle is exits")
                    return
                else:
                    raise TimedOutError
            except Exception as e:
                time.sleep(5)
                self.requester.use_proxy()
                raise HttpInternalServerError
        return data_list

    def parse_baijiahao_article_detail(self, resp):
        """
        解析文章详情
        :return: list
        """
        if not resp:
            return
        pics, img_url, is_share = "", [], ""
        try:
            resp_obj = BeautifulSoup(resp.get("resp"), 'html.parser')
            title = resp_obj.find("div", attrs={"class": "article-title"}).text.strip()  # 文章标题
            article_text = resp_obj.find("div", attrs={"class": "article-content"}).text.strip()  # 文章内容
            _date = resp_obj.find("div", attrs={"class": "article-source article-source-bjh"}).contents[0].text  # 发布时间
            _time = resp_obj.find("div", attrs={"class": "article-source article-source-bjh"}).contents[1].text  # 发布时间
            article_date = self.format_date(_date, _time)  # 发布时间
            task_date = self.params.get("date")
            if not self.parse_crawl_date(article_date, task_date):
                logger.info("Time exceeds start date data= [ article_date : {}, article_id : {}]".
                            format(article_date, resp.get("article_id")))
                return
            author = resp_obj.find("p", attrs={"class": "author-name"}).text.strip()  # 作者
            avatar_img = resp_obj.find("div", attrs={"class": "author-icon"}).find("img").attrs.get("src")  # 头像
            img = resp_obj.find_all("img", attrs={"class": "large"})  # 是否有图片
            user_id = re.findall(r"appId:(\d+)?", resp.get("resp"))[0]
            try:
                introduction = resp_obj.find("div", attrs={"class": "author-desc"}).text.split("简介:")[1]  # 作者简介
            except Exception as e:
                introduction = ""
            if img:
                pics = 1
                img_url = [soup.attrs.get("src") for soup in img]
            article_id = resp.get("article_id")
            data = dict(
                title=title,
                author=author,
                introduction=introduction,
                time=article_date,
                avatar_img=avatar_img,  # 头像
                b_keyword=resp.get("keyword"),
                contents=article_text,
                id=article_id,
                type="detail_type",
                is_pics=pics,
                user_id=user_id,
                img_url_list=img_url,
                link=resp.get("acticle_url"),  # 文章链接
                crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")  # 爬取时间
            )
            self.save_one_data_to_es(data, article_id)
        except Exception as e:
            logger.info(" article is delete article_id: ")
            logger.exception(e)

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

    def format_date(self, _date, _time):
        _str = None
        try:
            if "发布时间：" in _date:
                _date = _date.replace("发布时间：", "")
            if len(_date) > 5:
                _str = "20{}{}{}".format(_date, " ", _time)
            else:
                _str = "2019-{}{}{}".format(_date, " ", _time)
        except:
            _str = (datetime.now() + timedelta(minutes=-10)).strftime("%Y-%m-%d %H:%M")
        return datetime.strptime(_str, "%Y-%m-%d %H:%M")


if __name__ == '__main__':
    acticle_detail_list = []
    user_id_list = []
    acticle_url_list = []
    keyword_list = ["高校", "教师", "学生", "中小学", "幼儿园", "录取", "录取通知书", "大学", "中学", "小学", "暑假", "补习班", "托管班", "老师"]
    for keyword in keyword_list:
        dic = {
            "baijiahao_index": "baijiahao_keyword_details",
            "q": keyword,
            "date": "2019-07-01:2019-07-31"
        }
        bjh = BaiJiaHaoSpider(dic)
        bjh.query()