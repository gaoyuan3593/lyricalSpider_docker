#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Required
- requests (必须)
- rsa (必须)
- pillow (可选)
Info

'''
import time
import base64
import rsa
import binascii
import requests
import re
import random
import json

from bs4 import BeautifulSoup
from requests.cookies import RequestsCookieJar

try:
    from PIL import Image
except:
    pass
try:
    from urllib.parse import quote_plus
except:
    from urllib import quote_plus

'''
如果没有开启登录保护，不用输入验证码就可以登录
如果开启登录保护，需要输入验证码
'''

# 构造 Request headers
agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0'
headers = {
    'User-Agent': agent
}

session = requests.session()


def str_int(_str):
    if _str.split(" ")[1].isdigit():
        return int(_str.split(" ")[1])
    return None


def get_su(username):
    """
    对 email 地址和手机号码 先 javascript 中 encodeURIComponent
    对应 Python 3 中的是 urllib.parse.quote_plus
    然后在 base64 加密后decode
    """
    username_quote = quote_plus(username)
    username_base64 = base64.b64encode(username_quote.encode("utf-8"))
    return username_base64.decode("utf-8")


# 预登陆获得 servertime, nonce, pubkey, rsakv
def get_server_data(su):
    pre_url = "http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su="
    pre_url = pre_url + su + "&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.18)&_="
    pre_url = pre_url + str(int(time.time() * 1000))
    pre_data_res = session.get(pre_url, headers=headers)

    sever_data = eval(pre_data_res.content.decode("utf-8").replace("sinaSSOController.preloginCallBack", ''))

    return sever_data


def get_password(password, servertime, nonce, pubkey):
    rsaPublickey = int(pubkey, 16)
    key = rsa.PublicKey(rsaPublickey, 65537)  # 创建公钥
    message = str(servertime) + '\t' + str(nonce) + '\n' + str(password)  # 拼接明文js加密文件中得到
    message = message.encode("utf-8")
    passwd = rsa.encrypt(message, key)  # 加密
    passwd = binascii.b2a_hex(passwd)  # 将加密信息转换为16进制。
    return passwd


def get_cha(pcid):
    cha_url = "http://login.sina.com.cn/cgi/pin.php?r="
    cha_url = cha_url + str(int(random.random() * 100000000)) + "&s=0&p="
    cha_url = cha_url + pcid
    cha_page = session.get(cha_url, headers=headers)
    with open("cha.jpg", 'wb') as f:
        f.write(cha_page.content)
        f.close()
    try:
        im = Image.open("cha.jpg")
        im.show()
        im.close()
    except:
        print(u"请到当前目录下，找到验证码后输入")


def login(username, password):
    # su 是加密后的用户名
    su = get_su(username)
    sever_data = get_server_data(su)
    servertime = sever_data["servertime"]
    nonce = sever_data['nonce']
    rsakv = sever_data["rsakv"]
    pubkey = sever_data["pubkey"]
    showpin = sever_data["showpin"]
    password_secret = get_password(password, servertime, nonce, pubkey)

    postdata = {
        'entry': 'weibo',
        'gateway': '1',
        'from': '',
        'savestate': '7',
        'useticket': '1',
        'pagerefer': "http://login.sina.com.cn/sso/logout.php?entry=miniblog&r=http%3A%2F%2Fweibo.com%2Flogout.php%3Fbackurl",
        'vsnf': '1',
        'su': su,
        'service': 'miniblog',
        'servertime': servertime,
        'nonce': nonce,
        'pwencode': 'rsa2',
        'rsakv': rsakv,
        'sp': password_secret,
        'sr': '1366*768',
        'encoding': 'UTF-8',
        'prelt': '115',
        'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
        'returntype': 'META'
    }
    login_url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)'
    if showpin == 0:
        login_page = session.post(login_url, data=postdata, headers=headers)
    else:
        pcid = sever_data["pcid"]
        get_cha(pcid)
        postdata['door'] = input("请输入验证码")
        login_page = session.post(login_url, data=postdata, headers=headers)
    login_loop = (login_page.content.decode("GBK"))
    pa = r'location\.replace\([\'"](.*?)[\'"]\)'
    loop_url = re.findall(pa, login_loop)[0]
    login_index = session.get(loop_url, headers=headers)
    uuid = login_index.text
    uuid_pa = r'"uniqueid":"(.*?)"'
    uuid_res = re.findall(uuid_pa, uuid, re.S)[0]
    web_weibo_url = "http://weibo.com/%s/profile?topnav=1&wvr=6&is_all=1" % uuid_res
    response = session.get(web_weibo_url, headers=headers)
    weibo_pa = r'<title>(.*?)</title>'
    user_id = re.findall(weibo_pa, response.content.decode("utf-8", 'ignore'), re.S)[0]
    print(user_id)


def write_file(data):
    print("正在写文件")
    with open("weibo1.json", "a", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False) + "\n")
    return True


def search_result(data, user_id=None):
    data_list, original_weibo, comment_data = [], "", []
    time.sleep(3)
    url = "https://s.weibo.com/weibo?q=%s&typeall=1&suball=1&Refer=g" % (data)
    respone = session.get(url=url, verify=False)
    resp = BeautifulSoup(respone.text, 'html.parser')
    raw_data = resp.find_all("div", attrs={"class": "card-wrap"})[:20]
    count = 1
    for raw in raw_data:
        print("爬取第 {} 条微博！！！！".format(count))
        r_data = raw.contents[1]
        is_forward = r_data.find_all("div", attrs={"class": "con"})
        if len(is_forward):
            original_weibo = is_forward[0].text.strip()
        try:
            weibo = r_data.find_all("p", attrs={"class": "from"})[0]
            weibo_num = r_data.find_all("div", attrs={"class": "card-act"})[0].contents[1].find_all("li")[1:]
            com_num = str_int(weibo_num[1].text)
            if com_num:
                comment_data = get_com_user_data(weibo_num[0])
            raw_id = raw.contents[1].contents[1].contents[5].find_all("a", {"class": "name"})[0]
            resp_dada = dict(
                weibo_time=weibo.contents[1].text.strip(),  # 发微时间
                platform=weibo.contents[3].text.strip() if len(weibo) > 3 else "",  # 平台
                contents=r_data.find_all("p", attrs={"class": "txt"})[0].text.strip(),  # 内容
                weibo_id=raw_id.text,  # 微博id
                user_id=raw_id.attrs.get("href").split("/")[3].split("?")[0],  # 用户id
                like_num=str_int(weibo_num[2].text),  # 点赞数
                com_num=com_num,  # 评论数
                forward_num=str_int(weibo_num[0].text),  # 转发数
                is_forward="是" if is_forward else "否",  # 是否转发
                original_weibo=original_weibo,  # 转发原微博
                comment=comment_data
            )
            data_list.append(resp_dada)
            count += 1
        except Exception as e:
            print("出错了 e: {}".format(e))
            continue
    is_ok = write_file(data_list)
    if is_ok:
        print("写入成功！！！")


def get_user_info(user_data):
    """
    获取个人信息
    :param user_data:
    :return: dict
    """
    url = user_data.get("user_url")
    user_id = user_data.get("user_id")
    time.sleep(1)
    resp = session.get(url)
    value = resp.text.split('"value":"')[1].split('"}]')[0]
    url = "https://m.weibo.cn/api/container/getIndex?uid={}&type=uid&value={}".format(user_id, value)
    resp = session.get(url)
    data = json.loads(resp.text)
    if data.get("ok") == 0:
        return []
    con_id, user_info = None, {}
    fan_data = data.get("data").get("userInfo")
    con_id_list = data.get("data").get("tabsInfo").get("tabs")
    for i in con_id_list:
        if i.get("tab_type") == "profile":
            con_id = i.get("containerid")
            continue
    fan_count = fan_data.get("followers_count")  # 粉丝数
    follow_count = fan_data.get("follow_count")  # 关注数
    profile_image_url = fan_data.get("profile_image_url")  # 头像地址
    user_name = fan_data.get("screen_name")  # 用户名
    containerid = con_id + "_-_INFO"
    url = "https://m.weibo.cn/api/container/getIndex?uid={}&type=uid&value={}&containerid={}".format(user_id, value,
                                                                                                     containerid)
    time.sleep(2)
    resp = session.get(url).json()
    if resp.get("ok") == 0:
        return []
    resp_data = resp.get("data").get("cards")[0:2]
    city, gender, introduction = "", "", ""  # 所在地 性别 简介
    for i in resp_data:
        for k in i.get("card_group"):
            if k.get("item_name") == "简介":
                introduction = k.get("item_content")
            if k.get("item_name") == "性别":
                gender = k.get("item_content")
            if k.get("item_name") == "所在地":
                city = k.get("item_content")
        user_info = dict(introduction=introduction, gender=gender, city=city)
    user_info.update(
        user_id=user_id,
        fan_count=fan_count,
        follow_count=follow_count,
        profile_image_url=profile_image_url,
        user_name=user_name,
    )
    return user_info


def get_com_user_data(com_num):
    if not com_num:
        return com_num
    data_list = []
    mid = com_num.contents[0].attrs.get("action-data").split("mid=")[1].split("&")[0]
    url = "https://m.weibo.cn/api/comments/show?id={}".format(mid)
    time.sleep(2)
    resp = session.get(url).text
    com_data = json.loads(resp)
    if com_data.get("ok") == 0:
        return []
    comment_data = com_data.get("data").get("data")
    for data in comment_data:
        resp_dada = dict(
            weibo_time=data.get("created_at"),  # 评论时间
            platform=data.get("user").get("platform", ""),  # 平台
            comment_contents=data.get("text"),  # 评论内容
            weibo_id=mid,  # 原微博id
            commet_id=data.get("id"),  # 评论id
            user_id=data.get("user").get("id"),  # 用户id
            user_name=data.get("user").get("screen_name"),  # 用户名
            user_url=data.get("user").get("profile_url")
        )
        user_info = get_user_info(resp_dada)
        comment_dic = dict(
            comment_user=user_info,
            comment_data=resp_dada
        )
        data_list.append(comment_dic)

    return data_list


if __name__ == "__main__":
    username = "mwpd2x21iwa8@game.weibo.com"
    password = "a3jlg8pd6"

    from random import choice
    #login(username, password)
    # zi = ["契合", "黄土高坡", "桂林", "海南岛", "事故", "打官司", "狗不理 包子", "标志性建筑", "打人误伤", "扶老奶奶过马路",
    #       "黑龙江经济", "全国GDP", "人民币汇率", "工业行情", "人与人之间", "历史人物", "王安石", "赵构", "大唐", "宋朝"]

    zi = ["绿色改变中国"]
    while True:
        try:
            ci = choice(zi)
            print("关键词   {}".format(ci))
            time.sleep(3)
            search_result(ci)
        except:
            continue
