#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random
import time
import re
import requests
from lxml import etree
from datetime import datetime
from bs4 import BeautifulSoup
from service.exception import retry
from service.exception.exceptions import *
from service import logger
from service.db.utils.elasticsearch_utils import ALL_PAPER_DETAILS, PAPER_ALL_MAPPING
from service.micro.news.utils.search_es import SaveDataToEs
from service.micro.news.utils.proxies_util import get_proxies

INDEX_TYPE = "paper_china_qing_nian_bao"

_index_mapping = {
    INDEX_TYPE:
        {
            "properties": PAPER_ALL_MAPPING
        }
}


class ChinaQingNianBaoSpider(object):
    __name__ = 'china qing nian bao news'

    def __init__(self, data):
        self.s = requests.session()
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Host": "zqb.cyol.com",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
        }
        SaveDataToEs.create_index(ALL_PAPER_DETAILS, _index_mapping)

    def random_num(self):
        return random.uniform(0.1, 0.5)

    def use_proxies(self):
        self.s.proxies = get_proxies()

    @retry(max_retries=5, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_begin_url(self):
        year = datetime.today().year
        _month = datetime.today().month
        _day = datetime.today().day
        month = str(_month) if len(str(_month)) >= 2 else "0{}".format(_month)
        day = str(_day) if len(str(_day)) >= 2 else "0{}".format(_day)
        url = "http://zqb.cyol.com/html/{}-{}/{}/nbs.D110000zgqnb_01.htm".format(year, month, day)
        try:
            resp = self.s.get(url, headers=self.headers, verify=False)
            resp.encoding = "utf-8"
            if resp.status_code == 200 and "要闻" in resp.text:
                soup = BeautifulSoup(resp.text, "lxml")
                li_list = soup.find("div", attrs={"id": "pageList"}).find_all("li")
                url_list = []
                for li in li_list:
                    href = li.find("a").attrs.get("href")
                    if href.startswith("."):
                        href = href[1:]
                    url = "http://zqb.cyol.com/html/{}-{}/{}/{}".format(year, month, day, href)
                    url_list.append(
                        dict(
                            url=url,
                            text=li.text.strip()
                        ))
                return url_list
        except Exception as e:
            logger.exception(e)
            self.use_proxies()
            raise HttpInternalServerError

    @retry(max_retries=5, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_news_all_url(self, url_dic):
        logger.info('Processing get zhong guo qing nian bao network search list!')
        data_list = []
        try:
            url = url_dic.get("url")
            response = self.s.get(url, headers=self.headers, verify=False)
            response.encoding = "utf-8"
            if "中国青年报" in response.text:
                soup = BeautifulSoup(response.text, "lxml")
                pdf_url = soup.find("div", attrs={"class": "ban"}).find("img").attrs.get("src").split("../")[-1]
                pdf = "http://zqb.cyol.com/{}".format(pdf_url)
                li_list = soup.find("div", attrs={"id": "titleList"}).find_all("li")
                for li in li_list:
                    title = li.text.strip()
                    date = re.findall(r"\d+-\d+/\d+", url)[0]
                    url = "http://zqb.cyol.com/html/{}/{}".format(date, li.find("a").attrs.get("href"))
                    column = url_dic.get("text").split("：")[1]
                    page = url_dic.get("text").split("：")[0]
                    data_list.append(
                        dict(
                            url=url,
                            title=title,
                            column=column,
                            page=page,
                            pdf=pdf,
                        )
                    )

            return data_list
        except Exception as e:
            raise InvalidResponseError

    @retry(max_retries=3, exceptions=(HttpInternalServerError, TimedOutError, InvalidResponseError), time_to_sleep=3)
    def get_news_detail(self, data):
        logger.info('Processing get china qing nian bao details !!!')
        url = data.get("url")
        try:
            response = self.s.get(url, headers=self.headers, verify=False)
            response.encoding = "utf-8"
            if response.status_code == 200:
                logger.info("get china qing nian bao news detail success url: {}".format(url))
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
            soup = BeautifulSoup(resp, "lxml")
            content = x_html.xpath('//div[@id="ozoom"]/p/text()')
            if not content:
                logger.info("article content is img ...")
                return
            abstract = "".join(content[0]).strip()
            _content = "\r\n".join(content[:-1]).strip()
            word_num = len("".join(content).strip())
            publish_time = "".join(re.findall(r"\d+年\d+月\d+日 星期.", soup.text)).strip()
            week = publish_time.split(" ")[-1]
            _date = publish_time.split(" ")[0].replace("年", "-").replace("月", "-").replace("日", "")
            editor = soup.find("div", attrs={"class": "lai"}).text.strip().split("来源")
            if editor:
                _editor = editor[0].strip()
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
                paper_name="中国青年报",
                abstract=abstract,  # 摘要
                contents=_content,  # 内容
                crawl_time=datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")  # 爬取时间
            )
            SaveDataToEs.save_one_data_to_es(ALL_PAPER_DETAILS, data, article_id)
        except Exception as e:
            logger.exception(e)


def get_handler(*args, **kwargs):
    return ChinaQingNianBaoSpider(*args, **kwargs)


def china_qing_nian_bao_run():
    data_list = []
    detail_list = []
    cn = ChinaQingNianBaoSpider({})
    url_list = cn.get_begin_url()
    if url_list:
        for url_dic in url_list:
            page_data = cn.get_news_all_url(url_dic)
            data_list.extend(page_data)
        for data in data_list:
            detail = cn.get_news_detail(data)
            detail_list.append(detail)
        for detail_data in detail_list:
            cn.parse_news_detail(detail_data)
        return dict(
            status=200,
            message="中国青年报采集成功",
        )
    else:
        return dict(
            status=-1,
            message="中国青年报没有发布新闻",
        )


if __name__ == '__main__':
    china_qing_nian_bao_run()
