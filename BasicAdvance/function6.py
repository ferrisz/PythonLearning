#!/usr/local/python
# coding=utf-8
# Created by Ferris on 2016/11/14

# 多类型传值
# 冗余参数

def fun(x, y):
    print x + y

t = (1, 2)

fun(*t)
# 多类型传值传一个元组进入函数需要在元组前加*

def fun1(x, y, z):
    print x + y + z

t1 = (2, 3, 4)
fun1(*t1)
fun1(*(1, 2, 3))
fun1(1,*t)

# *t只能放在命名参数后边不能放在命名参数前边

dic = {'x':1, 'y':3, 'z':5}
# dic = {x:1, y:3, z:5} 这样是错误的 这样x y z是变量
fun1(**dic)

# 冗余参数
def fun3(x, *args, **kwargs):
    print x + y
    print args
    print kwargs

fun3(1,2,'a',[1,2,],*t,z=2,**{'f':11})
# 1 存入x 2,'a',[1,2,],元组t存入元组args  z=2,字典{'f':11}存入字典kwargs