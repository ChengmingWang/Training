#coding=utf-8
# Python 程序能用很多方式处理日期和时间，转换日期格式是一个常见的功能。
# Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。
# 时间间隔是以秒为单位的浮点小数。

import  time
# struct_time元组。这种结构具有如下属性
# 0	tm_year	2008
# 1	tm_mon	1 到 12
# 2	tm_mday	1 到 31
# 3	tm_hour	0 到 23
# 4	tm_min	0 到 59
# 5	tm_sec	0 到 61 (60或61 是闰秒)
# 6	tm_wday	0到6 (0是周一)
# 7	tm_yday	1 到 366(儒略历)
# 8	tm_isdst	-1, 0, 1, -1是决定是否为夏令时的旗帜

#本地时间
local_time=time.localtime(time.time())
print "本地时间为 :", local_time

#格式化时间
print time.strftime("%Y-%M-%D %H:%M:%S",time.localtime())

#获取某月日历
import calendar
print calendar.month(2017,6)