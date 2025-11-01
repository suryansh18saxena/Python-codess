
# num = int(input("Enter a number: "))

# if num <= 1:
#     print(f"{num} is not a prime number.")
# else:
#     is_prime = True
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break

# if is_prime:
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")

n=int(input())

if n<2:
    print("fd")
    
else:
        is_prime=True

        for i in range(2,n):
            if n%i==0:
                is_prime=False
                break
        if is_prime:
            print("w")
        else:
            print("fd")




# Input range from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print(f"Prime numbers between {start} and {end}:")

for num in range(start, end + 1):
    if num > 1:  # Prime numbers are greater than 1
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
