#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/12/10


import socket                                           # Socket模块
import datetime

HOST = '0.0.0.0'
PORT = 3434

# AF_INET说明使用IPv4地址，SOCK_STREAM指明TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))                                    # 绑定IP与端口
s.listen(1)                                             # 监听

while True:
    conn, addr = s.accept()                             # 接收TCP连接，并返回新的Socket对象
    print 'Client %s connected!' % str(addr)            # 输出客户端的IP地址
    dt = datetime.datetime.now()
    message = 'Current time is ' + str(dt)
    conn.send(message)                                  # 向客户端发送当前时间
    print 'Send: ', message
    conn.close()                                        # 关闭连接