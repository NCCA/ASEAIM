#!/usr/bin/env python
import json
from pprint import pprint

with open("data.json", "r") as json_file:
    data = json.load(json_file)
    pprint(data)
    print(f"{data['width']=}")
    print(f"{data['height']=}")
    for values in data["map_contents"]:
        print(f"{values['x_pos']=}")
        print(f"{values['y_pos']=}")
        print(f"{values['value']=}")
        print("-" * 30)
