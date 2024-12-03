def is_ordered(input_set: str) -> bool:
    input_ints = [int(x) for x in input_set.split()]

    return sorted(input_ints) == input_ints or sorted(input_ints, reverse=True) == input_ints


def is_adjacent_enough(input_set: str, how_close: int = 1, how_far: int = 3) -> bool:
    input_ints = [int(x) for x in input_set.split()]

    for ind in range(1, len(input_ints)):
        prev = input_ints[ind-1]
        cur = input_ints[ind]

        if not (how_close <= abs(prev-cur) <= how_far):
            return False

    return True


def is_safe(input_set: str) -> bool:
    return is_ordered(input_set) and is_adjacent_enough(input_set)


def is_safe_damped(report: str) -> bool:
    if is_safe(report):
        # print(f"'{report}' is safe as-is")
        return True

    # print(f"'{report}' is UNSAFE; iterating")
    report_ints = [int(x) for x in report.split()]

    for ind in range(len(report_ints)):
        dupe = report_ints[:]
        dupe.pop(ind)

        # print(f"checking '{dupe}'…", end=None)
        if is_safe(" ".join([str(i) for i in dupe])):
            # print("yep!")
            return True
        else:
            # print("nope")
            pass

    # print(f"Cannot damp '{report}'")
    return False
