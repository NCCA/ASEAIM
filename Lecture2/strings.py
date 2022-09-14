#!/usr/bin/env python

hello = "hello world"
print(hello)

text = 'We can use single "quotes"'

print(text)

text = """Triple single or double quotes
can be used for longer strings. These will
Be
printed
verbatum"""

print(text)

print(
    "Unicode strings start with u but not all terminals can print these chars \U0001D6D1 "
)
print("Omega:  Ω")


str = "Hello python"

# Prints complete string
print(str)
# Prints first character of the string
print(str[0])
# Prints characters starting from 3rd to 6th
print(str[2:5])
# Prints string starting from 3rd character
print(str[2:])
# Prints string two times
print(str * 2)
# Prints concatenated string
print(str + " with added text")
