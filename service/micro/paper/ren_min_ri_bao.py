#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random
import time
import json
import re
import requests
from lxml import etree
from datetime import datetime
from bs4 import BeautifulSoup
from service.exception import retry
from service.exception.exceptions import *
from service import logger
from service.micro.utils.math_utils import people_str_to_format_time
from service.db.utils.elasticsearch_utils import ALL_PAPER_DETAILS, PAPER_ALL_MAPPING
from service.micro.news.utils.search_es import SaveDataToEs

INDEX_TYPE = "paper_ren_min_ri_bao"

_index_mapping = {
    INDEX_TYPE:
        {
            "properties": PAPER_ALL_MAPPING
        }
}


class RenMinRiBaoSpider(object):
    __name__ = 'ren min ri bao news'

    def __init__(self, data):
        self.s = requests.session()
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Host": "paper.people.com.cn",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
        }
        SaveDataToEs.create_index(ALL_PAPER_DETAILS, _index_mapping)

    def random_num(self):
        return random.uniform(0.1, 0.5)

    def get_begin_url(self):
        year = datetime.today().year
        _month = datetime.today().month
        _day = datetime.today().day
        month = str(_month) if len(str(_month)) >= 2 else "0{}".format(_month)
        day = str(_day) if len(str(_day)) >= 2 else "0{}".format(_day)
        url = "http://paper.people.com.cn/rmrb/html/{}-{}/{}/nbs.D110000renmrb_01.htm".format(year, month, day)
        try:
            resp = self.s.get(url, headers=self.headers, verify=False)
            resp.encoding = "utf-8"
            if resp.status_code == 200 and "人民日报-人民网" in resp.text:
                soup = BeautifulSoup(resp.text, "lxml").find("div", attrs={"id": "pageList"})
                div_list = soup.find_all("div", attrs={"class": "right_title-name"})
                url_list = []
                for div in div_list:
                    href = div.find("a").attrs.get("href")
                    url = "http://paper.people.com.cn/rmrb/html/{}-{}/{}/{}".format(year, month, day, href)

                    pdf_url = \
                        div.parent.find("div", attrs={"class": "right_title-pdf"}).find("a").attrs.get("href").split(
                            "../")[
                            -1]
                    pdf = "http://paper.people.com.cn/rmrb/" + pdf_url
                    url_list.append(
                        dict(
                            url=url,
                            pdf=pdf,
                            text=div.text.strip()
                        ))
                return url_list
        except Exception as e:
            logger.exception(e)
            raise e

    @retry(max_retries=5, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_news_all_url(self, url_dic):
        logger.info('Processing get ren min ri bao network search list!')
        data_list = []
        try:
            url = url_dic.get("url")
            response = self.s.get(url, headers=self.headers, verify=False)
            response.encoding = "utf-8"
            if "人民日报-人民网" in response.text:
                soup = BeautifulSoup(response.text, "lxml")
                li_list = soup.find("div", attrs={"id": "titleList"}).find_all("li")
                for li in li_list:
                    title = re.findall(r'\("(.*?)"\)', li.text.strip())
                    if title:
                        title = title[0].strip()
                    date = re.findall(r"\d+-\d+/\d+", url)[0]
                    url = "http://paper.people.com.cn/rmrb/html/{}/{}".format(date, li.find("a").attrs.get("href"))
                    column = url_dic.get("text").split("：")[1]
                    page = url_dic.get("text").split("：")[0]
                    data_list.append(
                        dict(
                            url=url,
                            title=title,
                            column=column,
                            page=page,
                            pdf=url_dic.get("pdf")
                        )
                    )

            return data_list
        except Exception as e:
            raise InvalidResponseError

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_news_detail(self, data):
        logger.info('Processing get jin wan bao details !!!')
        url = data.get("url")
        try:
            response = self.s.get(url, headers=self.headers, verify=False)
            response.encoding = "utf-8"
            if response.status_code == 200:
                logger.info("get ren mn ri bao news detail success url: {}".format(url))
                article_id = url.split("/")[-1].split(".")[1]
                data.update(
                    article_id=article_id,
                    resp=response.text
                )
                return data
            else:
                logger.error("get news detail failed")
                raise InvalidResponseError
        except Exception as e:
            time.sleep(2)
            raise InvalidResponseError

    def parse_news_detail(self, _data):
        if not _data:
            return
        resp = _data.get("resp")
        article_id = _data.get("article_id")
        _content, _editor = "", ""
        try:
            x_html = etree.HTML(resp)
            content = x_html.xpath('//div[@id="ozoom"]/p/text()')
            if not content:
                logger.info("article content is img ...")
                return
            abstract = "".join(content[0]).strip()
            word_num = len("".join(content).strip())
            _content = "\r\n".join(content)
            publish_time = "".join(x_html.xpath('//div[@id="riqi_"]/text()')).strip()
            week = publish_time.split("\r\n")[-1].strip().split(" ")[-1]
            _date = publish_time.split("\r\n")[-1].strip().split(" ")[0].replace("年", "-").replace("月", "-"). \
                replace("日", "")
            editor = re.findall(r"记者(.*?)）", _content)
            if not editor:
                editor = re.findall(r"新华社记者(.*)?", _content)
                if editor:
                    _editor = editor[0].strip()
            else:
                _editor = editor[0]
            data = dict(
                title=_data.get("title"),  # 标题
                id=article_id,  # 文章id
                time=datetime.strptime(_date, "%Y-%m-%d"),  # 发布时间
                week=week,  # 星期
                word_num=word_num,  # 字数
                author=_editor,  # 责任编辑
                column=_data.get("column"),  # 版面内容
                page=_data.get("page"),  # 版面
                pdf=_data.get("pdf"),  # pdf地址
                link=_data.get("url"),  # url连接
                type=INDEX_TYPE,
                paper_name="人民日报",
                abstract=abstract,  # 摘要
                contents=content,  # 内容
                crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")  # 爬取时间
            )
            SaveDataToEs.save_one_data_to_es(ALL_PAPER_DETAILS, data, article_id)
        except Exception as e:
            logger.exception(e)


def get_handler(*args, **kwargs):
    return RenMinRiBaoSpider(*args, **kwargs)


def ren_min_ri_bao_run():
    data_list = []
    detail_list = []
    renmin = RenMinRiBaoSpider({})
    url_list = renmin.get_begin_url()
    if url_list:
        for url_dic in url_list:
            page_data = renmin.get_news_all_url(url_dic)
            data_list.extend(page_data)
        for data in data_list:
            detail = renmin.get_news_detail(data)
            detail_list.append(detail)
        for detail_data in detail_list:
            renmin.parse_news_detail(detail_data)
        return dict(
            status=200,
            message="人民日报采集成功",
        )
    else:
        return dict(
            status=-1,
            message="人民日报没有发布新闻",
        )


if __name__ == '__main__':
    ren_min_ri_bao_run()
