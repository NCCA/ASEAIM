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
