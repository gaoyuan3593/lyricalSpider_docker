import threading
from threading import Thread, Semaphore
from service import logger

__author__ = 'gaoyuan'

THREAD_JOIN_TIMEOUT = 1
MAX_THREADS_NUM = 100
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
