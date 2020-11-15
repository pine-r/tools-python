# _*_ coding: utf-8 _*_
__author__ = 'rentingsong'
__date__ = '2020/11/15 21:37'
"""
    功能： IP地址归属地自动查询
"""
import requests


def query_ip_attribution(url):
    h = {'User-Agent': "Mozilla/5.0"}
    try:
        r = requests.get(url + '202.204.80.112', headers=h)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text)
    except:
        print("获取失败")


if __name__ == "__main__":
    url = "http://m.ip138.com/iplookup.asp?ip="
    query_ip_attribution(url)
