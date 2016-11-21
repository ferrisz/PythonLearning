#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/21

# 文件处理的一些方法

# read() 一次都读完，参数可加 读几个字符
# readline() 是一行一行返回
# readlines() 是一个列表 每一行是个元素

import sys

def lineCount(fd):
    n = 0
    # for i in fd.readlines():
    for i in fd:
        n += 1
    return n

fd = sys.stdin
print lineCount(fd)

# f = open('/etc/hosts')
with open('/etc/hosts') as f:
    while True:
    data = f.readline()
    if not data:
        break
    print data,
# f.close()