#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/12/6


# 序列化对象供其他语言读写
# JavaScript Object Notation
# Json是被设计为跨语言使用的
# Json是文本格式
# Json必须使用unicode编码，默认utf-8方式存储

import json

d = {'a':1, 'b':2}
d['c'] = ('c1', 'c2')
d['d'] = True
d['e'] = None

with open('/tmp/d.json','w') as fd:
    json.dump(d, fd)

    with open('/tmp/d.json', 'r') as fd:
        d1 = json.load(fd)