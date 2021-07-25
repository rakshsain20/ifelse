tax=0
price=int(input("enter the price"))
if price>100000:
    print("tex=100%15")
elif price>50000:
    print("tex=100%10")
else:
    print("tex=100%5")