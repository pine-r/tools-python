# _*_ coding: utf-8 _*_
__author__ = 'rentingsong'
__date__ = '2021/1/9 11:53'
from FishMom import fish_mom_blue
from flask import render_template


@fish_mom_blue.route('/fish_index')
def fish_index():
    return render_template('fish_mom/fish_mom.html')


if __name__ == '__main__':
    pass