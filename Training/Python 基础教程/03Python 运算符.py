#coding=utf-8

# 算术运算符
# ** 幂 - 返回x的y次幂
a=5
print a**2 #25
# //取整除 - 返回商的整数部分
print a//6 #0
# 注意：Python2.x 里，整数除整数，只能得出整数。如果要得到小数部分，把其中一个数改成浮点数即可。
print 1/float(2) #0.5

# 位运算符
# ~ 按位取反运算符
a=40
print ~a #-41

#逻辑运算符
#and or not

#成员运算符
# in 如果在指定的序列中找到值返回 True，否则返回 False。
# not in 如果在指定的序列中没有找到值返回 True，否则返回 False。
a = 10
b = 20
list = [1, 2, 3, 4, 5,10 ]
if a in list:
    print 'a in list'
if b not in list:
    print 'b not in list'

#身份运算符
# is 判断两个标识符是不是引用自一个对象
# is not 判断两个标识符是不是引用自不同对象
a = 20
b = 20
if (a is b):
    print "1 - a 和 b 有相同的标识" #
else:
    print "1 - a 和 b 没有相同的标识"
a=24
if (a is not b):
    print "2 - a 和 b 没有相同的标识"#
else:
    print "2 - a 和 b 有相同的标识"

# is 与 == 区别：
# is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
a = [1, 2, 3]
b=a
print b is a #True
b=a[:]
print b == a #True
print b is a #False

#运算符优先级
# **指数 (最高优先级)
# ~ @+ @-按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
# * / % //乘，除，取模和取整除
# + -加法减法
# >> <<右移，左移运算符
# & 位与运算符
# |^ 位运算符
# <= < > >= 比较运算符
# <> == != 等于运算符
# = %= /= //= -= += *= **= 赋值运算符
# is is not 身份运算符
# in not in 成员运算符
# and or not 逻辑运算符