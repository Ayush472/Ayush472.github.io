def add():
    a = int(input("ENter the number"))
    b = int(input("ENter the number"))

    print("Sum =", a + b)


def  fact():
    n = int(input("Enter the number for factorial"))
    m = 1
    if n <= 0:
        print("")
    else:
        for i in range(n, 0, -1):
            print(i, " X ", end='')
            m *= i
        print("\nFact = ", m)


def tabel():
    num = int(input("Enter the number for table"))
    for i in range(1,11):

        print( num ,"x",i ,"=", num*i )


def oddeven():
    n = int(input("Enter the number"))
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i, "even")
        else:
            print(i, "odd")

def  areaoftriangel():
    h = float(input("Enter the highet Value"))
    b = float(input("Enter the Base Value"))
    print("Area of triangle =", h * b * (0.5))

def mtoc():
    M = float(input("Enter the meter Value"))
    print("Centimeter", M * 100)


add()
mtoc()
tabel()
fact()
areaoftriangel()
oddeven()