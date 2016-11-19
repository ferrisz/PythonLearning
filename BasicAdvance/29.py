#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/19

# 类的方法
# 方法的定义和函数一样,但是需要self作为第一个参数。
# 类方法为：
#   公有方法
#   私有方法
#   类方法
#   静态方法

# 公有方法:在类中和类外都能调用的方法
# 私有方法:不能被类的外部调用,在方法前面加上"__"双下划线就是私有方法。
# self参数
#   用于区分函数和类的方法（必须由一个self）self参数表示执行对象本身


# 类方法：被classmethod()函数处理过的函数，能被类所调用，也能被对象所调用（事继承的关系）
# 静态方法：相当于“全局函数”，可以被类直接调用，可以被所有实例话对象共享，
#           通过staticmethod()定义，静态方法没有“self”参数
#           速度比动态快，但是占用内存
# 装饰器：
#       @classmethod
#       @staticmethod

class People(object):
    color = 'yellow'
    __age = 30

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


jack = People()
jack.test()
People.cm()
