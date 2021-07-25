atm=input("enter the atm")
print("welcome atm")
card=input("enter the card") 
if "card==dabit card":
    print("transfar in inporcess")
    language=input("enter the language")
    if language=="english":
        print("inprocess")
        pin=int(input("enter the number"))
        if pin==1234:
            print("inprocess")
            account=input("enter the account")
            if account=="saving account" and account=="current account":
                print("inprocess")
                amount=int(input("enter the amount"))
                if amount<7000:
                    print("3000 amount is tarnsfar")
                    print("balance correct")
                    respect=input("do you to take respect")
                    if respect=="yes":
                        print("take  the respcet")
                        print("tanku")
                    else:
                        print("ok good luck")
                        print("tanku you for banking with us")
                else:
                    print("please enter the correct amount")
            else:
                print("please corrcet account")
        else:
            print("try again pin")
    else:
        print("your lanuage is correct")
else:
    print("insert card")

