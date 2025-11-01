x = float(input("Enter a point's x-coordinate: "))
y = float(input("Enter a point's y-coordinate: "))
inside = (x >= 0 and x <= 200 and y >= 0 and y <= 100 - (x / 2))
if inside:
  print("The point is in the triangle")
else:
  print("The point is not in the triangle")