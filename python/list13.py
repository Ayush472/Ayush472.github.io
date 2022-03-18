import random

list1=[]
list2=[]
n=int(input("Enter limit "))
m=int(input("Enter limit "))

for i in range(1,n+1):
    x=random.randint(-30,30)

    list1.append(x)

print(list1)



for i in range(1,n+1):
    y = random.randint(-30, 30)
    list2.append(y)

print(list2)


print(list1+list2)


