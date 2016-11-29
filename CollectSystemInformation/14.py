#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/29


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

def file_md5(topdir):
    a = os.walk(topdir)
    for p, d, f in a:
        for i in f:
            fn = os.path.join(p, i)
            md5 = md5sum(fn)
            yield '%s  %s' % (md5, fn)


if __name__ == '__main__':
    lines = ''
    try:
        topdir = sys.argv[1]
    except IndexError:
        print '%s follow a dir'
        sys.exit()
    gen = file_md5(topdir)
    for i in gen:
        lines += i + '\n'
    print lines
    print hashlib.md5(lines).hexdigest()


