#!/usr/bin/python
# coding=utf-8

info = {}
name = raw_input("Please input name:")
age = raw_input("Please input age:")
gender = raw_input("Please input (M/F):")
info['name'] = name
info['age'] = age
info['gender'] = gender
for i in info.items():
    print i
for k, v in info.items():
    print k + ':' + v //用加号连接字符串
    print "%s: %s" % (k,v) //格式化输出
print "main end"
