#!/usr/local/python
# coding=utf-8
# Created by Ferris on 2016/11/11

macaddr = 'e4:ce:8f:0b:00:0a'
prefix_mac = macaddr[:-3]
last_two = macaddr[-2:]
plus_one = int(last_two,16) + 1
if plus_one in range(10):
    new_last_two = hex(plus_one)[2:]
    new_last_two = '0' + new_last_two
else:
    new_last_two = hex(plus_one)[2:]
    if len(new_last_two) == 1:
        new_last_two = '0' + new_last_two
new_mac = prefix_mac + ':' + new_last_two
print new_mac.upper()
