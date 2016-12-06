#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/12/6

# API-json格式

{groupname:"web", members: []}

[
    {
        groupname:'web',
        members:[
            {
               hostname:'agent01',
                ip:'192.168.1.1'
            }，
        ]
    },
]

# 命令行访问数据库
# python manage.py shell
from hostinfo.models import *
hg = HostGroup.objects.all()
hg.groupname
hg.members.all()
h = hg.members.all()[0]
ip = h.ip
host = Host.object.get(hostname='agent03')
host.ip = '192.1681.113' //修改记录
host.save()