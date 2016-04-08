#!/usr/bin/env python
# -*- encoding:UTF-8 -*-
__author__ = 'wxmimperio'

# data类相关操作

from datetime import date

# 利用构造函数创建日期
now_time = date(2016, 1, 1)
print now_time

# 最大最小日期
print now_time.min, now_time.max

# 表示日期的最小单位
print now_time.resolution

# 取得年、月、日
print "year={0},month={1},day={2}".format(now_time.year, now_time.month, now_time.day)

# 返回一个表示当前本地日期的date对象
print date.today()

# 根据给定的时间戮,返回一个date对象
timesstamp = 1451577600
print date.fromtimestamp(timesstamp)
