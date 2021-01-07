# _*_ coding: utf-8 _*_
__author__ = 'rentingsong'
__date__ = '2021/1/1 21:37'
# 创建蓝图
from flask import Blueprint

file_compare_blue = Blueprint('FileCompare', __name__)


from FileCompare import FileCompare
