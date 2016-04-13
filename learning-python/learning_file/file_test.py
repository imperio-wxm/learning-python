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

# offset偏移
offset_path = os.path.abspath('../doc/offset_test.txt')
file_offset = open(offset_path, 'w')
file_offset.write("abcdefg")
file_offset.seek(2)
file_offset.write('12346')
file_offset.close()
file_offset = open(offset_path)
print file_offset.read()

# tell返回当前文件位置
file_tell = open(offset_path, 'w')
file_tell.seek(3)
print file_tell.tell()

