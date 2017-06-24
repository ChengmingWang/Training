#_*_encoding:utf-8_*_
# 函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。
# 函数能提高应用的模块性，和代码的重复利用率。你已经知道Python提供了许多内建函数，比如print()。但你也可以自己创建函数，这被叫做用户自定义函数。

# 你可以定义一个由自己想要功能的函数，以下是简单的规则：
#     函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
#     任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
#     函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
#     函数内容以冒号起始，并且缩进。
#     return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

# def functionname( parameters ):
#    "函数_文档字符串"
#    function_suite
#    return [expression]
# 默认情况下，参数值和参数名称是按函数声明中定义的的顺序匹配起来的。

def printAny(obj):
    print(obj)
    return #返回None

# 定义一个函数只给了函数一个名称，指定了函数里包含的参数，和代码块结构。
# 这个函数的基本结构完成以后，你可以通过另一个函数调用执行，也可以直接从Python提示符执行。
printAny({1:1,2:2})

# 在 python 中，类型属于对象，变量是没有类型的：
a=[1,2,3]
a="Runoob"
# [1,2,3] 是 List 类型，"Runoob" 是 String 类型，而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），可以是 List 类型对象，也可以指向 String 类型对象。

# 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
#     不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
#     可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

# python 函数的参数传递：
#     不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
#     可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响
# python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。

def ChangeInt( a ):
    a = 10
b = 2
ChangeInt(b)
print b #  2
# 有 int 对象 2，指向它的变量是 b，在传递给 ChangeInt 函数时，按传值的方式复制了变量 b，a 和 b 都指向了同一个 Int 对象，在 a=10 时，则新生成一个 int 值对象 10，并让 a 指向它。

def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4]);
   print "函数内取值: ", mylist
   return
changeme(['cd','dsfds','dsfdsfsd'])#函数内取值:  ['cd', 'dsfds', 'dsfdsfsd', [1, 2, 3, 4]]

# 以下是调用函数时可使用的正式参数类型：
#     必备参数
#     关键字参数
#     默认参数
#     不定长参数

# 必备参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。

# 关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
# 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
# 调用函数时，缺省参数的值如果没有传入，则被认为是默认值。
def keyPara(para1,para2,para3='888'):
    print para1+','+para2+','+para3
    return
keyPara(para2="2", para1="1")

# 你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名。
# 语法:
# def functionname([formal_args,] *var_args_tuple ):
#    "函数_文档字符串"
#    function_suite
#    return [expression]
# 加了星号（*）的变量名会存放所有未命名的变量参数。选择不多传参数也可。
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print "输出: "
    print arg1
    for var in vartuple:
        print var
    return;
# 调用printinfo 函数
printinfo(10);
printinfo(70, 60, 50);

#匿名函数
# python 使用 lambda 来创建匿名函数。
#     lambda只是一个表达式，函数体比def简单很多。
#     lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
#     lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
#     虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
sum = lambda arg1, arg2: arg1 + arg2;
print "相加后的值为 : ", sum(20, 10)
# sum=lambda  a1,*args:
# print "相加后的值为 : ", sum(20, 20,30)

# 全局变量想作用于函数内，需加 global
globvar =0
def set_globvar_to_one():
    global globvar    # 使用 global 声明全局变量
    globvar = 1
set_globvar_to_one()
print globvar#1
# 1、global---将变量定义为全局变量。可以通过定义为全局变量，实现在函数内部改变变量值。
# 2、一个global语句可以同时定义多个变量，如 global x, y, z。