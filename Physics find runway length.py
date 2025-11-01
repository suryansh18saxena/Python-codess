v = float(input("Enter the take-off speed (v) in meters/second (m/s): "))
a = float(input("Enter the acceleration (a) in meters/second squared (m/s^2): "))
length = (v ** 2) / (2 * a)
print("The minimum runway length for this airplane is", length, "meters")
