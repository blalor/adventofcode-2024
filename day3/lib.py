import re


def process_memory(input_str: str) -> int:
    total: int = 0

    for m in re.finditer(r"mul\((\d+),(\d+)\)", input_str):
        arg1, arg2 = m.groups()

        total += int(arg1) * int(arg2)

    return total


def process_memory_with_conditionals(input_str: str) -> int:
    is_enabled: bool = True
    total: int = 0

    for m in re.finditer(r"(?P<mul>mul\((?P<arg1>\d+),(?P<arg2>\d+)\))|(?P<do>do\(\))|(?P<dont>don't\(\))", input_str):
        if m["dont"] is not None:
            is_enabled = False
        elif m["do"] is not None:
            is_enabled = True
        elif is_enabled:
            total += int(m["arg1"]) * int(m["arg2"])

    return total
