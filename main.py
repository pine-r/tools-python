# _*_ coding: utf-8 _*_
__author__ = 'rentingsong'
__date__ = '2021/1/1 16:36'


from flask import Flask
from flask import render_template
from FileCompare import file_compare_blue
from ReplaceString import replace_string_blue
from WebCrawler import web_crawler_blue
from FishMom import fish_mom_blue

app = Flask(__name__)
# 注册比对工具
app.register_blueprint(file_compare_blue)
# 注册字符串替换工具
app.register_blueprint(replace_string_blue)
# 注册网络爬虫工具
app.register_blueprint(web_crawler_blue)
# 注册鱼妈妈小游戏
app.register_blueprint(fish_mom_blue)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
