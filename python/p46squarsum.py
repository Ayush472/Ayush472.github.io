n=int(input("Enter the number"))
m=1
if n<=0:
    print("")
for i in range(1,n+1):
    m+=i*i
    print(i*i, " + ", end='')
print("\nSum = ",m)