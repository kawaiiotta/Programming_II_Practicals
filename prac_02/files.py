def write_name():
    name = str(input("What is your name? "))
    with open("name.txt", "w") as name_file:
        name_file.write(name)


def read_name():
    with open("name.txt", "r") as name_file:
        lines = name_file.readlines()
        for name in lines:
            print(f"Your name is {name}")


def save_nums():
    with open("numbers.txt", "w") as numbers_file:
        numbers_file.writelines(["17\n", "42\n", "400"])


def add_nums():
    with open("numbers.txt", "r") as numbers_file:
        numbers = numbers_file.readlines()
        addition = int(numbers[0].strip("\n")) + int(numbers[1].strip("\n"))
        print(addition)

        # Add all numbers together
        total = 0
        for num in numbers:
            total += int(num.strip("\n"))

        print(total)


write_name()
read_name()

save_nums()
add_nums()
