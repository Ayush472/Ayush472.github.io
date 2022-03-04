print("Press 1 For area of triangle")
print("Press 2 For maximum value")
print("Press 3 For Positive & Negative")
print("Here")

op = int(input("Enter Your choice"))

if op==1:
    b=float(input("Enter the Base"))
    h=float(input("enter the height"))
    print("Area Of Triangle :",b*h*0.5)
elif op==2 :
    a=int(input("Enter the number"))
    b=int(input("Enter the number"))
    if a>b:
        print("Maximum number:")
    else:
        print("min")

elif op==3:
    a = int(input("Enter the number"))
    if a>0:
        print(a," is Positive Value")
    else:
        print("Negative value")

else:
    print("Wrong choice")