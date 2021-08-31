def get_email():
    email_dict = {}
    email = input("Enter an email: ")
    while email != "":
        if "@" not in email:
            print("Invalid Email")
        else:
            email_dict[email] = ""
        email = input("Enter an email: ")
    return email_dict


def get_name(email_dict):
    for email in email_dict:
        email_split = email.split("@")
        name = email_split[0]
        try:
            name = name.replace(".", " ")
        except:
            pass
        name = name.title()
        confirm = input(f"Is your name {name}? (Y/N)")
        if confirm.upper() not in ["YES", "Y"]:
            name = input("Name: ")
        email_dict[email] = name
    return email_dict


def print_dict(email_dict):
    for email in email_dict:
        print(f"{email_dict[email]} ({email})")


print_dict((get_name(get_email())))
