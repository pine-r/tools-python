# _*_ coding: utf-8 _*_
__author__ = 'rentingsong'
__date__ = '2020/11/15 21:04'
"""
功能：百度、360搜索关键词提交
"""
import requests


def get_search_result(url):
    try:
        kv = {'wd': 'Python'}  # 百度搜关键词Python
        # kv = {'q': 'Python'}  # 360搜关键词Python
        r = requests.get(url, params=kv)
        print(r.request.url)  # 获取请求的url
        r.raise_for_status()
        print(len(r.text))
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "爬取失败"


if __name__ == "__main__":
    url = "http://www.baidu.com/s"   # 百度搜索接口，构建参数时使用wd
    # url = "http://www.so.com/s"    # 360搜索接口，构建参数时使用q
    print(get_search_result(url))

