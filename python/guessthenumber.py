import  random
p=0
c=0
x = random.randint(1,20)
s1=1
s2=20
print(x)
for i in range(1,20):
    n = int(input("Enter the the  number"))
    c = c + 1
    if n==x:
        print("Right ans")
        break
    elif n<x:
        print("Please Enter the Greaterthan value")
        s1=x
        print("range",s1,"to",s2)
    else:
        print("please Enter the less than value")
        s2=x
        print("range", s1, "to",s2 )

print("Count",c)
