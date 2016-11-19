#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/16

# 内建函数1
import __builtin__

__builtin__.float()

# help(__builtin__.XXX)

# 返回一个数字的绝对值

def fun(x):
    if x < 0:
        return -x
    return x

# 等于abs()


# max() 参数时一个可迭代的对象
# min()

# len()取序列长度 列表 元组 字典 字符串
# divmod(x,y) x/y 返回一个元组两个值一个商一个余数
# pow(x,y[, z]) 两个参数的话就是 x^y  三个参数就是(x^y)%z
# round(number[, ndigits]) 四舍五入 后边可选参数是保留几位小数 默认为0  先变浮点侯保留

