#!/usr/bin/python
# coding=utf-8

# for循环正常结束才会执行else
import time
import sys
for i in xrange(10):
    print i
    if i == 3:
        continue
# continue 退出当前层的循环 也就是说不显示3了
#    time.sleep(2)
    elif i == 5:
        time.sleep(2)
        break
    elif i == 6:
        pass
# pass表示什么都不做,一般用作占位符
    elif i == 7:
        sys.exit()
# sys.exit()退出整个程序
# elif效率更好一些
    print i
else:
    print 'main end'
