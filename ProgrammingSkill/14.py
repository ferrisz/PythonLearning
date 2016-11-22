#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/22

# 简单的wc命令

import sys

data = sys.stdin.read()

chars = len(data)
words = len(data.split())
lines = data.count('\n')

print lines, words, chars
print '%(lines)s %(words)s %(chars)s' %locals()
print '%(lines)s %(words)s %(chars)s' % {'lines':lines,'words':words,'chars':chars}

# locals()返回一个字典对象，代表当前对象的情况