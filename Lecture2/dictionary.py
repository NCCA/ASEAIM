#!/usr/bin/env python

colours = {
    "red": [1, 0, 0],
    "green": [0, 1, 0],
    "blue": [0, 0, 1],
    "white": [1, 1, 1],
    "black": [0, 0, 0],
}

print(colours.get("red"))
print(colours.get("green"))
print(colours.get("purple"))
# can also use
print(colours["white"])
print(colours["purple"])
