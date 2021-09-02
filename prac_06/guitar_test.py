"""
CP1404 testing Guitar Class
"""

from guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2015, 1200.54)

print(gibson)
print(another_guitar)
print(gibson.get_age())
print(gibson.is_vintage())

print(another_guitar.get_age())
print(another_guitar.is_vintage())