#!/usr/bin/env python

import os
import sys


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]  # skip first arg

    for name in argv:
        with open(name) as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                print(f"{i:04d}: {line}", end="")
        print("-" * 80)


if __name__ == "__main__":
    sys.exit(main())
