#!/usr/bin/env python
# -*- UTF-8 -*-
__author__ = 'wxmimperio'

list_1 = list("I am wxmimperio")
print list_1

list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_2[1] = 'a'
print list_2

del list_2[2]
print list_2

list_2[6:] = list("hello")
print list_2

list_3 = [1, 6]
list_3[1:1] = [2, 3, 4, 5]
print list_3

list_3[1:4] = []
print list_3

list_4 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
list_4.append(1)
print list_4

conut = list_4.count('a')
print conut

list_4.extend([2, 3, 4])
print list_4
print (len(list_4))

print list_4.index('b')
# print list_4.index('xx')

list_4.insert(2, 'wxm')
print list_4

print list_4.pop()
print list_4.pop(2)

list_4.insert(3, 1)
list_4.remove(1)
print list_4

list_4.reverse()
print list_4

for x in reversed(list_4):
    print x,

list_5 = [88, 1, 9, 5, 20]
list_5_1 = list_5[:]
list_5_1.sort()
print list_5_1

list_6 = ['xx', 'ab', 'g', 'y23', 'i85dfa']
list_6.sort(key=len, reverse=True)
print list_6
