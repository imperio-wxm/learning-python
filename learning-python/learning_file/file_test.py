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

"""
# 写文件
file_wtite = open(file_path, 'a+')
file_wtite.write("\nThis is a test!".decode("utf-8"))
file_wtite.close()
"""

# 读一行数据
file_readline = open(file_path, 'r+')
print file_readline.readline().decode("utf-8")
# 读指定行数
lines = file_readline.readlines(2)
for line in lines:
	print line
file_readline.close()

"""
# 写入一个字符串列表
str_list = ["a\n", "b\n", "c\n"]
file_writelines = open(file_path, 'a+')
file_writelines.writelines(str_list)
file_writelines.close()
"""
