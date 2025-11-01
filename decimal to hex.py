a=int(input("enter a decimal value(0 to15)"))
if a >= 16:
    print("enter the number between 0 to 15 only")
else:
    h = hex(a)
    print("the hex value :",h)
