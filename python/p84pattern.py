n = int(input("Enter the number=>"))
for i in range(n,1,-1):
    for j in range(1,i+1):
        print(" ",end='')
    for j in range(n,i-1,-1):

        print("* ", end='')


    for j in range(1,i+1):
        print("  ",end='')
    for j in range(n,i-1,-1):

        print("* ", end='')

    print("")