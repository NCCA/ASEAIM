#!/usr/bin/env python

from functionStubFile import quadratic_roots

# This will return a complex result
a, b = quadratic_roots(2, 3, 4)
print(f"{a} {b}")
# This will return a complex but with zero j
a, b = quadratic_roots(1, 4, 2)
print(f"{a} {b}")

# This will throw an exception
try:
    a, b = quadratic_roots(0, 4.2, 2)
    print(f"{a} {b}")
except ValueError:
    print("a was zero!")


a, b = quadratic_roots("1", "4", "2")
print(f"{a} {b}")
