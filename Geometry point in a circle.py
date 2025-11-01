x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))
distance = ((x**2 + y**2))**0.5
if distance <= 10:
    print("Point" ,({x}, {y}), "is in the circle")
else:
    print("Point" ,({x}, {y}), "is not in the circle")
