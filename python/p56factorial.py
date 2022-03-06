i=1
m=1
n=int(input("Enter the number"))
while i<=n :
    m*=i
    print(i,"X ",end='')
    i=i+1
print("\nFact = ",m)