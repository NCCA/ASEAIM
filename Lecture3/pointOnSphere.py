#!/usr/bin/env python

import argparse
import math
import random


def randomPointOnSphere(radius=1):
    phi = random.uniform(0, 2 * math.pi)
    costheta = random.uniform(-1, 1)
    u = random.uniform(0, 1)
    theta = math.acos(costheta)
    # note we could use np.cbrt to calculate cube root
    cbrt = lambda x: x ** (1.0 / 3.0) if 0 <= x else -((-x) ** (1.0 / 3.0))

    r = radius * cbrt(u)
    x = r * math.sin(theta) * math.cos(phi)
    y = r * math.sin(theta) * math.sin(phi)
    z = r * math.cos(theta)
    return x, y, z


def main(numPoints, filename, radius):
    with open(filename, "w") as file:
        for i in range(0, numPoints):
            x, y, z = randomPointOnSphere(radius)
            file.write(f"{x} {y} {z}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description="generate random points on a sphere")
    parser.add_argument(
        "--num",
        "-n",
        nargs="?",
        const=10,
        default=10,
        type=int,
        help="number of points to generate default 10",
    )
    parser.add_argument(
        "--radius",
        "-r",
        nargs="?",
        const=1.0,
        default=1.0,
        type=float,
        help="radius of sphere default 1.0",
    )
    parser.add_argument("--file", "-f", type=str, required=True)
    args = parser.parse_args()
    main(args.num, args.file, args.radius)
