#!/usr/local/python
# coding=utf-8

score = int(raw_input("Please a num: "))
if score >= 90:
    print 'A'
    print 'Very good'
elif score >= 80:
    print 'B'
    print 'good'
elif score >= 70:
    print 'C'
    print 'pass'
else:
    print 'D'