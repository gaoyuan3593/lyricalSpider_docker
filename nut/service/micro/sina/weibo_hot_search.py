#! /usr/bin/python3
# -*- coding: utf-8 -*-


from service.core.utils.http_ import Requester
from service.exception import retry
from service.exception.exceptions import *
from service import logger
from service.micro.utils import ua
from bs4 import BeautifulSoup
#from service.db.utils.elasticsearch_utils import es


class WeiBoHotSpider(object):
    __name__ = 'Weibo hot search'

    def __init__(self, cookie=None):
        if not cookie:
            self.requester = Requester()

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, RequestFailureError), time_to_sleep=3)
    def get_hot_search_list(self):
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
        try:
            response = self.requester.get(url=url, header_dict=headers)
            if '热搜榜' in response.text and response.status_code == 200:
                resp = self.parse_hot_search_data(response.text)
                self.write_data_to_es(resp)
            else:
                logger.error('get weibo hot search list failed !')
                raise HttpInternalServerError
        except Exception as e:
            raise RequestFailureError

    @classmethod
    def parse_hot_search_data(self, raw_data):
        if not raw_data:
            return None
        return_list = list()
        data_obj = BeautifulSoup(raw_data, "lxml")
        try:
            data_list = data_obj.find_all("div", attrs={"id": "pl_top_realtimehot"})
            if not data_list:
                resp = self.parse_search_data(data_obj)
                return resp
            hot_list = data_list[0].find_all("tr")[1:]
            for raw in hot_list:
                len_num = len(raw.contents[3].contents)
                index = raw.contents[1].text.strip() if raw.contents[1].text.strip() else "置顶"
                keyword = raw.contents[3].contents[1].text
                search_num = "无" if len_num <= 3 else raw.contents[3].contents[3].text
                mark = raw.contents[5].text.strip()
                w_url = "https://s.weibo.com" + raw.contents[3].contents[1].attrs.get("href")
                return_list.append({keyword: dict(
                    index=index,
                    keyword=keyword,
                    search_num=search_num,
                    mark=mark,
                    w_url=w_url
                )})

            return return_list
        except IndexError as e:
            raise RequestFailureError

    @classmethod
    def parse_search_data(self, obj):
        return_list = list()
        try:
            data_list = obj.find_all("ul", attrs={"class": "list_a"})[0]
            hot_list = data_list.find_all("li")[1:]
            for raw in hot_list:
                index = raw.contents[1].contents[1].text.strip()
                keyword = str(raw.contents[1].contents[3].contents[0])
                search_num = raw.contents[1].contents[3].contents[1].text.strip()
                mark = ""
                w_url = "https://s.weibo.com" + raw.contents[1].attrs.get("href")
                return_list.append({keyword: dict(
                    index=index,
                    keyword=keyword,
                    search_num=search_num,
                    mark=mark,
                    w_url=w_url
                )})

            return return_list
        except Exception as e:
            raise RequestFailureError

    def write_data_to_es(self, data):
        if not data:
            logger.error("weibo hot search not data !")


if __name__ == "__main__":
    wb = WeiBoHotSpider()
    resp = wb.get_hot_search_list()
