#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/21

# 类的属性-总结
# 类属性,也是公有属性
# 类的私有属性
# 对象的公有属性
# 对象的私有属性
# 内置属性
# 函数的局部变量
# 全局变量

# 对象的属性只能通过对象访问不能通过类访问

var5 = '全局变量var5'
class MyClass(object):
    var1 = '类属性，累的公有属性 var1'
    __var2 = '类的私有属性 __var2'

    def func1(self):
        self.var3 = '对象的公有属性 var3'
        self.__var4 = '对象的私有属性 __var4'
        var5 = '函数的局部变量'

    def func2(self):
        print self.var1
        print self.__var2
        print self.var3
        print self.__var4

mc = MyClass()
print mc.var1
print mc._MyClass__var2
mc.func1()
print mc.var3
print MyClass.var1

mc.func2()
print mc.__dict__
# 类的内置属性