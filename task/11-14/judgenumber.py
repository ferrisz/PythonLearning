#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/14

def judgeNumber(s):
    for i in s:
        if i in '0123456789':
            pass
        else:
            return False
    else:
        return True
if __name__ == '__main__':
    string = raw_input('请输入一个字符串:')
    if judgeNumber(string):
        print '字符串是纯数字'
    else:
        print '字符串不是纯数字'
