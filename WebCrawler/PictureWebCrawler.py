# _*_ coding: utf-8 _*_
__author__ = 'rentingsong'
__date__ = '2020/11/15 21:13'
"""
功能：爬取一张图片
"""
import requests
import os


def get_picture(url):
    root = os.getcwd()
    path = root + os.sep + url.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                print("图片保存成功")
        else:
            print("图片已存在")
    except:
        return "爬取失败"


if __name__ == "__main__":
    url = "https://images.pexels.com/photos/2419006/pexels-photo-2419006.jpeg"  # 图片链接
    get_picture(url)

