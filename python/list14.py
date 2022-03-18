import random

list1=[]
list2=[]
list3=[]
n=int(input("Enter limit "))

for i in range(1,n+1):
    x=random.randint(-30,30)

    list1.append(x)
print(list1)

for x in list1:

    if x%2==0:
        list2.append(x)
    else:
        list3.append((x))
print(list2)
print(list3)