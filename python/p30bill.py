print("Press pi For Pizza")
print("Press r For Vge. Roll")
print("Press f For fix pack lunch")
print("Press b For brownie cake")
print("Press i For Ice Cream")
print("Press bmilk for Butter Milk")
pi=200
r=170
f=100
b=90
i=70
bm=20
op = input("Enter your Choice").lower()
total=pi+r+f+b+i+bm
if op=="pi":
    qty= int(input("Enter the qty of Pizza"))
    bill=qty*pi
    print("Your  bill  of Pizza ",bill)
elif op=="r":
    qty = int(input("Enter the qty of Vge.ROll"))
    bill = qty * r
    print("Your  bill  of Vge.ROll ", bill)
elif op=="f":
    qty = int(input("Enter the qty of fix lunch"))
    bill = qty * f
    print("Your  bill  of FIx Lunch ",bill)
elif op=="b":
    qty = int(input("Enter the qty of Brownie"))
    bill = qty * b
    print("Your  bill  of Brownie ",bill)
elif op=="i":
    qty = int(input("Enter the qty of Ice cream"))
    bill = qty * i
    print("Your  bill  of Ice cream ",bill)
elif op == "bmilk":
    qty = int(input("Enter the qty of Butter Milk"))
    bill = qty * bm
    print("Your  bill  of Butter Milk ",bill)
elif op == "all":
    qty = int(input("Enter the qty of Pizza"))


    qty = int(input("Enter the qty of fix lunch"))

    qty = int(input("Enter the qty of Vge.ROll"))


    qty = int(input("Enter the qty of Ice cream"))


    qty = int(input("Enter the qty of Butter Milk"))

    bill = (qty * pi) + (qty * f) + (qty * i) + (qty * bm) + (qty * r)
    print("Your Bill is", bill)