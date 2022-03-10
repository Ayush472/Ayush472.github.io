import  random
p=0
m= int(input("Enter the number"))
for i in range(1,m):
    x = random.randint(1,50)
    y= random.randint(1,50)
    print(x)
    print(y)
    p = x + y
    n = int(input("Enter the the  number"))

    if n==p:
        print("Right ans")
    else:
        print("Wrong ans")