#!/usr/bin/env python

import csv

with open("csv_data.csv", newline="") as csv_file:
    contents = csv.reader(csv_file)
    for row in contents:
        print(",".join(row))
