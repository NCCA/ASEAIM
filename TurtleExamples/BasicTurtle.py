#!/usr/bin/env python

import turtle

_distance = 10


def quit():
    turtle.bye()


def up():
    turtle.setheading(90)
    turtle.forward(_distance)


def down():
    turtle.setheading(270)
    turtle.forward(_distance)


def left():
    turtle.setheading(180)
    turtle.forward(_distance)


def right():
    turtle.setheading(0)
    turtle.forward(_distance)


def main():

    turtle.listen()
    turtle.onkey(up, "Up")
    turtle.onkey(down, "Down")
    turtle.onkey(left, "Left")
    turtle.onkey(right, "Right")
    turtle.onkey(quit, "Escape")

    turtle.mainloop()


if __name__ == "__main__":
    main()
