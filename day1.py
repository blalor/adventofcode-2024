#!/usr/bin/env python

## https://adventofcode.com/2024/day/1

import sys


def main(fn: str):
    # text file with two columns
    col1: list[int] = []
    col2: list[int] = []

    with open(fn) as ifp:
        for line in ifp:
            # read line, split on whitespace
            val1, val2 = line.strip().split(maxsplit=2)

            # convert to int, add to respective column
            col1.append(int(val1))
            col2.append(int(val2))

    # shouldn't get to this point given the maxsplit above
    assert len(col1) == len(col2), "columns have different length"

    # sort lists of numbers in ascending order
    col1.sort()
    col2.sort()

    total_distance = 0
    for val1, val2 in zip(col1, col2):
        total_distance += abs(val1 - val2)

    print(f"total distance: {total_distance}")


if __name__ == "__main__":
    main(*sys.argv[1:])
