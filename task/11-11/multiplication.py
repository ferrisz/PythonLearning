#!/usr/local/python
# coding=utf-8
# Created by Ferris on 2016/11/12

for i in xrange(1, 10):
    for j in xrange(1, i+1):
        print '%sx%s=%s' % (j,i,j*i),
    print

