# coding: utf-8
from service import logger
import re
import json
import requests
import base64
import urllib3
from service.core.config.redis_ import REDIS

from service.micro.utils.math_utils import str_to_int
from service.utils.yaml_tool import get_by_name_yaml

__auhtor__ = 'Yuan Gao'

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
NAME = "kuai_proxy"


def abstract_protocal(ip):
    protocal = 'http'
    if re.search(r'^http://', ip):
        protocal = 'http'
    elif re.search(r'^https://', ip):
        protocal = 'https'
    return protocal


def get_redis_proxy_choice():
    from service.core.config.redis_ import kuai_proxy_redis_cli
    name = kuai_proxy_redis_cli.get('use_train_proxy_pool')
    return True if str_to_int(name) else False


def get_kuai_proxy():
    conf = get_by_name_yaml("kuaiproxy")
    url = "{}?orderid={}&num=3&f_loc=1&f_et=1&format=json".format(conf["host"], conf["orderid"])
    rep = requests.get(url, verify=False)
    if rep.status_code == 200:
        json_info = rep.json().get("data").get("proxy_list")
        logger.info(json_info)
    else:
        json_info = None
    return json_info


def get_proxy_pool():
    server_info_list = []
    json_info = get_redis_proxy_pool()
    if json_info and isinstance(json_info, list):
        conf = get_by_name_yaml("kuaiproxy")
        for address in json_info:
            server_info = "%(user)s:%(pwd)s@%(proxy)s/" % {
                "user": conf["user"],
                "pwd": conf["password"],
                "proxy": address}
            server_info_list.append(server_info)
    return server_info_list


def retrun_redis_cli():
    import redis

    return redis.StrictRedis(host=REDIS['host'], port=REDIS['port'], password=REDIS['password'], db=3,
                             decode_responses=True)


def set_redis_proxy_pool(_time, ips):
    cli = retrun_redis_cli()
    cli.set(NAME, json.dumps(ips))
    cli.expire(NAME, _time)


def get_redis_proxy_pool():
    cli = retrun_redis_cli()
    value = cli.get(NAME)
    if value:
        return json.loads(value)
    else:
        json_info = get_kuai_proxy()
        _time, ip_list = parse_min_time_data(json_info)
        set_redis_proxy_pool(_time, ip_list)
        return ip_list


def parse_min_time_data(_parm):
    if not _parm:
        pass
    ip_list, time_list = [], []
    if isinstance(_parm, list):
        for i in _parm:
            _ip, _time = i.split(",")[0], i.split(",")[2]
            ip_list.append(_ip)
            time_list.append(_time)

    return min(time_list), ip_list


if __name__ == '__main__':
    for i in range(100):
        get_proxy_pool()
    "duoiphndrabdz:PFIolGQmc1zn9@ip2.hahado.cn:41281"
    # "duoiprwrrpznw:38DMh3TUNydgw@ip2.hahado.cn:41051"
    # "vzebgnsnh:Q18y2O4ZfitXC@ip2.hahado.cn:41838"
    #
    # add_consul_proxy("stable", "ip2.hahado.cn", "41281", "duoiphndrabdz", "PFIolGQmc1zn9")
    # add_consul_proxy("stable", "ip2.hahado.cn", "41051", "duoiprwrrpznw", "38DMh3TUNydgw")
    # add_consul_proxy("stable", "ip2.hahado.cn", "41838", "vzebgnsnh", "Q18y2O4ZfitXC")
    # proxy_pool_http = get_redis_proxy_pool('https')
    # set_redis_proxy_pool('https://vaxfrkjuh:F1x41OnjnGp3U@ip2.hahado.cn:39755')
    # print proxy_pool_http
    # print get_redis_proxy_pool('http')
    # rem_redis_proxy_pool('https://vaxfrkjuh:F1x41OnjnGp3U@ip2.hahado.cn:39755')
    # P = PrivateProxy(proxy_pool_http[0])
    # print time.time()
    # print P.proxy_get_current_ip()
    # P.proxy_change_ip()
    # while True:
    #     print P.proxy_get_current_ip()
    #     time.sleep(60)
