#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/13

from subprocess import PIPE, Popen
import os

def getPid():
    p = Popen(['pidof', 'httpd'], stdout=PIPE, stderr=PIPE)
    pids = p.stdout.read().split()
    return pids

def parsePidFile(pids):
    sum = 0
    for i in pids:
        fn = os.path.join('/proc',i,'status')
        with open(fn) as fd:
            for line in fd:
                if line.startwith('VmRSS'):
                    mem = int(line.split()[1])
                    sum += mem
                    break
    return sum

def total_mem(fn):
    with open(fn) as fd:
        for line in fd:
            if line.startswith('MemTotal'):
                total_memory = int(line.split()[1])
                return total_memory


if __name__ == '__main__':
    pids = getPid()
    sum_mem = parsePidFile(pids)
    total_memory = total_mem('/proc/meminfo')
    print 'Httpd sum memory is %s KB' % sum_mem
    print 'Memory percent: %.2f%%' % ((sum_mem/float(total_memory))*100)