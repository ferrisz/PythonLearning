#!/usr/bin/python
# coding=utf-8

# for循环用在有次数的循环上
# while循环用在有条件的控制上

# 当循环正常结束时执行else

x = ''
while x != 'q':
    print 'hello'
    x = raw_input("Please input something,q for quit:")
    if not x:
        break
    if x == 'quit':
        continue
    print 'continue'
else:
    print 'world'
