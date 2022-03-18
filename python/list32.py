list1=[11,55,77,80]
list2=[20,55,33,11]
list3=[]
for i in list1:
    if i in list2:
        list3.append(i)
print(list3)