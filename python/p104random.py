import  random
p=0
m= int(input("Enter the number"))
C=0
C1=0
n= input("Which operetar you choose:")

for i in range(1,m+1):
        x = random.randint(1,50)
        y= random.randint(1,50)
        print(x)
        print(y)
        if n == "+":
            p = x + y
            d = int(input("Enter the the  number"))
            if d == p:
                print("Right ans")
                C = C + 1
            else:
                print("Wrong ans")
                C1 = C1 + 1
        elif n=="-":
            p = x - y
            d = int(input("Enter the the  number"))
            if d == p:
                print("Right ans")
                C = C + 1
            else:
                print("Wrong ans")
                C1 = C1 + 1
        elif n == "*":
            p = x * y
            d = int(input("Enter the the  number"))
            if d == p:
                print("Right ans")
                C = C + 1
            else:
                print("Wrong ans")
                C1 = C1 + 1
        elif n == "/":
            p = x / y
            d = int(input("Enter the the  number"))
            if d == p:
                print("Right ans")
                C = C + 1
            else:
                print("Wrong ans")
                C1 = C1 + 1
        else:
            print("Wrong choice")
print("Right Ans",C)
print("Wrong Ans",C1)
