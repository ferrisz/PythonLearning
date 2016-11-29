#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/29

# 自定义异常

class FuncError(Exception):
    def __str__(self):
        return 'I am a FuncError'

def fun():
    raise FuncError()

try:
    fun()
except FuncError, e:
    print e


# 异常在try块里抛
# finally:无论try块里边是否抛异常，永远执行的代码，通常用来执行关闭文件，断开服务器连接的功能
# try无异常才会执行else
# try:
# except:
# else:
# finally:

# glob模块
# glob：扩展shell通配符
# glob.glob('*')
import glob
glob.glob('/etc/*.conf')

# shlex模块 将命令拆分 可以配合subproess使用
import shlex
cmd = "mysql -u root -p123 -e'show processlist'"
shlex.split(cmd)