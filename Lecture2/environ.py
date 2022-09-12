#!/usr/bin/env python

import os

for (var, value) in os.environ.items():
    print(f"key {var} : Value {value}")
