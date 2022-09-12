#!/usr/bin/env python
import argparse


def main(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            numbers = line.split(" ")
            print(numbers)
            if len(numbers) == 3:
                try:
                    x = float(numbers[0])
                    y = float(numbers[1])
                    z = float(numbers[2])
                    print(f"{x} {y} {z}")

                except ValueError:
                    print("unable to convert value to float")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description="parse points file")

    parser.add_argument("--file", "-f", type=str, required=True)
    args = parser.parse_args()
    main(args.file)
