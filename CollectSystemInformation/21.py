#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/30
import os
from subprocess import Popen, PIPE

def getPid():
    p = Popen(['pidof', 'httpd'], stdout=PIPE, stderr=PIPE)
    pids = p.stdout.read().split()
    return pids

def parsePidFile(pids):
    sum = 0
    for i in pids:
        fn = os.path.join('/proc', i, 'status')
        with open(fn) as fd:
            for line in fd:
                if line.startswith('VmRSS'):
                    http_mem = int(line.split()[1])
                    sum += http_mem
                    break
    return sum

def total_mem(f):
    with open(f) as fd:
        for line in fd:
            if line.startswith('MemTotal'):
                total_mem = int(line.split()[1])
                return total_mem

if __name__ == '__main__':
    pids = getPid()
    http_mem = parsePidFile(pids)
    total_mem = total_mem('/proc/meminfo')
    print 'Apache memory is: %s KB' % http_mem
    print 'Percent: %.2f%%' % (http_mem / float(total_mem) * 100)