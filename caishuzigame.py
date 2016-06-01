#!/usr/bin/python
# coding=utf-8
#猜数字游戏

import random
countplayer = 0
countsys = 0

for i in xrange(12):
    x = int(raw_input("Please input a number from 1 to 20:"))
    num = random.randint(1,20)
    if x == num:
        print '猜对了'
        countplayer = countplayer + 1
    elif x > num:
        print '猜大了'
        countsys = countsys + 1
    elif x < num:
        print '猜小了'
        countsys = countsys +1
    if countplayer == 6:
        print 'Player win!'
        break
    if countsys == 6:
        print 'System win!'
        break