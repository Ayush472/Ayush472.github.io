
while True:
    print("Press 1 For add")
    print("Press 2 For sub")
    print("Press 3 For Mul")
    print("Press 4 For Div")
    print("Press 5 For Exit")
    print("Enter ur choice")

    op=int(input("here"))
    if op==1:
        num1=float(input("Enter the number"))
        num2=float(input("Enter the number"))
        print("Add = ",num1+num2)
    elif op==2:
        num1=float(input("Enter the number"))
        num2=float(input("Enter the number"))
        print("Sub = ",num1-num2)
    elif op==3:
        num1=float(input("Enter the number"))
        num2=float(input("Enter the number"))
        print("Mul = ",num1*num2)
    elif op==4:
        num1=float(input("Enter the number"))
        num2=float(input("Enter the number"))
        print("Div = ",num1/num2)
    elif op==5:
        break
    else:
        print("Wrong choice")