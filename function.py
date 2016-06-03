#!/usr/bin/python
# coding=utf-8
def fun():
    sth = raw_input("Please input something:")
    try:
        if type(int(sth)) == type(1):
            print "%s in a number" %sth
    except:
        print "%s is not number" %sth

#只有try执行异常的会后except才会执行

fun()