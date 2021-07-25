
wight=float(input("enter the wight in m"))
height=float(input("enter the hight in kg"))
bmi=height**2/wight
if  bmi <18:
    print("severely underwight")
elif bmi >=18 and bmi<20.5:
    print("underwight")
elif bmi>16 and bmi <30:
    print("healthy")
elif bmi >5 and bmi<30:
    print("severely underheiht")
elif bmi>=30:
    print("over hight")
