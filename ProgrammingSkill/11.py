#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/21


# Python 处理标准输入

# unix的重要哲学之一：管道
# 一个程序的输出作为另一个程序的输入
# cat /etc/hosts |wc -l

import sys
fd = sys.stdin
data = fd.read()
sys.stdout.write(data + '\n')
print data,