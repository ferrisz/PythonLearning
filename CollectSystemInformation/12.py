#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/27

# os.walk模块使用
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
a = os.wait(sys.argv[1])
for p, d, f in a:
    for i in f:
        fn = os.path.join(p, i)
        md5 = md5sum(fn)
        s += md5 + '  ' + fn + '\n'
        print s,
