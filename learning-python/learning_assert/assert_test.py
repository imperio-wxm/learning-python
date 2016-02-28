#!/usr/bin/env python
# -*- UTF-8 -*-
__author__ = 'wxmimperio'

a = 10
assert a > 0, 'a > 0'
assert a < 20, 'a < 20'
# assert a%2 != 0, 'a is not an even number'


def assert_test(a, b):
    return a + b

assert 3 == assert_test(1, 2), 'right'
assert 3 == assert_test(1, 4), 'error'
