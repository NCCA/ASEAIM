#!/usr/bin/env python

data = (123, "hello", 2.45, 3 + 2j)
moreData = (" ", "world")

print(data)
print(data[1])
print(data[2:])

hello = data[1] + moreData[0] + moreData[1]
print(hello)
data[0] = 3
