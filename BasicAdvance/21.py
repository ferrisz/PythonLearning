#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/16

# 内建函数2

# callable() 返回一个对象是否是可被调用的对象（函数或者类） 返回一个布尔值

# type() 查看一个对象的类型
l = [1,2,3,]
if type(l) == type([]):
    print 'ok'

# isinstance() 返回一个对象是不是一个什么类型   第二个参数如果是一个类型的话就是判断是不是这个类型
#   如果第二个参数是一个元组，但是不是元组里类型的一种 返回值是布尔值
s = 'dadasdas'
isinstance(l, list)
isinstance(s, str)
isinstance(s,(int,str))
isinstance(s,(int, tuple))

class A(object):
    pass

a = A()
isinstance(a, A)
# 判断类用isinstance方便判断其他type方便

cap(1,2)
# cap(x,y)  x<y -1   x=y 0  x>y  1    可以比较字符串的大小 按照字符来比较

range(10)
xrange(10)
# range() 返回的是一个列表  真实的在内存里有了
#   xrange()返回的是一个可迭代的对象  遍历的时候他才有了一般不占用内存资源 所以效率高