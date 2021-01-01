# _*_ coding: utf-8 _*_
__author__ = 'rentingsong'
__date__ = '2021/1/1 16:36'

from flask import Flask
from flask import render_template
from flask import request
from FileCompare.FileCompare import files_compare

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/file_compare')
def file_compare():
    return render_template('file_compare/file_compare.html')


@app.route('/file_compare_result', methods=['GET', 'POST'])
def file_compare_result():
    # if request.method == "GET":
    #     file1 = request.args.get("file1", "")
    #     file2 = request.args.get("file2", "")
    #     return render_template('file_compare/file_compare_result.html', file1=file1, file2=file2)
    if request.method == "POST":
        file1 = request.form["file1"]
        file2 = request.form["file2"]
        files_compare(file1, file2)
        return render_template('file_compare/out.html')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
