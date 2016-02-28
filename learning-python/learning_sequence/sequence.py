#!/usr/bin/env python
# -*- UTF-8 -*-
__author__ = 'wxmimperio'

test_list = [1, 2, 3, 4, 5, 6, 7, 8]
print test_list[0]

print test_list[-1]

print test_list[0:2]
print test_list[1:-1]

print test_list[0:]
print test_list[:-1]
print test_list[:]

print test_list[0::2]
print test_list[7:2:-1]

test_list_1 = ['a', 'b', 'c', 'd', 'e', 'f']
print test_list + test_list_1

none_list = [None]
print none_list * 5

print 1 in test_list
print 'A' in test_list_1

print len(test_list)
print max(test_list_1)
print min(test_list_1)
