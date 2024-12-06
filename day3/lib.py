import re


def process_memory(input_str: str) -> int:
    total: int = 0

    for m in re.finditer(r"mul\((\d+),(\d+)\)", input_str):
        arg1, arg2 = m.groups()

        total += int(arg1) * int(arg2)

    return total
