#!/usr/bin/env python
code = [
    "a = 10 / 0",
    'int("hello")',
    'colours = {"red": [1, 0, 0]}',
    'colours["purple"]',
    '"2" + 2',
]

for line in code:
    try:
        exec(line)
    except Exception as e:
        print(f"exception thrown : {e.__class__.__name__} {e.args}")
