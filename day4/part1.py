#!/usr/bin/env python

import lib


with open("input.txt") as ifp:
    total, lines_processed = lib.find_xmasses(ifp)

assert lines_processed == 140
print(f"total: {total}")
