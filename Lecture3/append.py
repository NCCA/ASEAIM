#!/usr/bin/env python
import os
import sys

print(sys.path)
sys.path.append(os.getenv("HOME") + "/scripts")

print(sys.path)
