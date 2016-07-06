#!/usr/bin/python
# coding=utf-8


x = 'global var'
# 全局变量一般在上边定义
x = 100
def fun():
    global x
    x += 1
    # x = 100
    # 函数内部也能调用全局变量 能print 但不能进行实际操作 要进行实际操作  在函数中在进行 global x 进行定义
    global y
    y = 1
    # 在函数内部将变量申明为全局变量 在函数被调用后 变量也可以被使用
    print x
    print locals()
    # locals() 在函数内部用字典保存标量内用,统计函数内的变量,全局使用时保存脚本执行的时候保存哪些变量,统计程序内的变量w
# 局部变量只能在函数内部有效
fun()
print x