import threading
from threading import Thread, Semaphore
from service import logger

__author__ = 'gaoyuan'

THREAD_JOIN_TIMEOUT = 1
MAX_THREADS_NUM = 10000
threads_sem = Semaphore(MAX_THREADS_NUM)


class WorkerThread(Thread):
    def __init__(self, raw_data_list, func, args=None):
        super(WorkerThread, self).__init__()
        self.raw_data_list = raw_data_list
        self.func = func
        self.args = args

    def start(self):
        logger.info('Before running active threading count: {}'.format(threading.active_count()))
        threads_sem.acquire()
        super(WorkerThread, self).start()

    def run(self):
        import logbook
        with logbook.Processor():
            try:
                ret = self.func(*self.args)
                if ret and isinstance(ret, dict):
                    self.raw_data_list.append(ret)
                elif ret and isinstance(ret, list):
                    self.raw_data_list.extend(ret)
            finally:
                logger.info('After running active threading count: {}'.format(threading.active_count()))
                threads_sem.release()


class ThreadedSpider(object):
    def __init__(self, spider):
        self.spider = spider


    def crawl(self):
        start = int(time.time())

        logger.info('Starting {} spider threaded handling: '.format(self.spider.__name__))

        wb = self.spider (url)
        threads = []
        data_list, page_data_url_list = [], []
        html_list, wb_data_list = [], []
        weibo_detail_list, comment_or_repost_list = [], []
        com_or_re_data_list, user_id_list = [], []
        user_info_list = []
        keyword = url.split("q=")[1].split("&")[0]
        data = wb.get_weibo_page_data(url, keyword)

        # 解析每个热搜的所有页的url
        page_data_url_list.extend(wb.parse_weibo_page_url(data))
        if len(page_data_url_list) >= 10:
            for page_url_data in page_data_url_list:
                # 获取每页内容的html
                worker = WorkerThread(html_list, wb.get_weibo_data, (page_url_data,))
                worker.start()
                threads.append(worker)
            for work in threads:
                work.join()
            threads = []
        else:
            for page_url_data in page_data_url_list:
                html_list.append(wb.get_weibo_data(page_url_data))
        if len(html_list) >= 10:
            for html_data in html_list:
                # 解析每页的20微博内容
                worker = WorkerThread(wb_data_list, wb.parse_weibo_html, (html_data,))
                worker.start()
                threads.append(worker)
            for work in threads:
                work.join()
            threads = []
        else:
            for html_data in html_list:
                wb_data_list.append(wb.parse_weibo_html(html_data))

        for wb_data in wb_data_list:
            # 解析微博详情
            if not wb_data:
                continue
            keyword = wb_data.get("keyword")
            for data in wb_data.get("data"):
                worker = WorkerThread(weibo_detail_list, wb.parse_weibo_detail, (data, keyword))
                worker.start()
                threads.append(worker)
            for work in threads:
                work.join()
            threads = []

        # 发布微博的信息存入es
        # wb.save_data_to_es(list(filter(None, weibo_detail_list)))

        comment_url_list, repost_url_list = wb.parse_comment_or_repost_url(weibo_detail_list)

        if comment_url_list or repost_url_list:
            for data in comment_url_list:  # 所有评论url
                weibo_id = data.get("weibo_id")
                user_id = data.get("user_id")
                for url in data.get("url_list"):
                    worker = WorkerThread(comment_or_repost_list, wb.get_comment_data, (url, weibo_id, user_id))
                    worker.start()
                    threads.append(worker)
                for work in threads:
                    work.join()
                threads = []
            for data in repost_url_list:  # 所有转发url
                weibo_id = data.get("weibo_id")
                user_id = data.get("user_id")
                for url in data.get("url_list"):
                    worker = WorkerThread(comment_or_repost_list, wb.get_repost_data, (url, weibo_id, user_id))
                    worker.start()
                    threads.append(worker)
                for work in threads:
                    work.join()
                threads = []
        # 解析所有评论和转发信息，评论和转发用户ld列表
        for data in comment_or_repost_list:
            if not data:
                continue
            if data.get("type") == "comment_type":
                comment_data_list, comment_user_id_list = wb.parse_comment_data(data)
                com_or_re_data_list.extend(comment_data_list)
                user_id_list.extend(comment_user_id_list)
            elif data.get("type") == "repost_type":
                repost_data_list, repost_user_id_list = wb.parse_repost_data(data)
                com_or_re_data_list.extend(repost_data_list)
                user_id_list.extend(repost_user_id_list)
        # 评论和转发信息存入es
        # wb.save_data_to_es(com_or_re_data_list)

        # 获取用户个人信息
        for uid in user_id_list:
            worker = WorkerThread(user_info_list, wb.get_user_info, (uid,))
            worker.start()
            threads.append(worker)
        for work in threads:
            work.join()
        threads = []
        # 用户信息存入es
        wb.save_data_to_es_lists(user_info_list)
        return True

        logger.info('{} handle is done for DATA CRAWLING in {} seconds mobile: {}, seq_no: {}.'
                    .format(self.spider.__name__, int(time.time()) - start, self.mobile, self.seq_no))

        return to_mongo_bag



if __name__ == '__main__':
    import time


    def test(i):
        time.sleep(2)


    print(id(threads_sem))
    threads = []
    count = 0

    for i in range(1, 100):
        worker = WorkerThread([], test, (i,))
        try:
            worker.start()
        except Exception as e:
            print(count)
            raise e
        count += 1
        threads.append(worker)

    for t in threads:
        t.join()
