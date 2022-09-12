#!/usr/bin/env python
import sys

import aFunction


def main(argv=None):
    print("in main function")
    print(f"{__name__}")
    aFunction.aFunction()


if __name__ == "__main__":
    sys.exit(main())
