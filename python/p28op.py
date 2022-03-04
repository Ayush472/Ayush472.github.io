print("Press area For area of triangle")
print("Press m For maximum value")
print("Press p For Positive & Negative")
print("Here")

op = input("Enter Your choice").lower()

if op == "area":
    b = float(input("Enter the Base"))
    h = float(input("enter the height"))
    print("Area Of Triangle :", b * h * 0.5)
elif op == "m":
    a = int(input("Enter the number"))
    b = int(input("Enter the number"))
    if a > b:
        print("Maximum number:")
    else:
        print("min")

elif op == 3:
    a = int(input("Enter the number"))
    if a > 0:
        print(a, " is Positive Value")
    else:
        print("Negative value")

else:
    print("Wrong choice")