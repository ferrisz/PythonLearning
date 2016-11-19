#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/13

with open('/proc/meminfo') as fd:
    for line in fd:
        if line.startswith('MemTotal'):
            total = line.split( )[1]
            continue
        if line.startswith('MemFree'):
            free = line.split( )[1]
            break
print "%.2f" % (int(free)/1024.0) + 'M'
print "%.2f" % (int(free)/int(total))*100 + '%'
