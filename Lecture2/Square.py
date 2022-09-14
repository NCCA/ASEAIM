import turtle
from typing import Tuple


def square(
    turtle: object,
    x: int,
    y: int,
    width: int,
    height: int,
    colour: Tuple = (0, 0, 0),
    fillColour: Tuple = (0, 0, 0),
    fill: bool = True,
):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pencolor(colour)
    turtle.fillcolor(fillColour)
    if fill == True:
        turtle.begin_fill()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    if fill == True:
        turtle.end_fill()
