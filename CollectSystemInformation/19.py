#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/29

# subprocess 模块使用
# import subprocess
#
# subprocess.Popen(['mkdir', 'aaa'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

from subprocess import PIPE,Popen

p = Popen(['./test.sh'])
p.wait()
print "main process"
# 主进程的执行不等待副进程执行完  如果想则执行.wait 方法

# p.kill() 结束进程
# p.terminate() 结束进程
# p.returncode 进程返回值
# p.communicate() 可以给子进程传参数 传超时时间

# PIPE管道
p1 = Popen(['ls'], stdout=PIPE)
p2 = Popen(['grep', 'py'], stdin=p1.stdout, stdout=PIPE)
result = p2.stdout
for i in result: print i,

# p.communicate() 相当于 p.stdin.write() p.stdin.close(), p.stdout.read() 这三个方法