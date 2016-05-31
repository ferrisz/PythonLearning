#!/usr/bin/python
# coding=utf-8

a = 'ABC'
for i in a:
    print i,
# print 后加, 抑制换行符输出

print ""
# range(0,10,1) 开头 结尾 步长 开头和步长可以不写

for i in range(10):
    print i,

print [i for i in range(1,11)]
print [i*2 for i in range(1,11)]
print [i for i in range(1,11) if i%2 == 0]
print [i**2 for i in range(1,11)]
# **表示乘方

# xrange 返回是对象 不是列表 执行完之后不会占用内存
a = xrange(10)
for i in a:
    print i