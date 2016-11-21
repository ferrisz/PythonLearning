#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/22

# Python 处理标准输出

# print 和 stdout的区别
# print 通常是调用一个stdout对象的write方法
# print 会先进行格式转换
# print 会在最后加上换行符



import sys

sys.stdout.write('this is a stdout\n')
sys.stderr.write('this is a stderr\n')


# python 13.py > /dev/null   标准输出定向到了null中  只输出了错误输出
# python 13.py 2> /dev/null   错误输出定向到了null中  只输出了标准输出
# python 13.py 2> /dev/null  >&2 输出都定向到了null中