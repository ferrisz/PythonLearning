#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/12/6

# 访问数据库
# 如何访问数据库,交互式方法
# python manage.py shell
# from blog.models import Host //导入表
# 显示数据
# node = Host.objects.all()
# node,values()
# 增加数据：
# n1 = Host(hostname='node1',ipaddr='1.1.1.1')
# 或者：
# n1 = Host()
# n1.hostname = 'node1'
# n1.ipaddr = '1.1.1.1'
# n1.save()

# 通过视图文件views.py来访问数据库
# 1、在urls.py文件里定义urls访问路径
# 2、在views。py里定义访问方法
# from blog.models import Host
# def index(req):
#     n1 = Host(hostname = 'node2', ipaddr = '2.2.2.2')
#     n1.save()
#     return HttpResponse('OK')