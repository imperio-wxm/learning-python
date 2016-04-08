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

# 生成一个新的日期对象
replace_date = now_time.replace(year=1990)
print replace_date

# 返回日期对应的time.struct_time对象
print now_time.timetuple()

# 返回weekday,如果是星期一,返回0,如果是星期2,返回1,以此类推.
print now_time.weekday()

# 返回格式如(year,month,day)的元组
print now_time.isocalendar()

# 返回格式如'%Y-%m-%d'的字符串
print now_time.isoformat()

# 自定义格式化字符串
fmt = "%Y-%m-%d %H:%M:%S"
print now_time.strftime(fmt)

# 两个日期运算
date_1 = date(1992, 1, 20)
date_2 = date(2000, 5, 3)
print "date_2 - date_1 = {0}".format(date_2 - date_1)

# 比较日期时返回True or False
if date_1 > date_2:
	print "date_1 > date_2"
else:
	print "date_1 < date_2"
