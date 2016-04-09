#!/usr/bin/env python
# -*- encoding:UTF-8 -*-
__author__ = 'wxmimperio'

from datetime import datetime, time, date

# datetime相关操作

# 获取当前时间
now_datetime = datetime.now()
print now_datetime

# 最小值与最大值
print now_datetime.min, now_datetime.max

# datetime最小单位
print now_datetime.resolution

# 获取datetime的年、月、日、时、分、秒、时区
print now_datetime.year, now_datetime.month, now_datetime.day
print now_datetime.hour, now_datetime.minute, now_datetime.second, now_datetime.microsecond
print now_datetime.tzinfo

# 返回一个表示当前本地时间的datetime对象
print now_datetime.today()

# 返回一个当前utc时间的datetime对象
print now_datetime.utcnow()

# 根据时间戮创建一个datetime对象,参数tz指定时区信息
timesstamp = 1451577600
print datetime.fromtimestamp(timesstamp)

# 根据时间戮创建一个datetime对象
print datetime.utcfromtimestamp(timesstamp)

# 根据date和time,创建一个datetime对象
new_date = date.today()
new_time = time(12, 12, 12)
print datetime.combine(new_date, new_time)

# 将格式字符串转换为datetime对象
fmt = "%Y-%m-%d %H:%M:%S:%f"
fmt_datetime = "2016-1-2 12:8:52:2569"
print datetime.strptime(fmt_datetime, fmt)

# 将datetime对象格式化成字符串
datetime_str = datetime.today().strftime("%Y-%m-%d %H:%M:%S:%f")
print datetime_str

# 获取星期
print datetime.today().weekday()

# 转换成UTC的元祖
print datetime.today().utctimetuple()
