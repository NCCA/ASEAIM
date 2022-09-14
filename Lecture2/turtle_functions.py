#!/usr/bin/env python
import turtle


def square(turtle, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)


turtle = turtle.Turtle()

square(turtle, 20, 20, 100, 100)
