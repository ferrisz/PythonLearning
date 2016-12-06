#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/12/6

# 主机分组管理

# 创建HostGroup表 models.py
# class HostGroup(model.Model):
#     groupname = models.CharFiled(max_lenth=50)
#     members = models.ManyToManyField(Host)

# 注册数据库,admin.py
# from hostinfo.models import HostGroup
# class HostGroupAdmin(admin.ModelAdmin):
#     list_display = ['groupname']
#
# admin.site.register(HostGroup, HostGroupAdmin)