#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/12/4

# 收集IP信息

from subprocess import Popen, PIPE

def getIfconfig():
    p = Popen(['ifconfig'], stdout=PIPE)
    data = p.stdout.read().split('\n\n')
    return [i for i in data if i and not i.startswith('lo')]

def parseIfconfig(data):
    dic = {}
    for line in data:
        line_list = line.split('\n')
        devname = line_list[0].split()[0]
        macaddr = line_list[0].split()[-1]
        ipaddr = line_list[1].split()[1].split(':')[1]
        dic[devname] = [ipaddr, macaddr]
    return dic

if __name__ == '__main__':
    data = getIfconfig()
    print parseIfconfig(data)