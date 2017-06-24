#encoding=utf-8

# 捕捉异常可以使用try/except语句。
# try/except语句用来检测try语句块中的错误，从而让except语句捕获异常信息并处理。
# 如果你不想在异常发生时结束你的程序，只需在try里捕获它。

# 语法：
# try:
# <语句>        #运行别的代码
# except <名字>：
# <语句>        #如果在try部份引发了'name'异常
# except <名字>，<数据>:
# <语句>        #如果引发了'name'异常，获得附加的数据
# else:
# <语句>        #如果没有异常发生

# try的工作原理是，当开始一个try语句后，python就在当前程序的上下文中作标记，这样当异常出现时就可以回到这里，try子句先执行，接下来会发生什么依赖于执行时是否出现异常。
# 如果当try后的语句执行时发生异常，python就跳回到try并执行第一个匹配该异常的except子句，异常处理完毕，控制流就通过整个try语句（除非在处理异常时又引发新的异常）。
# 如果在try后的语句里发生了异常，却没有匹配的except子句，异常将被递交到上层的try，或者到程序的最上层（这样将结束程序，并打印缺省的出错信息）。
# 如果在try子句执行时没有发生异常，python将执行else语句后的语句（如果有else的话），然后控制流通过整个try语句。


try:
    fh=open("hehe","rb")
    fh.write("haha")
except IOError:
    print 'IOError'
else:
    print "file write successfully!"
    fh.close()

# 变量接收的异常值通常包含在异常的语句中。在元组的表单中变量可以接收一个或者多个值。
# 元组通常包含错误字符串，错误数字，错误位置。
