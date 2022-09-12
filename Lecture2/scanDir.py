#!/usr/bin/env python

import os

with os.scandir(".") as it:
    for entry in it:
        if not entry.name.startswith(".") and entry.is_file():
            print(f"Name {entry.name} path {entry.path} \nStat : {entry.stat()}")
