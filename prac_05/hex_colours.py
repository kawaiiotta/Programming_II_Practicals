"""
CP1404/CP5632 Practical
Hex Colour picker / namer
"""

HEX_COLOURS = {"White": "#ffffff",
               "Black": "#000000",
               "Beige": "#f5f5dc",
               "BlanchedAlmond": "#ffebcd",
               "Burlywood": "#def887",
               "CadetBlue3": "#7ac5cd",
               "chocolate3": "#cd661d",
               "cyan2": "#00eeee",
               "DarkGoldenrod3": "#cd950c"}

colour_name = input("Enter colour name: ")
while colour_name != "":
    if colour_name in HEX_COLOURS:
        print(colour_name, "is", HEX_COLOURS[colour_name])
        break
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ")