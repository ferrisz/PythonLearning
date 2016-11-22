#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/22

# import OptionParser
# -c/--chars: 命令行选项
# dest:为选项定义变量名，值characters就是‘-c’选项的名字
# default=False:characters的值False，意思是默认情况下的命令不带-c选项
# help：选项的解释说明部分

# wc 命令中使用函数

from optparse import OptionParser

import sys,os

parser = OptionParser("Usage:%prog [file1] [file2]...")

parser.add_option('-c', '--char',
                  dest='chars',
                  action='store_true',
                  default=False,
                  help='only count chars')

parser.add_option('-w', '--word',
                  dest='words',
                  action='store_true',
                  default=False,
                  help='only count words')

parser.add_option('-l', '--line',
                  dest='lines',
                  action='store_true',
                  default=False,
                  help='only count lines')

options, agrs = parser.parse_args()

if not (options.lines or options.words or options.chars):
    options.lines, options.words, options.chars = True, True, True

if agrs:
    fn = args[0]
    with open(fn) as fd:
        data = fd.read()

else:
    data = sys.stdin.read()
    fn = ''

chars = len(data)
words = len(data.split())
lines = data.count('\n')

if options.lines:
    print lines,

if options.words:
    print words,

if options.chars:
    print chars,
print fn
