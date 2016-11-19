#!/usr/local/python
# coding=utf-8
# Created by Ferris on 2016/11/19

# 内建函数4
# 字符串处理函数

# str.capitalize() 返回一个字符串 他的首字母被大写

s = 'hello'

s.capitalize()

# str.replace(old, new[, count])
#   把字符串中的旧的字符串换成新的字符串 count是替换次数，默认都替换

# str.split([sep [,maxspilt]]) 默认以空格、tab、换行符切分， sep为切割符  ，maxspilt 最多切分几次
ip = '192.168.1.1'
ip.split('.')

# str.join(iterable) 参数是个可迭代的对象 返回的是个字符串 连接可迭代的对象 str是连接符

print ' '.join([str(i) for i in range(10)])

import string
string.capitalize('hello')
string.replace('hello','o','O',1)

