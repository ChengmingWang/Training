list=[15,12,4,32,17,77,98,56]
temp=0#temporary variable
#sort by asc
for i in range(len(list)):
    for j in range(len(list) - i - 1):
        if list[j] > list[j + 1]:
            temp=list[j]
            list[j]=list[j + 1]
            list[j + 1]=temp
print list