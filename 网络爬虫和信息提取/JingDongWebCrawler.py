# _*_ coding: utf-8 _*_
__author__ = 'rentingsong'
__date__ = '2020/11/15 20:39'
import requests


def get_JD_web(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text[:1000]
    except:
        return "爬取失败"


if __name__ == "__main__":
    url = "https://item.jd.com/100015287764.html"
    print(get_JD_web(url))
