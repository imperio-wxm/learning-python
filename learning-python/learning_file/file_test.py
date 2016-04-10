#!/usr/bin/env python
# -*- encoding:UTF-8 -*-
__author__ = 'wxmimperio'

import os

file_path = os.path.abspath('../doc/file_test.txt')
print file_path

# 读文件
file_read = open(file_path, 'r+')
print file_read.read()
file_read.close()

# 写文件
file_wtite = open(file_path, 'a+')
file_wtite.write("This is a test!".decode("utf-8"))
file_wtite.close()