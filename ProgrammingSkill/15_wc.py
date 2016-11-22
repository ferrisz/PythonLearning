#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/22
import os
import sys

if len(sys.argv) == 1:
    data = sys.stdin.read()
else:
    try:
        fn = sys.argv[1]
    except IndexError:
        print 'please follow a argument at %s' % __file__
        sys.exit()

    if not os.path.exists(fn):
        print '%s is not exists' % f1
        sys.exit()
    fd = open(sys.argv[1])
    data = fd.read()
    fd.close()


chars = len(data)
words = len(data.split())
lines = data.count('\n')

# print lines, words, chars
# print '%(lines)s %(words)s %(chars)s' %locals()
print '%(lines)s %(words)s %(chars)s' % {'lines':lines,'words':words,'chars':chars}
