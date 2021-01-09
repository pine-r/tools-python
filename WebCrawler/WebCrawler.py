# _*_ coding: utf-8 _*_
__author__ = 'rentingsong'
__date__ = '2020/11/14 11:34'
from flask import render_template
from WebCrawler import web_crawler_blue
# import requests


@web_crawler_blue.route('/web_crawler_index')
def web_crawler_index():
    return render_template('web_crawler/web_crawler_index.html')

# def get_html_text(url):
#     try:
#         r = requests.get(url, timeout=30)
#         r.raise_for_status()  # 如果返回状态不是200，引发HTTPError异常
#         r.encoding = r.apparent_encoding  # 使返回解码正确
#         return r.text
#     except:
#         return "产生异常"


if __name__ == "__main__":
    pass
    # url = "http://www.baidu.com"
    # print(get_html_text(url))
    #
    # # put方法
    # payload = {'key1': 'value1111', 'key2': 'value2222'}
    # r = requests.put("http://httpbin.org/put", data=payload)
    # print("put 字典", r.text)  # 提交一个字典，被存储到form字段下，但是会将原有的数据覆盖掉
    # r = requests.put("http://httpbin.org/put", data='ABC')
    # print("put 字符串", r.text)  # 提交一个字符串，被存储到data字段下,但是会将原有的数据覆盖掉
    #
    # # post方法使用
    # payload = {'key1': 'value1', 'key2': 'value2'}
    # r = requests.post("http://httpbin.org/post", data=payload)
    # print("post 字典", r.text)  # 提交一个字典，被存储到form字段下
    # r = requests.post("http://httpbin.org/post", data='DEF')
    # print("post 字符串", r.text)  # 提交一个字符串，被存储到data字段下
