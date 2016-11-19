#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/9

string = []

while 1 :
    string_temp = raw_input('请输入字符串, 如想结束输入请单独输入" . ":')
    if string_temp == '.':
        break
    string.append(string_temp)

print ' '.join(string) + '.'
