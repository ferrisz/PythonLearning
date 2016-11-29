#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/29

# 判断一个字符串是数字
import string
import sys, os


def isNum(s):
    for i in s:
        # if i in '0123456789':
        if i in string.digits:
            continue
        else:
            return False
    return True


# 可以用字符串的方法isdigit()判断字符串是不是纯数字

for pid in os.listdir('/proc'):
    if isNum(pid):
        print pid

