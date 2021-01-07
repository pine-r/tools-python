# _*_ coding: utf-8 _*_
__author__ = 'rentingsong'
__date__ = '2020/12/29 21:45'
"""
function: 比较两个文件的差异
version: v1.0 将文件格式化，每一行不超过80字符（可自定义），并展示两个文件之间的差异
"""
import difflib
import os
import webbrowser
from flask import render_template
from flask import request
from werkzeug.utils import secure_filename
from FileCompare import file_compare_blue


def line_wrapping_string(string, chars=80):
    tmp = ''
    len_str = len(string)
    if len_str <= chars:
        tmp = string
        return tmp
    while len_str > chars:
        tmp = tmp + string[0:chars] + '\n'
        string = string[chars:]
        len_str = len(string)
    return tmp + string


def line_wrapping_file(file):
    with open(file, 'r+', encoding='UTF-8') as f:
        lines = f.readlines()
    with open(file, 'r+', encoding='UTF-8') as f:
        for line in lines:
            line = line_wrapping_string(line)
            f.write(line)


def files_compare(file1, file2):
    hd = difflib.HtmlDiff()
    line_wrapping_file(file1)
    line_wrapping_file(file2)
    file1_content = ''
    file2_content = ''
    with open(file1, 'r', encoding='UTF-8') as f1:
        file1_content = f1.readlines()
    with open(file2, 'r', encoding='UTF-8') as f2:
        file2_content = f2.readlines()
    out = os.path.abspath('.')[:27] + os.sep + "templates" + os.sep + "file_compare" + os.sep + "out.html"
    with open(out, 'w+', encoding='UTF-8') as fo:
        fo.write(hd.make_file(file1_content, file2_content, fromdesc=file1.split(os.sep)[-1],
                              todesc=file2.split(os.sep)[-1]))
    # webbrowser.open_new_tab('out.html')


@file_compare_blue.route('/file_compare')
def file_compare():
    return render_template('file_compare/file_compare.html')


@file_compare_blue.route('/file_compare_result', methods=['GET', 'POST'])
def file_compare_result():
    # if request.method == "GET":
    #     file1 = request.args.get("file1", "")
    #     file2 = request.args.get("file2", "")
    #     return render_template('file_compare/file_compare_result.html', file1=file1, file2=file2)
    if request.method == "POST":
        file1 = request.files["file1"]
        file2 = request.files["file2"]
        base_path = os.path.dirname(__file__).rsplit(os.sep, 1)[0]
        upload_path1 = os.path.join(base_path, 'static'+os.sep+'uploads' + os.sep + 'first', secure_filename(file1.filename))
        print("上传文件1：{0}".format(upload_path1))
        file1.save(upload_path1)
        upload_path2 = os.path.join(base_path, 'static'+os.sep+'uploads' + os.sep + 'second', secure_filename(file2.filename))
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


if __name__ == '__main__':
    pass
    # file1 = os.path.abspath('.') + os.sep + "file1.txt"
    # file2 = os.path.abspath('.') + os.sep + "file2.txt"
    # print(os.path.abspath('.')[:27] + "templates" + os.sep + "file_compare" + os.sep + "out.html")
    # file_compare1(file1, file2)
