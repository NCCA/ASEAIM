#!/usr/bin/env python
import sys


def main(argv=None):
    if argv is None:
        argv = sys.argv
    for index, args in enumerate(argv):
        print(f"{index} : {args}")


if __name__ == "__main__":
    sys.exit(main())
