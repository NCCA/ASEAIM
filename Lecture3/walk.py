#!/usr/bin/env python

import os

for root, dirs, files in os.walk(".", topdown=True):
    print(f"Root :{root}\n\tDirectories : {dirs}\n\tFiles {files}")
