#!/usr/bin/env python
import sys


def aFunction(argv=None):
    print("in a function")
    print(f"my name is {__name__}")


if __name__ == "__main__":
    sys.exit(aFunction())
