#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/12/6

# 数据传递post和get

# 定义api
1、urls.py定义访问路径
2、views.py定义访问方法
# def collect(request):
#     if request.POST: 或者 request.method == 'POST':
#         hostname = request.POST.get('hostname')
#         ipaddr = request.POST.get('ipaddr')
#         host = Host()
#         host.hostname = hostname
#         host.ipaddr = ipaddr
#         host.save('OK')
#     else:
#         return HttpResponse('not data')

# HttpRequest
# request.POST.get('hostname')
# 或
# request.POST['hostname']

# request.GET.get('hostname')
# 或
# request.GET['hostname']

# 传输数据
# POST方法
# curl -d hostname='node5' -d ip='192.168.1.5' http://127.0.0.1:8000/db/

# GET方法
# http://127.0.0.1:8000/db/?hostname=n3&ip=1.1.1.3