#! /usr/bin/python3
# -*- coding: utf-8 -*-
import json
import random
import time
import urllib.request
from datetime import datetime, date
from http.client import IncompleteRead
from urllib.parse import urlencode
import urllib3
import requests
import requests.adapters
from requests.exceptions import ProxyError, SSLError, Timeout, HTTPError

from service import logger
from service.core.utils.customerized_data_type import enum
from service.exception import retry
from service.exception.exceptions import *
from service.utils.yaml_tool import get_by_name_yaml

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.adapters.DEFAULT_RETRIES = 500


HTTP_METHODS = enum(
    get='GET',
    post='POST',
    put='PUT',
    delete='DELETE'
)

RESP_RETURN_TYPE = enum(
    plain_text='plain',
    object='obj'
)

SUBMISSION_TYPE = enum(
    json='json',
    form='form',
    encrypt='enc',
    text='text'
)

EMPTY_PARAMETER = {}
PICK_PROXY_PERCENT = 0.1
PICK_FEWEST_PROXIES = 10


class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%dT%H:%M:%SZ')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        return json.JSONEncoder.default(self, obj)


class NotRedirctHandler(urllib.request.HTTPRedirectHandler):
    def __init__(self):
        pass

    def http_error_301(self, req, fp, code, msg, headers):
        pass

    def http_error_302(self, req, fp, code, msg, headers):
        return fp


class HTTPAdapter(requests.adapters.HTTPAdapter):
    def proxy_headers(self, proxy):
        headers = super(HTTPAdapter, self).proxy_headers(proxy)
        if hasattr(self, 'tunnel'):
            headers['Proxy-Tunnel'] = self.tunnel
        return headers


class Requester(object):
    HTTP_TIMEOUT = 10
    DEFAULT_HTTP_TIMEOUT_INCREASING_RATE = 1
    HTTP_TIMEOUT_INCREASING_RATE = 2

    def cal_next_timeout(self, is_last_access_ok):
        if is_last_access_ok:
            self.current_timeout_rate = self.DEFAULT_HTTP_TIMEOUT_INCREASING_RATE
        else:
            self.current_timeout_rate *= self.HTTP_TIMEOUT_INCREASING_RATE

        self.next_http_timeout = max(self.timeout or 1, self.HTTP_TIMEOUT * self.current_timeout_rate)

    def __init__(self, proxy_category='default', cookie=None, timeout=None, verify=False, proxy_tunnel=None,
                 seq_no=None):
        self.s = requests.session()
        self.verify = verify

        if cookie:
            self.s.cookies = cookie

        self.proxy_category = proxy_category
        self.timeout = timeout
        self.proxy_tunnel = proxy_tunnel

        self.current_timeout_rate = 1
        if timeout:
            self.next_http_timeout = max(timeout, self.HTTP_TIMEOUT)
        else:
            self.next_http_timeout = self.HTTP_TIMEOUT

        if self.proxy_tunnel:
            ha = HTTPAdapter()
            ha.tunnel = self.proxy_tunnel
            self.s.mount("https://", ha)

    def cookie(self):
        return requests.utils.dict_from_cookiejar(self.s.cookies)

    def clear_cookie(self):
        self.s.cookies.clear()

    def use_proxy(self, proxy=None):
        if proxy:
            proxies = proxy
        else:
            conf = get_by_name_yaml("proxy")
            proxym_meta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
                "host": conf["host"],
                "port": conf["port"],
                "user": conf["user"],
                "pass": conf["password"],
            }
            proxies = {'http': proxym_meta, 'https': proxym_meta}

        self.s.proxies = proxies

    @retry(max_retries=3, exceptions=(ConnectionResetError, TimedOutError, IncompleteRead,
                                      ServiceUnavailableError, BadRequestError), time_to_sleep=1)
    def get(self, url, header_dict=None, params=EMPTY_PARAMETER, is_not_redirct=True, stream=False):
        logger.info('GET {}'.format(url))
        try:
            resp = self.s.get(url, headers=header_dict, params=params, allow_redirects=is_not_redirct,
                              timeout=self.next_http_timeout, verify=self.verify, stream=stream)
            self.cal_next_timeout(True)
            self.exception(resp.status_code)

            return resp
        except (ProxyError, SSLError, HTTPError, Timeout) as e:
            time.sleep(random.uniform(1, 2))
            logger.exception('http get exception: {}'.format(url))
            raise e

    @retry(max_retries=3, exceptions=(ConnectionResetError, TimedOutError, IncompleteRead,
                                      ServiceUnavailableError, BadRequestError), time_to_sleep=1)
    def post(self, url, header_dict=None, data_dict='', submission_type=SUBMISSION_TYPE.form, is_not_redirct=False):
        logger.info('POST {}'.format(url))
        try:
            if submission_type == SUBMISSION_TYPE.json:
                resp = self.s.post(url, headers=header_dict, json=data_dict, allow_redirects=is_not_redirct,
                                   timeout=self.next_http_timeout,
                                   verify=self.verify)
            else:
                resp = self.s.post(url, headers=header_dict, data=data_dict, allow_redirects=is_not_redirct,
                                   timeout=self.next_http_timeout,
                                   verify=self.verify)

            self.cal_next_timeout(True)
            self.exception(resp.status_code)
            return resp
        except Exception as e:
            logger.exception('http post exception: {}'.format(url))
            raise e

    @retry(max_retries=3, exceptions=(ConnectionResetError, TimedOutError, IncompleteRead,
                                      ServiceUnavailableError, BadRequestError), time_to_sleep=1)
    def put(self, url, header_dict=None, data_dict='', is_not_redirct=False):
        logger.info('PUT {}'.format(url))
        try:
            resp = self.s.put(url, headers=header_dict, data=data_dict, allow_redirects=is_not_redirct,
                              timeout=self.next_http_timeout,
                              verify=self.verify)

            self.cal_next_timeout(True)
            self.exception(resp.status_code)
            return resp
        except Exception as e:
            logger.exception('http put exception: {}'.format(url))
            raise e

    def exception(self, status_code):
        if status_code in [200, 204]:
            pass
        elif status_code in [429, 407]:
            time.sleep(random.uniform(0.5, 1.5))
            self.use_proxy()
        elif status_code in [400, 401, 402, 403, 404, 405, 406, 409, 410, 411, 412, 413, 414,
                             415, 416, 417, 418, 421, 422, 423, 424, 425, 426, 428, 431, 444,
                             449, 450, 451, 499, 500, 503, 507, 510, 511]:
            self.use_proxy()
            raise ServiceUnavailableError()
        elif status_code in [408, 504]:
            self.use_proxy()
            raise TimedOutError()

    @classmethod
    def generate_query_string(cls, url, data_dict):
        return '{}?{}'.format(url, urlencode(data_dict).encode("utf-8"))


if __name__ == '__main__':
    req = Requester()
    k = req.get('https://www.baidu.com', params=dict(a=2))
    print(k.text)
    print(k.headers)
    print(k.cookies)
    resp = req.put('http://httpbin.org/put', {'key': 'value'})
    print(resp.text)
    print(resp.headers)
    print(resp.cookies)
