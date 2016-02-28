#!/usr/bin/env python
# -*- UTF-8 -*-
__author__ = 'wxmimperio'

set_list = [1, 2, 2, 2, 3, 4, 5, 5, 6]
print set(set_list)

set_1 = set([1, 2, 3, 4, 5])
set_2 = set([3, 4, 5, 6, 7, 8])
print set_1 & set_2

print set_1 | set_2

print set_1 - set_2

print set_1 ^ set_2

set_3 = set([0, 1, 2, 3])
set_3.add(4)
print set_3
set_3.update([5, 6])
print set_3

print len(set_3)

print 0 in set_3
print 10 in set_3

set_3.discard(1)
print set_3

print set_3.pop()
print set_3

set_3.clear()
print set_3
