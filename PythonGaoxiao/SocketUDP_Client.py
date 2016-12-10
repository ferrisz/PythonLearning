#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/12/10

import socket

HOST = '127.0.0.1'
PORT = 3434

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = 'Hello UDP!'
s.sendto(data, (HOST, PORT))
print 'Sent: %s to %s:%d' % (data, HOST, PORT)

s.close()