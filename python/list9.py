import random

list1=[]

n=int(input("Enter limit "))
s=0
s1=0
c=0
c1=0
for i in range(1,n+1):
    x=random.randint(1,30)
    list1.append(x)

print(list1)
p=int(input("Which number to divisable"))
for x in list1:
    if x%p==0:
        print(x)
        s +=x
        c=c+1



print("Sum = ",s)


print("count = ",c)
