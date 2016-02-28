#!/usr/bin/env python
# -*- UTF-8 -*-
__author__ = 'wxmimperio'

age_dict = {'Alex': 22, 'Bob': 21, 'Tom': 25, 'Beth': 18}
print age_dict

student_list = [('name', 'Alex'), ('age', 20), ('gender', 'male')]
student_dict = dict(student_list)
print student_dict
print student_dict['name']

student_list_1 = dict(name='Tom', age=20)
print student_list_1

print len(student_dict)
print student_dict['gender']
student_dict['age'] = 23
print student_dict
del student_dict['age']
print student_dict
result = 'name' in student_dict
print result

hobby_dict = {'Bob': 'game', 'Alex': 'tennis', 'Tom': 'basketball'}
print "My hobby is %(Tom)s" % hobby_dict

clear_dict = {'name': 'Bob', 'age': 23}
clear_dict.clear()
print clear_dict

light_copy = {'name': 'Tom', 'hobby': ['basketball', 'fishing']}
light_copy_dict = light_copy.copy()
light_copy_dict['name'] = 'Alex'
print light_copy
print light_copy_dict['hobby'].remove('fishing')
print light_copy
print light_copy_dict

from copy import deepcopy

deepcopy_dict = {}
deepcopy_dict['names'] = ['Tome', 'Tob', 'Alex']
deepcopy_dict_1 = deepcopy_dict.copy()
deepcopy_dict_2 = deepcopy(deepcopy_dict)
deepcopy_dict_2['names'].append('Jack')
print deepcopy_dict_1
print deepcopy_dict_2

print dict.fromkeys(['name', 'age'])
print dict.fromkeys(['name', 'age'], 'NULL')

print deepcopy_dict.get('xxx')
print deepcopy_dict.get('names')
print deepcopy_dict.get('yyy', 'NULL')

print deepcopy_dict.has_key('names')
print deepcopy_dict.has_key('age')

print hobby_dict.items()
for x in hobby_dict.iteritems():
    print x,

print '\n'

print hobby_dict.keys()
for x in hobby_dict.iterkeys():
    print x,
print '\n'

pop_dict = {'name': 'Tom', 'age': 20}
print pop_dict.pop('name')
print pop_dict

popitem_dict = {'name': 'Alex', 'gender': 'male', 'age': 20, 'hobby': 'tennis'}
print popitem_dict.popitem()
print popitem_dict

setdefault_dict = {}
setdefault_dict.setdefault('name', 'NULL')
print setdefault_dict
setdefault_dict['name'] = 'Tom'
print setdefault_dict.setdefault('name', 'xxx')
print setdefault_dict

update_dict = {'name': 'Alex', 'gender': 'male', 'age': 20, 'hobby': 'tennis'}
change_dict = {'language': 'chinese'}
update_dict.update(change_dict)
print update_dict

print update_dict.values()
for x in update_dict.itervalues():
    print x,
