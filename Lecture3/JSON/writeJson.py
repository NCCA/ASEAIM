#!/usr/bin/env python
import json
import random

json_data = dict()  # create a dictionary
json_data["width"] = 200
json_data["height"] = 200
map_data = list()
for i in range(100):
    x_pos = random.randint(0, 100)
    y_pos = random.randint(0, 100)
    value = random.uniform(0.0, 20.0)
    map_data.append({"x_pos": x_pos, "y_pos": y_pos, "value": value})

json_data["map_contents"] = map_data

json_object = json.dumps(json_data, indent=4)
# Writing to sample.json
with open("map_data.json", "w") as json_file:
    json_file.write(json_object)
