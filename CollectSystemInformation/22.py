#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/12/1

from subprocess import PIPE, Popen

p = Popen(['dmidecode'], stdout=PIPE)
data = p.stdout
lines = []
a = True
while a:
    line = data.readline()
    if line.startswith('System Information'):
        while True:
            line=data.readline()
            if line == '\n':
                a = False
                break
            else:
                lines.append(line)

print s\
    # mark