#!/usr/bin/env python

import random
import turtle


def colourFunction():
    red = 0
    green = 0
    blue = 0
    while True:
        colour = [red, green, blue]
        red = red + 1
        if red == 255:
            red = 0
            green = green + 1
        if blue == 255:
            green = 0
            blue = blue + 1
        yield colour


colour = colourFunction()
turtle = turtle.Turtle()
turtle.speed(0)
for i in range(0, 100000):
    r, g, b = next(colour)
    print(r, g, b)
    turtle.color(float(r), float(g), float(b))  # note we need float values here
    turtle.goto(random.uniform(-100, 100), random.uniform(-100, 100))
