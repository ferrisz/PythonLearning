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

# for 字典
dic = {'a':1,'b':1}
# #定义字典为{'a':100,'b':100,'c':100,'d':100,'e':100}
dic1 = dic.fromkeys('abcde',100)

for k in dic:
    print k

for k in dic1:
    print k
# #取到字典里的值
for k in dic1:
    print k, dic1[k]

for k in dic1:
    print "%s --> %s" % (k, dic1[k]),
# ##占一行加,

for i in dic1.items():
    print i

for k, v in dic1.items():
    print k, v

# #iteritems()用法和items一样只不过发挥的是对象不是元组

for k, v in dic1.iteritems():
    print k, v