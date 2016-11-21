#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/22

import sys

fd = sys.stdin
data = fd.read()
filename = sys.argv[1]
def write(filename):
    with open(filename,'w') as f:
        sys.stdout = f
        for line in data:
            sys.stdout.write(line)

if __name__ == '__main__':
    write(filename)