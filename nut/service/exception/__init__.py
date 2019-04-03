#! /usr/bin/python3
# -*- coding: utf-8 -*-
import time
from functools import wraps


class GenericAppError(Exception):
    def __init__(self, err_code, msg, status_code=500, data=None):
        self.code = err_code
        self.message = msg
        self.data = data

        self.status_code = status_code

    def __str__(self):
        return '%s' % self.__class__

    def dict(self):
        return {
            'err_code': self.code,
            'err_msg': self.message,
            'data': self.data
        }

    def status_code(self):
        return self.status_code

RETRY_RETURN_NOTHING = 'nothing'


def retry(max_retries=3, exceptions=(), time_to_sleep=0, save_result=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            _max_retries = max_retries
            while _max_retries > 0:
                try:
                    wrapper.chances_left = _max_retries - 1
                    f = func(*args, **kwargs)
                    return f
                except exceptions as e:
                    _max_retries -= 1
                    if _max_retries == 0:
                        if save_result is not None:
                            if save_result == RETRY_RETURN_NOTHING:
                                return
                            return save_result.get_result()
                        raise e
                    time.sleep(time_to_sleep)
            return None
        return wrapper
    return decorator
