# _*_ coding: utf-8 _*_
__author__ = 'rentingsong'
__date__ = '2020/11/15 20:52'
import requests


def get_amazon_web(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}  # 模拟浏览器访问
        r = requests.get(url, headers=kv)
        print(r.request.headers)  # 查看发给Amazon请求的headers
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text[1000:2000]
    except:
        return "爬取失败"


if __name__ == "__main__":
    url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
    print(get_amazon_web(url))
