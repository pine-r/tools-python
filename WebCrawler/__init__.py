# _*_ coding: utf-8 _*_
__author__ = 'rentingsong'
__date__ = '2021/1/9 10:42'
from flask import Blueprint

web_crawler_blue = Blueprint('WebCrawler', __name__)

from WebCrawler import WebCrawler
from WebCrawler import AmazonWebCrawler
from WebCrawler import BaiduKeySearch