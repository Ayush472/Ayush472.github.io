list1=[11,55,77,80]
list2=[20,55,33,11]
list3=[]
list4=[]
for i in list1:

    if i in list2:
        pass
    else:
        list3.append(i)
print(list3)
for i in list2:
    if i in list1:
        pass
    else:
        list4.append(i)
print(list4)
