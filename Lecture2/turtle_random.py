#!/usr/bin/env python
import turtle
import turtle
import random
from Square import square


def randomColour() :
  return (random.uniform(0,255),
          random.uniform(0,255),
          random.uniform(0,255))

turtle=turtle.Turtle()
turtle.speed(1500)

for i in range(0,200) :
  x=random.uniform(-200,200)
  y=random.uniform(-200,200)
  width = random.uniform(50,300)
  height = random.uniform(50,300)
  
  square(turtle,x,y,width,height,randomColour(),randomColour())