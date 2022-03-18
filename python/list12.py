import random

list1=[]

n=int(input("Enter limit "))
s=0
s1=0
c=0
c1=0
for i in range(1,n+1):
    x=random.randint(-30,30)
    list1.append(x)
y=0
print(list1)
for x in list1:
    print(x*-1)
