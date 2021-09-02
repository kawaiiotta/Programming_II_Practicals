"""
CP1404 Using Guitar Class
"""

from guitar import Guitar


def main():
    print("My guitars!")
    guitar_list = get_guitars()
    print(" ... snip ... ")
    print_guitars(guitar_list)


def get_guitars():
    guitar_list = []
    while True:
        guitar_name = str(input("Name: "))
        if guitar_name == "":
            break

        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: "))

        print(f"{guitar_name} ({guitar_year}) : ${guitar_cost:.2f} added")
        guitar_list.append(Guitar(guitar_name, guitar_year, guitar_cost))

    return guitar_list


def print_guitars(guitar_list):
    for i, guitar in enumerate(guitar_list):

        vintage_string = "(vintage)" if guitar.is_vintage() else ""

        print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}),"
              f" worth ${guitar.cost:10,.2f}{vintage_string}")


main()
