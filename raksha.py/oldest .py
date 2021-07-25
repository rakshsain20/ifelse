age=input("enter the number")
age1= input("enter the number")
age2=input("enter the number")
if age>age1 and age>age2:
    print("first is oldest")
elif age1>age and age1>age2:
    print("second is oldest")
elif age2>age and age2>age1:
    print("third is oldest")
else:
    print("equal")
