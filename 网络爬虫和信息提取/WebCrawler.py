# _*_ coding: utf-8 _*_
__author__ = 'rentingsong'
__date__ = '2020/11/14 11:34'

import requests


def get_html_text(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 如果返回状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding  # 使返回解码正确
        return r.text
    except:
        return "产生异常"


if __name__ == "__main__":
    url = "http://www.baidu.com"
    print(get_html_text(url))
