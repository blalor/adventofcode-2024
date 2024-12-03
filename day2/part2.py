#!/usr/bin/env python

## https://adventofcode.com/2024/day/2

import sys
import lib


def main(fn: str):
    total_reports: int = 0
    safe_reports: int = 0

    with open(fn) as ifp:
        for line in ifp:
            total_reports += 1

            if lib.is_safe_damped(line.strip()):
                safe_reports += 1

    print(f"{safe_reports} safe (damped) reports out of {total_reports} total")


if __name__ == "__main__":
    main(*sys.argv[1:])
