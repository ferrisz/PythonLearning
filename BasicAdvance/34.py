#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/21

# 类的方法总结
# 公有方法
# 私有方法
# 类方法
# 静态方法
# 内置方法

class MyClass(object):
    name = 'Test'

    def func1(self):
        print self.name
        print '我是公有方法'

    def __func2(self):
        print self.name
        print '我是私有方法'

    @classmethod
    def classFun(self):
        print self.name
        print '我是类方法'

    @staticmethod
    def staticFun():
        print MyClass.name
        print '我是静态方法'

mc = MyClass()
