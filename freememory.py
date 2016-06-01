#!/usr/bin/python
# coding=utf-8
# 统计系统剩余内存

with open('/proc/meminfo') as fd:
    for line in fd:
        # 字符串.startswith 以什么开头  返回布尔值
        if line.startswith('MemTotal'):
            # 字符串.split 以什么字符分割
            total = line.split( )[1]
            continue
        if line.startswith('MemFree'):
            free = line.split( )[1]
            break
print "%.2f" % (int(free)/1024.0) + 'M'
print "%.2f" % (int(free)/int(total))*100 + '%'
