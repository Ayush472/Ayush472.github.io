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

for x in list1:
    if x%2==0:
        print(x,"even")
        s +=x
        c=c+1
    else:
        print(x,'Odd')
        s1+=x
        c1=c1+1


print("Even Number Of Sum = ",s)
print("Odd Number Of Sum = ",s1)

print("Even Number count = ",c)
print("Odd Number count = ",c1)

