#! /usr/bin/python3
# -*- coding: utf-8 -*-


import requests

url = "https://twitter.com/realDonaldTrump"
#url = "http://ip138.com/"

resp = requests.get(url, verify=False)
resp.encoding = "utf-8"
print(resp.headers)
print(resp.text)