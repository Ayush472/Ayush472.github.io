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
y=int(input("Enter the number"))

for x in list1:
    if x==y:
        print(x)
        c=c+1
    else:
        print(y," number is not in this list ")
print("Even Number count = ",c)
