#!/usr/bin/env python
import random
import turtle

from LSystem import *

# F -> Forward
# X -> A place holder for movements
# [ push position and direction onto stack
# ] pop position and direction back to turtle
# + Turn Left
# - Turn Right

axiom = "X"  # start
rules = {"X": "F+[[X]-X]-F[-FX]+X", "F": "FF"}  # fern
iterations = 4  # lower is quicker
lenght = 10  # lower this if more iterations
angle = 25  # change this to make different shapes


g = generatRuleString(axiom, rules, iterations)
print(g[-1])

turtle = turtle.Turtle()
turtle.speed(100)
turtle.penup()
turtle.goto(0, -200)
turtle.left(90)

turtle.color(0.0, 128.0, 0.0)
drawLSystem(turtle, g[-1], 10, 25)
