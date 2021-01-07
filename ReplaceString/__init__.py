# _*_ coding: utf-8 _*_
__author__ = 'rentingsong'
__date__ = '2021/1/7 21:54'
from flask import Blueprint
replace_string_blue = Blueprint('ReplaceString', __name__)
from ReplaceString import ReplaceFileString
