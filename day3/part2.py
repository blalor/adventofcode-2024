#!/usr/bin/env python

import lib


with open("input.txt") as ifp:
    total = lib.process_memory_with_conditionals(ifp.read())

print(f"total: {total}")
