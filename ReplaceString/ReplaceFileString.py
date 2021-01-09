# _*_ coding: utf-8 _*_
__author__ = 'rentingsong'
__date__ = '2021/1/7 21:55'
from flask import render_template
from flask import request
from flask import send_from_directory
from werkzeug.utils import secure_filename
import os
from ReplaceString import replace_string_blue


def replace_file_string(file, old_string, new_string):
    with open(file, 'r+', encoding='UTF-8') as f:
        lines = f.readlines()
    with open(file, 'r+', encoding='UTF-8') as f:
        for line in lines:
            if old_string in line:
                f.write(line.replace(old_string, new_string))
            else:
                f.write(line)


@replace_string_blue.route('/replace_string_index')
def replace_string_index():
    return render_template('replace_string/replace_string.html')


@replace_string_blue.route('/replace_string', methods=['GET', 'POST'])
def replace_string():
    if request.method == "POST":
        file1 = request.files['file1']
        origin_string = request.form['origin_text']
        goal_string = request.form['goal_text']
        print(file1, origin_string, goal_string)
        base_path = os.path.dirname(__file__).rsplit(os.sep, 1)[0]
        upload_path = os.path.join(base_path, 'static' + os.sep + 'uploads' + os.sep + 'replace_string',
                                   secure_filename(file1.filename))
        file1.save(upload_path)
        replace_file_string(upload_path, origin_string, goal_string)
        return render_template('replace_string/replace_string_success.html', filename=file1.filename)


@replace_string_blue.route('/download_replace_file/<filename>')
def download_replace_file(filename):
    base_path = os.path.dirname(__file__).rsplit(os.sep, 1)[0]
    dirpath = os.path.join(base_path, 'static' + os.sep + 'uploads' + os.sep + 'replace_string')
    # as_attachment=True下载文件，不加的话会在浏览器打开文件而不会下载
    return send_from_directory(dirpath, filename, as_attachment=True)
    # return send_from_directory(dirpath, filename)


if __name__ == "__main__":
    pass


