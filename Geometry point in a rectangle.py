x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))
h = (x)
v = (y)
hw = 10 / 2
hh = 5 / 2
if h <= hw and v <= hh:
    print((x,y),"The point is inside the rectangle.")
else:
    print((x,y),"The point is outside the rectangle.")
