"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    result = get_result(score)
    print(result)

    print("Random Score generator:")
    print(get_random_score())


def get_result(score):
    if 100 >= score >= 90:
        return "Excellent"
    elif 90 > score >= 50:
        return "Passable"
    elif 50 > score >= 0:
        return "Bad"
    else:
        return "Invalid score"


def get_random_score():
    random_score = random.randint(1, 100)
    result = get_result(random_score)
    return "Random result is: " + result


main()
