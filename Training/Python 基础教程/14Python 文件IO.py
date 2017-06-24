#encoding=utf-8
# raw_input([prompt]) 函数从标准输入读取一个行，并返回一个字符串（去掉结尾的换行符）
print raw_input("please input:\n")#
print type(raw_input("please input:\n"))#<type 'str'>
# input([prompt]) 函数和 raw_input([prompt]) 函数基本类似，但是 input 接收一个Python表达式作为输入，并将运算结果返回。
# 输入字符串的时候必须使用引号将它括起来，否则它会引发一个 SyntaxError 。
print input("please input:\n")
print type(input("please input:\n"))#如输入1+6,返回7,类型<type 'int'>

#你必须先用Python内置的open()函数打开一个文件，创建一个file对象，相关的方法才可以调用它进行读写。
fo = open("foo.txt", "wb")
print "文件名: ", fo.name
print "是否已关闭 : ", fo.close()
print "访问模式 : ", fo.mode
print "末尾是否强制加空格 : ", fo.softspace