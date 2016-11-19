#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/20

# python 内部类
# 所谓内部类,就是在类的内部定义的额勒,主要目的事更好的抽象现实世界
# 例子:
#       汽车是个类,汽车的底盘,轮胎也可以抽象为类,将其定义到汽车的类中,
#       则形成内部类,更好的描述汽车类,因为底盘、轮胎是汽车的一部分

# 内部类的实例化方法
# 方法1：直接使用外部类调用内部类
#       object_name = outclass_name.inclass_name()
# 方法2：先对外部类进行实例化，然后再实例化内部类
# out_name = outclass_name()
# in_name = out_name.inclass_name()
# in_name.method()

# 魔术方法
# __str__(self)
# 构造函数与析构函数
#  构造函数：用于初始化类的内部状态，python提供的构造函数是__init__()
#           __init__()方法是可选的，如果不提供，python会给出一个默认的__init__的方法
#  析构函数：用于释放对象占用的资源，python提供的析构函数是__del__()
#           __del__()也是可选的，如果不提供，则python会在后台提供默认析构函数

# 垃圾回收机制
# python采用垃圾回收机制来清理不在使用的对象；python提供gc模块释放不在使用的对象
# python采用”引用计数“的算法方式来处理回收，即：当某个对象在其作用域内不在被其他对象引用的时候，python就自动清除对象
# gc模块的collect()可以一次性收集所有待处理的对象（gc.collect）

import gc

class People(object):
    color = 'yellow'
    __age = 30

    class Chinese(object):
        print "I am Chinese"

    def __str__(self):
        return 'This is People class'

    def think(self):
        self.color = "black"
        print "I am a %s" % self.color
        print "I am a thinker"
        print self.__age

    def __talk(self):
        print "I am talking to Tom"

    def test(self):
        self.think()
        self.__talk()

    def test1(self):
        print self.color


    cm = classmethod(test1)

    def test2():
        print "this is func"
        print People.color

    sm = staticmethod(test2)

    @staticmethod
    def test3():
        print "this is func"

    @classmethod
    def test4(self):
        print self.color

print gc.collect()