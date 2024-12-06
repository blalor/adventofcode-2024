#!/usr/bin/env python

import lib


with open("input.txt") as ifp:
    total = lib.process_memory(ifp.read())

print(f"total: {total}")
