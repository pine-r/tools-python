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
    with open(file, 'r+') as f:
        lines = f.readlines()
    with open(file, 'r+') as f:
        for line in lines:
            line = line_wrapping_string(line)
            f.write(line)


def file_compare(file1, file2):
    hd = difflib.HtmlDiff()
    line_wrapping_file(file1)
    line_wrapping_file(file2)
    file1_content = ''
    file2_content = ''
    with open(file1, 'r') as f1:
        file1_content = f1.readlines()
    with open(file2, 'r') as f2:
        file2_content = f2.readlines()
    with open('out.html', 'w+') as fo:
        fo.write(hd.make_file(file1_content, file2_content, fromdesc=file1.split(os.sep)[-1],
                              todesc=file2.split(os.sep)[-1]))
    webbrowser.open_new_tab('out.html')


if __name__ == '__main__':
    file1 = os.path.abspath('.') + os.sep + "file1.txt"
    file2 = os.path.abspath('.') + os.sep + "file2.txt"
    file_compare(file1, file2)
