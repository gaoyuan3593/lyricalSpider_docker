#! /usr/bin/python3
# -*- coding: utf-8 -*-
from service.exception import GenericAppError


class BadRequestError(GenericAppError):
    def __init__(self, err_code=50068, msg='请求错误!', status_code=200):
        self.code = err_code
        self.message = msg

        self.status_code = status_code


class InvalidResponseError(GenericAppError):
    def __init__(self, err_code=500003, msg='响应无效!', status_code=200):
        self.code = err_code
        self.message = msg
        self.status_code = status_code


class TimedOutError(GenericAppError):
    def __init__(self, err_code=50004, msg=u'网络请求超时!', status_code=200):
        self.code = err_code
        self.message = msg

        self.status_code = status_code


class ServiceUnavailableError(GenericAppError):
    def __init__(self, err_code=50053, msg='服务暂时不可用', status_code=200):
        self.code = err_code
        self.message = msg

        self.status_code = status_code

#
# class CaptchaVerifiedError(GenericAppError):
#     def __init__(self, err_code=50005, msg=u'图形验证码错误!', data=None, status_code=200):
#         self.code = err_code
#         self.message = msg
#         self.data = data
#
#         self.status_code = status_code
#
#