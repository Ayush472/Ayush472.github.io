age=int(input("Enter your age"))
Gender  = input("enter your Gender")
maritalstatus = input("Enter your marital status M & U")

if Gender== "F":
    print("She will work only ubrn areas.")
elif Gender == "M" and age >= 20 and age <=40:
    print("He will work in anywhere")
elif Gender == "M" and age >= 41 and age <=60:
    print("He will work in urban areas only.")
else:
    print("Error")