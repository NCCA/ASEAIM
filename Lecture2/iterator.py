#!/usr/bin/env python

fruit = ("apple", "banana", "cherry")
fruit_it = iter(fruit)

print(next(fruit_it))
print(next(fruit_it))
print(next(fruit_it))

try:
    print(next(fruit_it))
except:
    print("none left")
