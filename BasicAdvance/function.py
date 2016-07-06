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

def fun1(x,y):
    print x + y
fun1(2,3)

def Max(x, y):
    if x > y:
        print x
    else:
        print y

Max(5, 4)
