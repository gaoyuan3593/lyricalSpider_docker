
import requests
from bs4 import BeautifulSoup

url = "http://www.dangjian.cn/"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
    'Proxy-Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}
resp = requests.get(url, headers=headers)
resp.encoding = "utf-8"

soup = BeautifulSoup(resp.text, "lxml")
div = soup.find("div", attrs={"class": "nav"}).find_all("a")
url_list = []
for i in div:
    print(i)
    href = i.attrs.get("href")
    text = i.text
    url_list.append(
        "{}   {}".format(href, text)
    )

print(url_list)