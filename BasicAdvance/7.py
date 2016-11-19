#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/15


def factorial(n):
    sum = 1
    for i in range(1, n+1):
        sum *= i
    return sum


print factorial(5)

# 递归方式实现
# 递归的注意事项
#   必须有最后的默认结果 if n == 0
#   递归参数必须向默认结果收敛的： factorial(n-1)
def factorial1(n):
    if n == 0:
        return 1
    else:
        return n * factorial1(n-1)

print factorial1(5)
