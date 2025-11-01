# password = input("Enter a password: ")
# special_characters = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
# if len(password) <= 8:
#     print("Password must be at least 8 characters long.")
# else:

#     for char in password:
#         if char.isupper():
#             print("")
#         else:
#             print("password should contain upper letter ")
#         pass
#     for char in password:
#         if char.isupper():
#             print("")
#         else:
#             print("password should contain lowercase letter")
#     for char in password:
#         if char in special_characters:
#             print("")
#         else:
#             print("password should contain any special charecter ")
#     for char in password:
#         if char.isdigit():
#             print("")
#         else:
#             print("password should contain a number ")




password = input("Enter a password: ")
special_characters = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
for char in password:
        if char.isupper():
            upper = True
        elif char.islower():
            lower = True
        elif char in special_characters:
            special = True
        elif char.isdigit():
            digit = True

if len(password) >=  8 and upper and lower and special and digit:
     print('password is strong')
else:
     print('password is weak')