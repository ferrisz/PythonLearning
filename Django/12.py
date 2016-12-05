#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/12/5

# 添加一个应用
# python manage.py startapp blog
# 或者
# django-admin.py startapp blog

# 1、添加应用：setting.py
# INSTALLED_APPS={
#     'blog',
# }
# 2、修改url配置文件urls.py：用户请求的url转给谁去如理
# url(r'^blog/index/$','blog.views.index'),
# 3、修改应用的视图文件：让views.py文件的index方法来处理此请求：
# from django.http import HttpResponse
# def index(request):
#     return HttpResponse('<h1>hello django</h1>')

# 导入模板
# mkdir blog/templates
# 修改视图文件views.py
# from django.template import loader, Context
# 1、创建模板对象，把对性的模板文件导入
# t = loader.get_template('index')
# 2、生成Context对象
# c = Context({})
# 3、return HttpResponse(t.render(c))