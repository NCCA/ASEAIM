#!/usr/bin/env python

import os

cwd = os.getcwd()
print(f"Current directory is {cwd}")
try:
    os.mkdir("testdir")
except FileExistsError:
    print("directory testdir already exists")
    pass

os.chdir("testdir")
new_dir = os.getcwd()
print(f"Current directory is {new_dir}")

try:
    os.chdir(cwd)
    os.rmdir(new_dir)
except FileNotFoundError:
    print("can't remove the specified directory")
