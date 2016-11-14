#!/usr/bin/python
# coding=utf-8

import sys


# print sys.argv 打印文件名 以及 文件名后边的参数 以列表输出
def isNum(s):
    for i in s:
        if i in '0123456789':
            pass
        else:
            print "%s is not a num" % s
            sys.exit()
    else:
        # for循环正常退出执行else
        print "%s is a num" % s


isNum(sys.argv[1])
