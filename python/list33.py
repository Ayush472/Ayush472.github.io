list1=[11,55,77,80]
list2=[20,55,33,11]
list3=[]

for i in list1:
    list3.append(i)
for i in list2:

    if i not in list1:
        print(i)
        list3.append(i)
print(list3)
