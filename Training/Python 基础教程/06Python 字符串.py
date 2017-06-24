#_*_coding:utf-8_*_
# r/R 原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。
#  原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。
print '\000'
print r'\000'
print "\v"
print R"\v"

# Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。
# 在 Python 中，字符串格式化使用与 C 中 sprintf 函数一样的语法。
print 'age:%d,name:%s,score:%.2f' %(20,'Jack',86.466)

#常用字符串内建函数
#string.count(str, beg=0, end=len(string)) 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
print 'sdfdsfsf'.count('s',2,99)
#string.endswith(obj, beg=0, end=len(string)) 检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
print 'sdfdfklgjkdflg'.endswith('l')
#string.find(str, beg=0, end=len(string)) 检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
str1 = "this is string example....wow!!!";
str2 = "exam";
print str1.find(str2);#15
print str1.find(str2, 10);#15
print str1.find(str2, 40);#-1
#string.format() 格式化字符串
# Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。
# 基本语法是通过 {} 和 : 来代替以前的 %  , format 函数可以接受不限个参数，位置可以不按顺序。
print('{},{}'.format("hello",'world')) # 不设置指定位置，按默认顺序
print "{1} {0} {1}".format("hello", "world")  # 设置指定位置
print("网站名：{name}, 地址 {url}".format(name="haha",url="hehe",dfdf="xdfvxcvcxv"))
# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是可选的
#也可以向 str.format() 传入对象
#我们可以使用大括号 {} 来转义大括号
print ("{} 对应的位置是 {{0}}".format("runoob"))#runoob 对应的位置是 {0}
# string.index(str, beg=0, end=len(string)) 跟find()方法一样，只不过如果str不在 string中会报一个异常.
str1 = "this is string example....wow!!!";
str2 = "exam";
print str1.index(str2);
print str1.index(str2, 10);
#print str1.index(str2, 40);#异常
#string.join(seq) 以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
str = "-";
seq = ("a", "b", "c");
print str.join(seq)
#string.partition(str) 有点像 find()和 split()的结合体,
# 从 str 出现的第一个位置起,把 字 符 串 string 分 成 一 个 3 元 素 的 元 组 (string_pre_str,str,string_post_str),
# 如果 string 中不包含str 则 string_pre_str == string.
str = "http://www.w3cschool.cc/"
print str.partition("://")#('http', '://', 'www.w3cschool.cc/')
print str.partition("dsfsdfds")#('http://www.w3cschool.cc/', '', '')
#string.replace(str1, str2,  num=string.count(str1))  把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.
str = "this is string example....wow!!! this is really string";
print str.replace("is", "was");
print str.replace("is", "was", 3);
#string.split(str="", num=string.count(str)) 以 str 为分隔符切片 string，如果 num有指定值，则仅分隔 num+1 个子字符串
str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print str.split();#['Line1-abcdef', 'Line2-abc', 'Line4-abcd']
print str.split(' ', 1);#['Line1-abcdef', '\nLine2-abc \nLine4-abcd']
#string.strip([obj]) Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）。
str = "0000000this is string example....wow!!!0000000";
print str.strip( '0' );
#string.translate(str, del="") 根据 str 给出的表(包含 256 个字符)转换 string 的字符,要过滤掉的字符放到 del 参数中
from string import maketrans   # 引用 maketrans 函数。
#intab与outtab长度要相同,要替换的字符一一对应
intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)
str = "this is string example....wow!!!";
print str.translate(trantab);#th3s 3s str3ng 2x1mpl2....w4w!!!