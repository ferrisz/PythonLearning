#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/29

# 按字典值排序
# 按照字典value排序，类似sort -k 命令
# import operator
# x = {1:2, 3:4, 4:3, 2:1, 0:0}
# sorted_x = sorted(x.iteritems(), key=operator.itemgetter(1))
# sorted_y = sorted(x.iteritems(),key=operator.itemgetter(1), reverse=True)

# 找出占用空间大的文件

import os
import operator

import sys


def gen_dic(topdir):
    dic = {}
    a = os.walk(topdir)
    for p, d, f in a:
        for i in f:
            fn = os.path.join(p, i)
            f_size = os.path.getsize(fn)
            dic[fn] = f_size
    return dic

if __name__ == '__main__':
    dic = gen_dic(sys.argv[1])
    sorted_dic = sorted(dic.iteritems(), key=operator.itemgetter, reverse=True)
    for k, v in sorted_dic[:10]:
        print k, '-->', v

