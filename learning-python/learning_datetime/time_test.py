#!/usr/bin/env python
# -*- encoding:UTF-8 -*-
__author__ = 'wxmimperio'

from datetime import time

# time类相关操作

# 构造函数创建时间
now_time = time(10, 12, 13, 856)
print now_time

# 最小、最大时间
print now_time.min, now_time.max

# 时间的最小单位，微妙
print now_time.resolution

# 时、分、秒、微秒
print now_time.hour, now_time.minute, now_time.second, now_time.microsecond

# 创建一个新的时间对象,用参数指定的时、分、秒、微秒代替原有对象中的属性
new_time = now_time.replace(hour=19, second=50)
print new_time

# 返回型如"%H:%M:%S"格式的字符串表示
print now_time.isoformat()

# 返回自定义格式化字符串。在下面详细介绍
fmt = "%H:%M:%S:%f"
print now_time.strftime(fmt)
