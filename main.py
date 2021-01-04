# _*_ coding: utf-8 _*_
__author__ = 'rentingsong'
__date__ = '2021/1/1 16:36'


import os
from flask import Flask
from flask import render_template
from flask import request
import webbrowser
from werkzeug.utils import secure_filename
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
        file1 = request.files["file1"]
        file2 = request.files["file2"]
        base_path = os.path.dirname(__file__)
        upload_path1 = os.path.join(base_path, 'static'+os.sep+'uploads', secure_filename(file1.filename))
        print("上传文件1：{0}".format(upload_path1))
        file1.save(upload_path1)
        upload_path2 = os.path.join(base_path, 'static'+os.sep+'uploads', secure_filename(file2.filename))
        print("上传文件2：{0}".format(upload_path2))
        file2.save(upload_path2)
        files_compare(upload_path1, upload_path2)
        out = base_path + os.sep + "templates" + os.sep + "file_compare" + os.sep + "out.html"
        webbrowser.open_new_tab(out)
        # 比对完记得把上传的文件清理掉
        if os.path.exists(upload_path1):
            os.remove(upload_path1)
        if os.path.exists(upload_path2):
            os.remove(upload_path2)
        return render_template('file_compare/file_compare.html')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
