"""
Cp1404 Languages
"""

from programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(ruby)
print(python)
print(visual_basic)

language_list = [ruby, python, visual_basic]
print("the dynamically typed languages are:")

for lang in language_list:
    if lang.is_dynamic():
        print(lang.name)
