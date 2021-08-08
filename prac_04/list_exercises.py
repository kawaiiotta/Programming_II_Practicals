numbers = []
for i in range(0, 5):
    number = float(input("Give a number: "))
    numbers.append(number)

print(f"Max: {max(numbers)}")
print(f"Min: {min(numbers)}")
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"Average: {sum(numbers)/len(numbers)}")


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = str(input("Your username: "))
if username in usernames:
    print("Access granted")
