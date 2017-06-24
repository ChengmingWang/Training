#encoding=utf-8
# 序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。
# Python有6个序列的内置类型，但最常见的是列表和元组。
# 序列都可以进行的操作包括索引，切片，加，乘，检查成员。
# 此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。
# 列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。
# 列表的数据项不需要具有相同的类型
# 创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。

# 可以使用 del 语句来删除列表的的元素
list1=[1,2,3,]
del list1[2]
print list1*2

print len([1,2,3])#3
print list1[-2]#1
for o in list1:
    print o

for i in range(6):#i>=0 and i<6 int
    print (i)

#List常用函数
#cmp(list1, list2) 比较两个列表的元素
#cmp() 方法用于比较两个列表的元素。
# 如果比较的元素是同类型的,则比较其值,返回结果。
# 如果两个元素不是同一种类型,则检查它们是否是数字。
#     如果是数字,执行必要的数字强制类型转换,然后比较。
#     如果有一方的元素是数字,则另一方的元素"大"(数字是"最小的")
#     否则,通过类型名字的字母顺序进行比较。
# 如果有一个列表首先到达末尾,则另一个长一点的列表"大"。
# 如果我们用尽了两个列表的元素而且所 有元素都是相等的,那么结果就是个平局,就是说返回一个 0。
list1,list2=[1,'2'],[3,4,5,]
print cmp(list1, list2);#-1
print cmp(list2, list1);#1
list3 = list2 + [786];
print cmp(list2, list3)#-1

# len(list)列表元素个数

#max(list) 返回列表元素最大值
print 'max:'+ str(max([1,2,3,3]))#max:3
#min(list) 返回列表元素最小值

#list(seq)将元组转换为列表
tuple1=(1,2,3)
print type(list(tuple1))#<type 'list'>

#List常用方法
#list.append(obj)在列表末尾添加新的对象
list1=[1,2,3]
list1.append([4,5,6])
print list1#[1, 2, 3, [4, 5, 6]]
# list.extend(seq)在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list1.extend([7,8,9])
print list1#[1, 2, 3, [4, 5, 6], 7, 8, 9]
#list.insert(index, obj) insert() 函数用于将指定对象插入列表的指定位置。
aList = [123, 'xyz', 'zara', 'abc']
aList.insert( 3, 2017)
print "Final List : ", aList#Final List :  [123, 'xyz', 'zara', 2017, 'abc']

# list.count(obj) 统计某个元素在列表中出现的次数

#list.index(obj) 从列表中找出某个值第一个匹配项的索引位置

# list.pop(obj=list[-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
aList = [123, 'xyz', 'zara', 'abc'];
print "A List : ", aList.pop();#abc
print "B List : ", aList.pop(2);#zara

# list.remove(obj) 移除列表中某个值的第一个匹配项

# list.reverse()反向列表中元素
aList = [123, 'xyz', 'zara', 'abc', 'xyz'];
aList.reverse();
print "List : ", aList;#List :  ['xyz', 'abc', 'zara', 'xyz', 123]

# list.sort([func]) 对原列表进行排序
aList = [123, 'xyz', 'zara', 'abc', 'xyz'];
aList.sort();
print "List : ", aList;#List :  [123, 'abc', 'xyz', 'xyz', 'zara']