#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/20

# 类的继承（一）
# 继承是面向对象的重要特征之一
# 继承关系：继承是相对两个类而言的父子关系，子类继承了父类的所有公有属性和方法
# 继承实现了代码的重复使用

# 使用继承
# 继承可以重用已经存在的数据和行为，减少代码的重复编写。Python在类名后使用一对括号来表示继承关系，括号中的类即为父类
# class Myclass(ParentClass):
#     如果父类定义了__init__方法，子类必须显式调用父类的__init__方法(当构造函数有参数时)：
#     ParentClass.__init__(self,[args...])
#     如果子类需要扩展父类的行为，可以添加__init__方法的参数

# 父类和子类有同样的方法先调用子类的方法

# super函数



class A(object):
    def __init__(self):
        print 'enter A'
        print 'leave A'

class B(A):
    def __init__(self):
        print 'enter B'
        super(B,self).__init__()
        print 'leave B'

b = B()



class People(object):
    color = 'yellow'
    __age = 30

    def __init__(self，c):
        self.dwell = 'Earth'

    def think(self):
        self.color = "black"
        print "I am a %s" % self.color
        print "I am a thinker"
        print self.__age

class Chinese(People):
    def __init__(self):
        People.__init__(self,'red')
    def think(self):
        self.color = "black"


cn = Chinese()
print cn.color
print cn.dwell