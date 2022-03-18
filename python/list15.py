list1=["Apple","Mango","Orange","Grape","Banana","watermelon"]
list2=[]
for x in list1:
    if str(x).find("a")>0:
        list2.append(x)
        
print(list2)
