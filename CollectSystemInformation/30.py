#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/12/4

import re

# re.findall()方法：找到re匹配的所有字符串，并把它作为一个列表返回
# re.match()方法返回一个对象，只匹配开始的位置
# re.search()方法：扫描字符串，找个这个re匹配的位置
# re.match()与re.search()的区别：re.match只匹配字符串的开始如果字符串的开始不符合正则表达式则匹配失败，函数返回None；
#               而re.search匹配整个字符串，直找到一个匹配，如果成功的话，返回MatchObject实例
# re.sub()方法：替换