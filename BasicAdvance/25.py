#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/19

# python模块的使用（一）

# 模块时python组织代码的基本方式
# 一个python脚本可以单独运行，也可以导入到另一个脚本中运行，当脚本导入运行时我们称其为模块
# 所有的py文件都可以座位一个模块导入

# 模块名与脚本的文件名相同
# 例如我们边写了一个名为hello.py的脚本，则可以在另一个脚本中用import hello 语句来导入他

# 包
# python的模块可以按目录组织为包
# 创建一个包的步骤：
#   创建一个名字为包的目录
#   在该目录下创建一个__init__.py文件
#   根据需要，在该目录下存放脚本文件或已经编译的扩展子包
#   import pack.m1, pack.m2, pack.m3

def wordCount(s):
    chars = len(s)
    words = len(s.split())
    # lines = len(s.split('\n')) 会多数一个
    lines = s.count('\n')
    print lines, words, chars

s = open('/etc/passwd').read()
wordCount(s)

# 如果脚本当作模块导入的话 模块不能以数字命名