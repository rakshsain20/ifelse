num1=int(input("enter the number"))
num2=int(input("enter the number"))
num3=int(input("enter the number"))
if num1> num2 and num3>num2:
    print("smallest",num2)
elif  num2>num1 and num3>num1:
    print("smallest",num1)
else:
    print("smallest",num3)