n= int(input("Enter the value"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(" ",end='')
    for j in range(n,i-1,-1):

        print("* ", end='')

    for j in range(1,i+1):
        print("  ",end='')
    for j in range(n,i-1,-1):

        print("* ", end='')
    print("")