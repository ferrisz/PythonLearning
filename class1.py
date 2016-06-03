#!/usr/bin/python
# coding=utf-8

class People(object):
    color = 'yellow'
    def think(self):
        self.color = 'black'
        print "I am a %s" % self.color
        print "i am thinker"
        # 类的方法中至少有一个参数self

ren = People()
print ren.color
ren.think()