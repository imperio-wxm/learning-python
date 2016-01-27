#!/usr/bin/env python
# -*- UTF-8 -*-
__author__ = 'wxmimperio'

print "hello"
print 'hello'
print "'hello'"
print '"hello"'

print "let\'s go"
print "100\\2=50"
print '\"hello\"'
print "this \nis"

str1 = "100+"
str2 = "5=105"
print str1 + str2

print """1
2
3"""
print '''a
b
c'''

print r"let\'s go"

str3 = u'hello world'
print str3
print isinstance(str3, unicode)

format_str = "My %s is %s"
values = ('name', 'wxmimperio')
print format_str % values

from math import pi

print "%d" % 10
print "%f" % 12.5
print "%s" % 'abc'
print "%10f" % pi
print "%10.2f" % pi
print "%.2f" % pi
print "%010.2f" % pi
print "%-10.2f" % pi
print "% d,% d" % (10, -20)
print "%+d,%+d" % (5, -30)

str4 = "My name is wxmimperio"
print str4.find("name")
print str4.find("we")

print str4.find('is', 0, 10)

list1 = ['1', '2', '3', '4', '5', '6']
print '+'.join(list1)
dict1 = {'a', 'b', 'c'}
print '&'.join(dict1)

str5 = "ABCD EFG"
print str5.lower()
print str5.lower().upper()
print str5.title()

print str5.replace('A', '12345')

str6 = "a+b+-c+d+e-f+g"
print str6.split("+")

str7 = "    1 2 3 4 5    "
print str7.strip()

from string import maketrans

table = maketrans('abc', '123')
str8 = 'abc'
print str8.translate(table)
