#!/usr/bin/python
# coding=utf-8

# python文件访问
# open(name[,mode[,buffering]]) 返回时一个文件对象

# r 以读的方式打开 必须是已存在的文件
# w 写 没有的话会创建 有的话会覆盖
# a 追加 不存在也会创建
# r+ 读写
# w+ 读写 与w一样
# a+ 读写 与a一样
# rb 二进制读
# wb 二进制写
# ab 二进制追加
# rb+ 二进制读写
# wb+ 二进制读写
# ab+ 二进制读写
# 通常用二进制模式打开

fd = open('/tmp/tmp.txt','ab')

# write 只接受字符串
fd.write('adsad')

# read 默认从第一个字符读到最后一个字符 后边的参数表示读几个字符 返回的是一个字符串
fd.read()

# readline 读一行 返回的是一个字符串
fd.readline()

# readlines 读多行 有多少行读多少行 返回的是一个list 每一行后边有个换行符

fd.close()