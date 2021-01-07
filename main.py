# _*_ coding: utf-8 _*_
__author__ = 'rentingsong'
__date__ = '2021/1/1 16:36'


from flask import Flask
from flask import render_template
from FileCompare import file_compare_blue

app = Flask(__name__)
app.register_blueprint(file_compare_blue)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
