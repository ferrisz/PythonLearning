#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/27

# hashlib模块使用

# import hashlib
#
# md5 = hashlib.md5()
#
# md5.update('a')
#
# md5.hexdigest()

import hashlib
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

if __name__ == '__main__':
    try:
        print md5sum(sys.argv[1])
    except IndexError:
        print "%s follow a argument" % __file__


