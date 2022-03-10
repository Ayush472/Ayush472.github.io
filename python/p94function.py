def cube(a):
    print("Cube =>",a*a*a)

def max(a,b):
    if a>b:
        print("maximum number of a")
    else:
        print("minmum number of a")

def add(a,b):
    print("Addition of  two number=", a + b)


a= int(input("Enter the number"))
b= int(input("Enter the number"))
max(a,b)
cube(a)
add(a,b)