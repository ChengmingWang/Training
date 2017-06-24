#encoding=utf-8
# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
tup = ('physics', 'chemistry', 1997, 2000);
print tup;
del tup;

# 无关闭分隔符 任意无符号的对象，以逗号隔开，默认为元组
a='abc', -4.24e93, 18+6.6j, 'xyz'
print type(a)#<type 'tuple'>

#元组内置函数

# cmp(tuple1, tuple2) 比较两个元组元素

#len(tuple) 计算元组元素个数

# max(tuple) 返回元组中元素最大值

#min(tuple) 返回元组中元素最小值

#tuple(seq) 将列表转换为元组
print type(tuple([1,2,3]))#<type 'tuple'>
