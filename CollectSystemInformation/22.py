#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/12/1

from subprocess import PIPE, Popen

p = Popen(['dmidecode'], stdout=PIPE)
data = p.stdout
lines = []
dmi = {}
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

dmi_dic = dict([i.strip().split(':') for i in lines])
for k, v in dmi_dic.items():
    dmi[k] = v.strip()
dmi['Manufacturer'] = dmi_dic['Manufacturer'].strip()
dmi['Product'] = dmi_dic['Product Name'].strip()
dmi['Serial'] = dmi_dic['Serial Number'].strip()
print dmi