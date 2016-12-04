#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/12/4

# 正则表达式
# \d 匹配任何十进制数，相当于[0-9]
# \D 匹配任何非数字字符，相当于[^0-9]
# \s 匹配任何空白字符，相当于[\t\n\r\f\v]
# \S 匹配任何非空白字符，相当于[^\t\n\r\f\v]
# \w 匹配任何字母数字字符，相当于[a-zA-Z0-9]
# \W 匹配任何非字母数字字符，相当于[^a-zA-Z0-9]

import re

re.findall(r'^ab+', 'fsdfsd')
