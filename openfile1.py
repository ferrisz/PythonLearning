#!/usr/bin/python
# coding=utf-8

fd = open('/tmp/tmp.txt')
for line in fd.readlines():
    print line,