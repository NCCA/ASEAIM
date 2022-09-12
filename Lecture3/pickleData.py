#!/usr/bin/env python
import pickle
import random

a = random.sample(range(100), 20)
print(a)

with open("test.pickle", "wb") as file:
    pickle.dump(a, file, protocol=pickle.HIGHEST_PROTOCOL)

with open("test.pickle", "rb") as file:
    b = pickle.load(file)
print(b)
print(a == b)
