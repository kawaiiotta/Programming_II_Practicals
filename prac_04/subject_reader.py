"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    data = get_data()
    print_data(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    lines = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        lines.append(parts)
    input_file.close()
    return lines


def print_data(data):
    for line in data:
        course = line[0]
        name = line[1]
        amount_of_stud = line[2]
        print(f"{course} is taught by {name} and has {amount_of_stud} students.")

main()
