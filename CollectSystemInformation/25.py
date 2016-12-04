#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/12/4

# 收集IP信息

from subprocess import Popen, PIPE

def getIP():
    p = Popen(['ifconfig'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()
    data = [i for i in stdout.split('\n') if i]
    return data

def genIP(data):
    new_line = ''
    lines = []
    for line in data:
        if line[0].strip():
            lines.append(new_line)
            new_line = line + '\n'
        else:
            new_line += line + '\n'
    lines.append(new_line)
    return [i for i in lines if i and not i.startswith('lo')]

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
    data = getIP()
    data_list = genIP(data)
    print parseIfconfig(data_list)