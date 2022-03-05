n=int(input("Enter the  number"))
total=0
for i in range(1,n+1):
    if i%2 == 0:
        print(i)

        total = total+i
print(total)