#!/usr/local/python
# coding=utf-8
__author__ = 'Ferris'


# Function Define

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

# Input
try:
    num1 = float(input('Please input the first number:'))
    opinion = raw_input('Please input the opinion:(+ - * /)')
    num2 = float(input('Please input the second number:'))
except:
    print 'Number ERROR'
    exit(1)

# Calculate

if opinion == '+':
    ans = addition(num1, num2)
elif opinion == '-':
    ans = subtraction(num1, num2)
elif opinion == '*':
    ans = multiplication(num1, num2)
elif opinion == '/':
    ans = division(num1, num2)
elif opinion != '+' or opinion != '-' or opinion != '*' or opinion != '/':
    print 'Opinion ERROR'
    exit(1)

# Output
print  'Answer is '+ str(ans)

