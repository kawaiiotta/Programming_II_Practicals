"""
CP1404 Programming Language
"""

class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, " \
               f"Reflection={self.reflection}, " \
               f"First appeared in {self.year}"

