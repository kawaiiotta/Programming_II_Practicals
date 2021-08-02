"""
This code will Error check a password
"""
password = str(input("Set new password: "))
while not len(password) > 6:
    print("Password is not long enough")
    password = str(input("Set new password: "))

for char in password:
    print("*", end="")

