"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting with the str.format() method
Want to read more about it? https://docs.python.org/3/library/string.html#formatstrings
"""

name = "Gibson L-5 CES"
year = 1922
cost = 16035.4

# 1922 Gibson L-5 CES for about $16,035!
print(f"{year} {name} for about ${cost:>,.0f}!")

# produce the following right-aligned output (do not use a list):
for i in range(0, 151, 50):
    print(f"{i:>3}")
