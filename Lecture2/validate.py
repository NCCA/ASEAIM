#!/usr/bin/env python


def getInt():
    while True:
        try:
            userInput = int(input("please enter an int >"))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return userInput


end = getInt()
for i in range(0, end):
    print(i)
