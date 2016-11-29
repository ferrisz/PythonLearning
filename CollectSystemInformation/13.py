#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/28

# 生成器yield

# def f(n):
#     for i in range(n):
#         yield i

# 生成器是一个可迭代的对象，可以对可迭代对象进行遍历，比如字符串列表灯都是课迭代的对象
# 当调用这个函数的时候，函数内部的代码并不立即执行，这个函数只是返回一个生成器对象
# 当使用for进行迭代的时候，函数内的代码才会被执行

# return宇yield的区别
# return的时候这个函数的局部变量就都销毁了
# 所有return是得到所有结果后的返回
# yield是产生了一个可以恢复的函数（生成器），恢复了局部变量
# 生成器只有在调用.next()时才运行函数生成一个结果

import hashlib
import os
import sys

def md5sum(f):
    m = hashlib.md5()
    with open(f) as fd:
        while True:
           data = fd.read(4096)
           if data:
               m.update(data)
           else:
               break
    return m.hexdigest()

s = ''
a = os.walk(sys.argv[1])
for p, d, f in a:
    for i in f:
        fn = os.path.join(p, i)
        md5 = md5sum(fn)
        s += md5 + '  ' + fn + '\n'
        print s,

