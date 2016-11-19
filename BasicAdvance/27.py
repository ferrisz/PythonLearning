#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/19

# 面向对象介绍
# 类定义
# 类把需要的变量和函数组合成一起，这种包含成为封装
# class A(object):
# 类的结构：
# class 类名:
#     成员变量-属性
#     成员函数-方法

class Myclass(object):
    def fun(self):
        print 'I am function'

# 类的方法中至少有一个参数self