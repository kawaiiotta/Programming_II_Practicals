"""
This code will Error check a password
"""


def main():
    password = get_password()
    print_asterix(password)


def get_password():
    password = str(input("Set new password: "))
    while not len(password) > 6:
        print("Password is not long enough")
        password = str(input("Set new password: "))
    return password


def print_asterix(password):
    for char in password:
        print("*", end="")


main()
