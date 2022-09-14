#!/usr/bin/env python

a = 10
b = 0
try:
    print("Doing Division {}".format(a / b))
except ZeroDivisionError:
    print("Cant divide by zero")

print("no do something else")
