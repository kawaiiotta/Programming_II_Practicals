numbers = [3, 1, 4, 1, 5, 9, 2]
""" 3, 
    2, 
    4, 
    [3, 1, 4, 1, 5, 9], 
    [1], 
    True, 
    False, 
    False, 
    [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
"""
numbers[0] = "ten"
numbers[-1] = 1
slice = numbers[2:]
print(numbers)
print(slice)
print(9 in numbers)