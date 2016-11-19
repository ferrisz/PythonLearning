#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/16

# 打印目录下所有的文件

import os
import sys

# os模块下的方法
# os.listdir(path) 列出目录下所有的文件，以列表的形式呈现目录和文件都会有
# os.path.isdir() 判断后边后边的参数是不是一个目录 True False
# os.path.isfile() 判断后边后边的参数是不是一个文件 True False
# os.path.join('/etc/', 'passwd', 'abc') 将参数连接威路径连接起来 返回/etc/passwd/abc


# 使用递归实现

def print_files(path):
    lsdir = os.listdir(path)
    dirs = [i for i in lsdir if os.path.isdir(os.path.join(path, i))]
    files = [i for i in lsdir if os.path.isfile(os.path.join(path, i))]
    if files:
        for f in files:
            print os.path.join(path, f)
    if dirs:
        for d in dirs:
            print_files(os.path.join(path, d))

if __name__ == '__main__':
    print_files(sys.argv[1])
