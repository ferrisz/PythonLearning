#!/usr/bin/python

yn = raw_input("Please input [Yes/No]: ")

yn = yn.lower()

if yn == 'y' or yn == 'yes':
    print "programe is running..."
elif yn == 'n' or yn == 'no':
    print "programe is exit"
else:
    print "Please input [Yes/No]"