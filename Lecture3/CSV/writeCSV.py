#!/usr/bin/env python
import csv
import random

header = ["x_pos", "y_pos", "size"]
with open("csv_data.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header)
    for i in range(100):
        x_pos = random.randint(0, 200)
        y_pos = random.randint(0, 200)
        size = random.randint(0, 10)
        csv_writer.writerow([x_pos, y_pos, size])
