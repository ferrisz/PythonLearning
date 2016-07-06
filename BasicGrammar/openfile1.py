#!/usr/bin/python
# coding=utf-8

fd = open('/tmp/tmp.txt')
for line in fd.readlines():
    print line,

for line in fd:
    print line,

fd.close()


with open('/tmp/tmp.txt') as fd:
# fd = open('/tmp/tmp.txt')
    while True:
        line = fd.readline()
        if not line:
            break
        print line,
# fd.close()

