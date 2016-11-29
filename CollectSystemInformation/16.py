#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/29
import os
# python 调用外部命令
# 打开外部程序

# os.system 输出到终端上，捕获不到
# os.popen 只能捕获到标准输出，捕捉不到标准错误输出 方法 read() readinto() readline() readlines()
# os.popen2 返回两个对象，一个是标准输入，一个标准输出
# os.popen3 返回三个对象，标准输入，标准输出，标准错误输出
# os.popen4 返回两个对象，pipe_in 和 pipe_out_err
# 以上都不建议使用

import subprocess

# subprocess.call() 与 os.system() 用法类似
# 如果命令式带参数的需要
# subprocess.call(['ls -l'], shell=True)
# subprocess.call(['ls', '-l'])这两种写法
# subprocess.check_call() 与call用法基本一直 如果返回码不为0 将抛出异常
