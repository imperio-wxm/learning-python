#!/usr/bin/env python
# -*- UTF-8 -*-
__author__ = 'wxmimperio'

try:
    x = input("Enter the first number: ")
    y = input("Enter the second number: ")
    print x / y
except ZeroDivisionError, e:
    print "ZeroDivisionError " + e.message
except NameError, e:
    print "Name Error " + e.message
else:
    print "No Error"
finally:
    print "Finish"

try:
    x = input("Enter the first number: ")
    y = input("Enter the second number: ")
    print x / y
except ZeroDivisionError as msg:
    print "ZeroDivisionError " + msg.message

try:
    x = input("Enter the first number: ")
    y = input("Enter the second number: ")
    print x / y
except:
    print "All Except"

try:
    x = input("Enter the first number: ")
    y = input("Enter the second number: ")
    print x / y
except (ZeroDivisionError, NameError) as msg:
    print msg.message

raise IOError("This is a IOError")


class MyException(Exception):
    def __init__(self, message):
        self.message = message


try:
    raise MyException("This is my exception class")
except MyException, e:
    print e.message

with open("test.txt") as message:
    for msg in message:
        print msg
