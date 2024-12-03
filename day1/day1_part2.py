#!/usr/bin/env python

## https://adventofcode.com/2024/day/1#part2

import sys


def main(fn: str):
    # text file with two columns
    left_list: list[int] = []
    right_list: list[int] = []

    with open(fn) as ifp:
        for line in ifp:
            # read line, split on whitespace
            val1, val2 = line.strip().split(maxsplit=2)

            # convert to int, add to respective column
            left_list.append(int(val1))
            right_list.append(int(val2))

    # shouldn't get to this point given the maxsplit above
    assert len(left_list) == len(right_list), "lists have different length"

    ## figure out how many times each number in the left list appears in the
    ## right list.

    ## map of list entry to similarity score
    similarity_scores: dict[int, int] = {}

    for left_val in left_list:
        ss = similarity_scores.get(left_val, 0)
        ss += left_val * right_list.count(left_val)

        similarity_scores[left_val] = ss

    total_similarity_score = sum(similarity_scores.values())

    print(f"total_similarity_score: {total_similarity_score}")


if __name__ == "__main__":
    main(*sys.argv[1:])
