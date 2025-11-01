import random

options = ["scissors", "rock", "paper"]

print("Choose 0 for scissors")
print("Choose 1 for rock")
print("Choose 2 for paper")

user_choice = int(input("Enter the number between 0-2 only: "))
computer_choice = random.randint(0, 2)

print("Computer chose", options[computer_choice])
print("You chose",options[user_choice])

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice + 1) % 3 == computer_choice:
    print("Computer wins the game!")
else:
    print("You win the game!")
