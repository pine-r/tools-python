# _*_ coding: utf-8 _*_
__author__ = 'rentingsong'
__date__ = '2021/1/7 21:55'
from flask import render_template
from flask import request
from ReplaceString import replace_string_blue


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
        return render_template('replace_string/replace_string_success.html')


if __name__ == "__main__":
    pass

