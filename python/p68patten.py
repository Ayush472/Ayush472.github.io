n =  int(input("Enter the number"))

for i in range(1,n+1):
    k=n
    for j in range(1,i+1):

        print(k,end='')
        k=k-1
    print("")