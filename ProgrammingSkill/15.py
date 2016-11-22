#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/22

# 简单的wc命令实现(二)
import os
import sys
try:
    fd = open(sys.argv[1])
except IndexError:
    print 'please follow a argument at %s' % __file__
    sys.exit()

if not os.path.exists(fd):
    print '%s is not exists' % fd
    sys.exit()

data = fd.read()
chars = len(data)
words = len(data.split())
lines = data.count('\n')

print '%(chars)s %(words)s %(lines)s' % locals()
