num=int(input("enter the number"))
if num=="1,2,34,45":
    print("it is a string")
elif num=="1,2,45,67,78":
    print("it is a int")
elif num=="34.9,3.4,12.7":
    print("it is a float")
else:
    print("it is a complex")