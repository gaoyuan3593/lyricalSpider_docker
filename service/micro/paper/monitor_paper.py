#! /usr/bin/python3
# -*- coding: utf-8 -*-

import multiprocessing
from service import logger
from service.utils.seq_no import generate_seq_no


class MonitorPaper(object):
    __name__ = " monitor paper"

    def __init__(self, data):
        self.data = data
        self.seq_no = generate_seq_no()

    def query(self):
        logger.info("Begin monitor paper query run ...")
        result = self.get_monitor_paper()
        return dict(
            status=200,
            result=result,
            message="success",
        )

    def get_monitor_paper(self):
        logger.info("Begin get all paper detail ...")
        data_list = []
        try:
            from service.micro.paper.tj_ri_bao import tian_jin_ri_bao_run
            from service.micro.paper.china_qing_nian_bao import china_qing_nian_bao_run
            from service.micro.paper.guang_ming_ri_bao import guang_ming_ri_bao_run
            from service.micro.paper.jin_wan_bao import jin_wan_bao_run
            from service.micro.paper.jing_ji_ri_bao import jing_ji_ri_bao_run
            from service.micro.paper.mkdx import xin_hua_mei_ri_dian_xun_run
            from service.micro.paper.ren_min_ri_bao import ren_min_ri_bao_run
            func_list = [tian_jin_ri_bao_run, china_qing_nian_bao_run, guang_ming_ri_bao_run, jing_ji_ri_bao_run,
                         jin_wan_bao_run, xin_hua_mei_ri_dian_xun_run, ren_min_ri_bao_run]
            for func in func_list:
                result = func()
                data_list.append(result)
            logger.info("paper get data success seq_no: {}".format(self.seq_no))
            return data_list
        except Exception as e:
            logger.exception(e)
            return data_list


def get_handler(*args, **kwargs):
    return MonitorPaper(*args, **kwargs)


if __name__ == '__main__':
    data = {"status": "1", "relative_word": "dasfasdf,", }
    s = MonitorPaper(data)
    s.query()