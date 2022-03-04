
print("Press 1 for square")
print("Press 2 for cube")
print("Enter ur choice ")
op=int(input("here"))

if op==1:
    a = int(input("Enter the A number"))
    print("Square = ",a*a)
elif op==2:
    a= int(input("Enter the number"))
    print("Cube = ",a*a*a)
else:
    print("Wrong opt")
