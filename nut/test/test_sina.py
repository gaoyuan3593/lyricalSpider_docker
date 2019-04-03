# -*- coding: utf-8 -*-


from service.micro.referee import CASES_TYPE
from service.micro.referee.referees import CasesSpider


def test_referees_spider():
    cases_obj = CasesSpider(CASES_TYPE[0])
    cases_obj.product()
