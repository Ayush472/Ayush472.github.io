
pi=200
r=170
f=100
b=90
i=70
bm=20
bill1=0
bill2=0
bill3=0
bill4=0
bill5=0
bill6=0
while True:
    print("Press 1 For Pizza")
    print("Press 2 For Vge. Roll")
    print("Press 3 For fix pack lunch")
    print("Press 4 For brownie")
    print("Press 5 For Ice Cream")
    print("Press 6 for Butter Milk")
    print("Press 7 for Exit")

    op =int(input("Enter your Choice"))

    if op==1:
        qty= int(input("Enter the qty of Pizza"))
        bill1 = (qty * pi)

    elif op==2:
        qty = int(input("Enter the qty of Vge.ROll"))
        bill2=(qty * r)

    elif op==3:
        qty = int(input("Enter the qty of fix lunch"))
        bill3 = qty * f

    elif op==4:
        qty = int(input("Enter the qty of Brownie"))
        bill4=(qty*b)
    elif op==5:
        qty = int(input("Enter the qty of Ice cream"))
        bill5=(qty * i)

    elif op == 6:
        qty = int(input("Enter the qty of Butter Milk"))
        bill6=(qty * 6)
    elif op==7:
        break
    else:
        print("wrong choice")


grandtotal = bill1+bill2+bill3+bill4+bill5+bill6
print("Your  bill  is ", grandtotal )