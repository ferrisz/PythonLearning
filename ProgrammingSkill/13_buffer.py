#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/22

import sys

import time

for i in range(10):
    sys.stdout.write("str:%d\n" % i)
    sys.stdout.flush()
    time.sleep(1)

# python 13_buffer.py | cat -
# python -u 13_buffer.py | cat -
# cat sss.rpm |ssh 192.168.1.10 "cat - >/tmp/sss.rpm" 传输文件用输出流拷贝