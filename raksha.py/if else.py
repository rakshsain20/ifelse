time=float(input("enter the time table"))
if time>=6.00 and time<7.00:
    print("morning exercise") 
elif time>=8.00 and time<9.00:
    print("break fast")
elif time>=9.00 and time<10.00:
    print("english activity")
elif time>=10.00 and time<13.00:
    print("coding")
elif time>=13.00 and time<2.00:
    print("lunch")
elif time>=2.00 and time<17.00:
    print("self study")
elif time>=17.00 and time<19.00:
    print("cultural activity")
elif time>=19.00 and time<20.00:
    print("coding time")
elif time>=20.00 and time<21.00:
    print("learning circle")
else:
    print("dinner")

