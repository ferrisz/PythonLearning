#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/12/6

# 序列化介绍及pickle模块


# 简单序列化
# 序列化
# 将对象的状态信息转换为可以存储或传输的形式的过程
# 内存里面有一个数据结构，你希望把它保存下来重用，或者发送给其他人
# 很多游戏允许你在退出的时候保存进度，然后你再次启动的时候回到上次退出的地方

# 常用的一些序列化
# pickle, cPickel
# JSON 跨语言
# shelve
# YAML

import pickle

d = {'a':1, 'b':2}

with open('/tmp/1.pickel','wb') as fd:
    # pickle.dump() 序列化到磁盘
    # pickle.dumps() 序列化到内存
    pickle.dump(d, fd)


with open('/tmp/1.pickel','r') as fd:
    a = pickle.load(fd)
    # pickle.load() 从硬盘反序列化
    # pickle.loads() 从内存反序列化

# 序列化到内存
a1 = pickle.dumps(a)
a2 = pickle.loads(a1)
