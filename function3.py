#!/usr/bin/python
# coding=utf-8
# 打印proc模块下所有的pid


import sys
import os

def isNum(s):
    for i in s:
        if i in '0123456789':
            pass
        else:
            # print "%s is not a num" %s
            break
    else:
        print s

for i in os.listdir('/proc'):
    isNum(i)

# 默认参数

def fun(x, y = 100):
    print x + y

fun(2,5)
fun(2)
fun(x=20,y=30)
fun(x=20)
fun(x=20,)

def fun1(x=2,y=3):
    print x + y

fun1()
fun1(4,7)
fun1(4)

# 默认参数只能是从右到左 写到后边
def fun2(x,y=3):
    print x + y

def fun1(a,x=2,y=3):
    print a + x + y