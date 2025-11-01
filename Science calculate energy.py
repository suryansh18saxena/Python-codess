mass = float(input("Enter the amount of water in kilograms: "))
initial_temp = float(input("Enter the initial temperature: "))
final_temp = float(input("Enter the final temperature: "))
energy = mass * (final_temp - initial_temp) * 4184
print("The energy needed is", energy)
