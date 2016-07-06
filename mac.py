#!/usr/bin/env python
# coding=utf-8

macaddr = 'e4:ce:8f:0b:00:9a'
prefix_mac = macaddr[:-3]
last_two = macaddr[-2:]
plus_one = int(last_two,16) + 1
new_last_two = hex(plus_one)[2:]
new_mac = prefix_mac + ':' + new_last_two
print new_mac.upper()
