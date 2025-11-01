a = int(input("Enter today's day: "))
d = int(input("Enter the number of days elapsed since today: "))
f = (a + d) % 7
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print("Today is", days[a], "and the future day is", days[f])
