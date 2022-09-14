#!/usr/bin/env python

import cmath


# Note float type hint will also support int as a number
def quadratic_roots(a, b, c):
    """calculate the quadratic roots of a, b, and c are coefficient and real numbers and also a ≠ 0.
    If a is equal to 0 that equation is not valid quadratic equation.

    Parameters
    ----------
    a : number
    b : number
    c : number

    Returns
    -------
        first : number
        second : number
    Raises
    ------
        ValueError if a == 0
    """
    if a == 0:
        raise ValueError

    discriminant = (b**2) - (4 * a * c)

    first = (-b - cmath.sqrt(discriminant)) / (2 * a)
    second = (-b + cmath.sqrt(discriminant)) / (2 * a)
    return first, second


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
