#!/usr/bin/python
#coding=UTF-8

#phthon保留字符
# and	exec	not
# assert	finally	or
# break	for	pass
# class	from	print
# continue	global	raise
# def	if	return
# del	import	try
# elif	in	while
# else	is	with
# except	lambda	yield

# 学习 Python 与其他语言最大的区别就是，Python 的代码块不使用大括号 {} 来控制类，函数以及其他逻辑判断。python 最具特色的就是用缩进来写模块。
# 缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行。
if 1==1:
    print "aaa";
else:
    print "bbb";

# Python语句中一般以新行作为为语句的结束符。
# 但是我们可以使用反斜杠（ \）将一行的语句分为多行显示
num=1+\
    2;
# 语句中包含 [], {} 或 () 括号就不需要使用多行连接符。
days = ['Monday', 'Tuesday',
        'Wednesday',
        'Thursday', 'Friday'];

# Python 可以使用引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串，引号的开始与结束必须的相同类型的。
# 其中三引号可以由多行组成，编写多行文本的快捷语法，常用于文档字符串，在文件的特定地点，被当做注释。
word = 'word'
sentence = "这是一个句子。"
paragraph = '''这是一个段落
。
包含了多个语句'''

# python 中多行注释使用三个单引号(''')或三个双引号(''' or """)。
'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""

# 函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
# 空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
# 记住：空行也是程序代码的一部分。

# 下面的程序执行后就会等待用户输入，按回车键后就会退出：
raw_input("\n\nPress the enter key to exit.");

# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号：
print 1,
print 2 #输出结果1 2

# 缩进相同的一组语句构成一个代码块，我们称之代码组。
# 像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
# 我们将首行及后面的代码组称为一个子句(clause)。