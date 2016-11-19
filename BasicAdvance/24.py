#!/usr/local/python
# coding=utf-8
# Created by Ferris on 2016/11/19

# 内建函数5

# 序列处理函数

# len() 取序列的长度
# max() 取序列的最大值
# min() 取序列的最小值

# filter(function or None, sequence) 返回 list tuple string
filter(None, 'abc')
filter(None, range(10))
def f(x):
    if x % 2 == 0:
        return True

filter(f, range(10))

# zip(seq1[, seq2 [...]]) 返回一个大的序列 把几个列表拉在一个每个元素变成了一个元组
#   列表长度不一样 取最小的

l1 = [1,2,3]
l2 = ['a', 'b', 'c']
zip(l1,l2)
dict(zip(l1,l2))

# map(function,seq1[, seq2 [...]) 返回是个list  function 可以是None  多个系列长度不一函数为None时用None填充

def f1(x):
    return x ** 2
map(f1,l1)

l3 = [4,5,6]
def f2(x, y):
    return x * y

map(f2, l1, l2)

# reduce(function, seq)  将seq里边中的元素循环执行前边的函数


# 函数都可以使用匿名函数

# 列表表达式
# [i*2 for i in range(10)]
# [i*2+10 for i in range(10) if i % 3 == 0]
