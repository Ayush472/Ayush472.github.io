print("Press add For addition")
print("Press sub For subtraction")
print("Press mul For Multiplication")
print("Press div For Division")
print("Press s For Square")
print("Press c For Cube")
print("Here")

op=input("Enter your Choice").lower()

if op== "add":
    a=int(input("Enter the number"))
    b=int(input("Enter the number"))
    print("Addition = ",a+b)
elif op=="sub":
    a = float(input("Enter the number"))
    b = float(input("Enter the number"))
    print("Subtraction = ", a - b)
elif op=="mul":
    a = float(input("Enter the number"))
    b = float(input("Enter the number"))
    print("Multiplication = ", a * b)
elif op=="div":
    a = float(input("Enter the number"))
    b = float(input("Enter the number"))
    print("Division = ", a / b)
elif op=="s":
    a = float(input("Enter The number"))
    print("Square = ",a*a)
elif op=="c":
    a = float(input("Enter The Number"))
    print("Cube = ",a*a*a)
else:
    print("Wrong Choice")