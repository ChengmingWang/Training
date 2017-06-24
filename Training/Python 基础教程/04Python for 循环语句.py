#coding=utf-8
import random
#for循环
for letter in 'starmerx':
    print letter+'-',

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
    for word in fruit:
        print word,
    print fruit,

#while循环

# r=random.uniform(1,10)
# print r
# input1=input("\nPlease input:\n")
# while True:
#     if input1>r:
#         print 'bigger'
#         input1 = input("Please input:\n")
#     if input1<r:
#         print 'smaller'
#         input1 = input("Please input:\n")
#     if input1==r:
#         break
#或者
r=random.uniform(1,10)
print r
#raw_input把所有输入当作字符串,需要转换类型再比较结果才准确
input1=int(raw_input("\nPlease input:\n"))
while True:
    if input1>r:
        print 'bigger'
        input1 = int(raw_input("Please input:\n"))
    if input1<r:
        print 'smaller'
        input1 = int(raw_input("Please input:\n"))
    if input1==r:
        break