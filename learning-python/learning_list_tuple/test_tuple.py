#!/usr/bin/env python
# -*- UTF-8 -*-
__author__ = 'wxmimperio'

tuple_1 = 1, 2, 3
print tuple_1
tuple_2 = 5,
print tuple_2

tuple_empty = ()
print tuple_empty

print tuple([1, 2, 3, 4, 5, 6])

tuple_3 = tuple('tuple')
print tuple_3[1]
print tuple_3[2:5]

tuple_4 = tuple([1, 2, 3, ['a', 'b', 'c']])
tuple_4[3][0] = 'xx'
tuple_4[3][1] = 'yy'
print tuple_4
