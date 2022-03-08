n = int(input("Enter the number=>"))
k=n
for i in range(1,n+1):
    for j in range(1,i+1):

        print(" ",end='')
    for j in range(n,i-1,-1):

        print(k,end='')
    k=k-1
    print("")
