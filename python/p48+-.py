n=int(input("Enter the number"))
m=1

for i in range(1,n+1):
    if i%2==0:
        m-=i
        print("-",i, end='')
    else:
        m+=i
        print( " + ",i, end='')
print("\nSum = ",m)