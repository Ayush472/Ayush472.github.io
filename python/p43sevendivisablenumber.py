n= int(input("Enter the number"))
sum=0
for i in range(1,n+1):
    if i%7==0:
        print(i)
        sum = sum+i
print(sum)