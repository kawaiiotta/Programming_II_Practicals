# odd numbers 1 to 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# count in 10s
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# count down 20 to 1
for i in reversed(range(1, 21, )):
    print(i, end=' ')
print()

# print stars
stars = int(input("How many stars? "))
for i in range(0, stars):
    print("*", end="")
print()
