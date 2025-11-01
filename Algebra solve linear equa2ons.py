a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))
d = float(input("Enter value of d: "))
e = float(input("Enter value of e: "))
f = float(input("Enter value of f: "))
O = (a * d) - (b * c)
if O == 0:
  print("The equation has no solution.")
else:
  x = ((e * d) - (b * f)) /O
  y = ((a * f) - (e * c)) /O
  print("x is", x, "and y is", y)
