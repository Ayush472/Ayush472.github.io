n = int(input("Enter the number for factorial"))
m= 1
if n <= 0:
    print("")
else:
    for i in range(1,n+1):
            print(i," X ",end='')
            m*=i
    print("\nFact = ",m)

