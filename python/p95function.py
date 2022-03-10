def cube(a):
    return  a**3

def max(a,b):
    if a>b:
        return a
    else:
        return b
def add(a,b):
    return a+b

def cal(a,b):
    return a+b,a-b,a/b,a*b

a= int(input("Enter the number"))
b= int(input("Enter the number"))
c=max(a,b)
print("Max=",c)
c=cube(a)

x=cube(c)
print("Cube = ",x)
c=add(a,b)
print("ADD = ",c)

a,s,d,m=cal(22,2)
print("Add ",a)
print("sub ",s)
print("Div ",d)
print("Mul ",m)