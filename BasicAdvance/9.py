#!/usr/local/python
# coding=utf-8
# Created by Ferris on 2016/11/16

# 匿名函数
# lambda函数是一种快速定义单行的最小函数，可以用在任何需要函数的地方

def fun(x, y):
    return x * y
fun(2, 3)

r = lambda x, y: x * y
r(2, 3)

# 匿名函数的优点：
# 1.使用python写一些脚本时，使用lambda可以省去定义函数的过程，让代码更加精简
# 2.对于一些抽象的，不会被别的地方再重复使用的函数，有时候函数起个名字也是个难题
#   使用lambda不再需要考虑命名的问题
# 3.使用lambda再某些时候让代码更容易理解

# lambda基础
# lambda语句中，冒号前时参数，可以有多个，逗号隔开，冒号右边时返回值
# lambda语句构建的其实是一个函数对象

# reduce(function,sequence) 一个函数一个序列 函数必须有两个参数
# 遍历序列执行函数
# reduce(lambda x, y: x+y,[1, 2, 3, 4, 5]) ((((1+2)+3)+4)+5)
print reduce(fun, range(1, 5))