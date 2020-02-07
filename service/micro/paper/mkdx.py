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

INDEX_TYPE = "paper_xin_hua_mei_ri_dian_xun"

_index_mapping = {
    INDEX_TYPE:
        {
            "properties": PAPER_ALL_MAPPING
        }
}


class XinHuaMeiRiDianXunSpider(object):
    __name__ = 'xin hua mei ri dian xun'

    def __init__(self, data):
        self.s = requests.session()
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Host": "www.dailytelegraph.cn",
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
        url = "http://mrdx.cn/content/{}{}{}/Page02DK.htm".format(year, month, day)
        try:
            resp = self.s.get(url, headers=self.headers, verify=False)
            resp.encoding = "utf-8"
            if resp.status_code == 200 and "新华每日电讯" in resp.text:
                soup = BeautifulSoup(resp.text, "lxml").find("div", attrs={"class": "listdaohang"})
                div_list = soup.contents[3::2]
                url_list = []
                pdf, column, page = "", "", ""
                for div in div_list:
                    if "版：" in div.text:
                        pdf_url = div.find("a").attrs.get("href").split("../")[-1]
                        pdf = "http://www.dailytelegraph.cn/" + pdf_url
                        column = div.text.strip().split("：")[1]
                        page = div.text.strip().split("：")[0]
                    if div.find("li"):
                        li_list = div.find_all("li")
                        for li in li_list:
                            title = li.find("a").text.strip()
                            url = "http://www.dailytelegraph.cn/content/{}{}{}/{}".format(year, month,
                                                                                          day, li.find("a").attrs.get(
                                    "daoxiang"))
                            article_id = li.find("a").attrs.get("field")
                            url_list.append(dict(
                                title=title,
                                url=url,
                                article_id=article_id,
                                pdf=pdf,
                                column=column,
                                page=page
                            ))
                return url_list
        except Exception as e:
            logger.exception(e)
            raise e

    @retry(max_retries=5, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_news_all_url(self, url_dic):
        logger.info('Processing get xin hua mei ri dian xun bao network search list!')
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
        logger.info('Processing get xin hua mei ri dian xun details !!!')
        url = data.get("url")
        try:
            response = self.s.get(url, headers=self.headers, verify=False)
            response.encoding = "utf-8"
            if response.status_code == 200:
                logger.info("get xin hua mei ri dian xun news detail success url: {}".format(url))
                data.update(
                    resp=response.text
                )
                return data
            elif response.status_code == 404:
                logger.info("xin hua mei ri dian xun news artiacle is delete title:{}".format(data.get("title")))
                return
            else:
                logger.error("get xin hua mei ri news detail failed")
                raise InvalidResponseError
        except Exception as e:
            time.sleep(2)
            raise InvalidResponseError

    def parse_news_detail(self, _data):
        if not _data:
            return
        resp = _data.get("resp")
        article_id = _data.get("article_id")
        _editor = ""
        try:
            x_html = etree.HTML(resp)
            begin_content = x_html.xpath('//div[@id="contenttext"]/div/text()')
            center_content = x_html.xpath('//div[@id="contenttext"]/div/p/text()') or \
                             x_html.xpath('//div[@id="contenttext"]/div/div/text()')
            word_num = len("".join(begin_content).strip() + "".join(center_content).strip())
            content = "\r\n".join(begin_content) + "\r\n".join(center_content)
            if not content:
                logger.info("article content is img ...")
                return
            abstract = "".join(begin_content).strip()
            publish_time = "".join(x_html.xpath('//span[@class="shijian"]/text()')).strip()
            week = ""  # 没有星期几
            _date = publish_time.split("\r\n")[-1].strip().split(" ")[0].replace("年", "-").replace("月", "-"). \
                replace("日", "")
            editor = re.findall(r"记者(.*?)）", content) or \
                     re.findall(r"新华社记者(.*?)<br>", resp) or \
                     re.findall(r"本报记者(.*?)<BR>", resp)
            if not editor:
                editor = re.findall(r"新华社记者(.*)?", content)
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
                paper_name="新华每日电讯",
                abstract=abstract,  # 摘要
                contents=content,  # 内容
                crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")  # 爬取时间
            )
            SaveDataToEs.save_one_data_to_es(ALL_PAPER_DETAILS, data, article_id)
        except Exception as e:
            logger.exception(e)


def get_handler(*args, **kwargs):
    return XinHuaMeiRiDianXunSpider(*args, **kwargs)


def xin_hua_mei_ri_dian_xun_run():
    detail_list = []
    xin_hua = XinHuaMeiRiDianXunSpider({})
    data_list = xin_hua.get_begin_url()
    if data_list:
        for data in data_list:
            detail = xin_hua.get_news_detail(data)
            detail_list.append(detail)
        for detail_data in detail_list:
            xin_hua.parse_news_detail(detail_data)
        return dict(
            status=200,
            message="新华每日电讯采集成功",
        )
    else:
        return dict(
            status=-1,
            message="新华每日电讯没有发布新闻",
        )


if __name__ == '__main__':
    xin_hua_mei_ri_dian_xun_run()
