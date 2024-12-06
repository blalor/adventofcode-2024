from typing import Iterator


def find_xmasses(source: Iterator[str]) -> tuple[int, int]:
    """return count of 'XMAS' instances in input matrix"""

    total: int = 0

    # tuple of 2D indexes (line, char) relative to a given index in a line
    # these should be named tuples or something
    possible_match_references: tuple[
        tuple[str, tuple[int, int], tuple[int, int], tuple[int, int], tuple[int, int]],
        ...
    ] = (
        ("east",      (0, 0), ( 0,  1), ( 0,  2), ( 0,  3)),
        ("west",      (0, 0), ( 0, -1), ( 0, -2), ( 0, -3)),
        ("south",     (0, 0), ( 1,  0), ( 2,  0), ( 3,  0)),
        ("north",     (0, 0), (-1,  0), (-2,  0), (-3,  0)),

        ("northeast", (0, 0), (-1,  1), (-2,  2), (-3,  3)),
        ("southeast", (0, 0), ( 1,  1), ( 2,  2), ( 3,  3)),
        ("southwest", (0, 0), ( 1, -1), ( 2, -2), ( 3, -3)),
        ("northwest", (0, 0), (-1, -1), (-2, -2), (-3, -3)),
    )

    # buffer of lines read from the source, pre-filled with 4 lines of empty data
    buffer: list[tuple[str, ...]] = [tuple("    ")] * 4

    # pre-fill the buffer. could maybe support having an input with fewer than 4
    # lines, but not necessary now.
    while len(buffer) < 8:
        buffer.append(tuple(next(source).strip("\n")))

    # keep track of the line number (NOT index) of the source
    source_ind: int = 0

    # the index of the line we're referencing. starts at 4 (the first line of
    # the source input), doesn't go beyond the length of the buffer. buffer
    # shouldn't have more than 8 lines total.
    buffer_ind: int = 4
    while buffer_ind < len(buffer):
        source_ind += 1
        # print(f"matching against line {source_ind}: {buffer[buffer_ind]}")

        line_matches = 0
        for char_ind in range(len(buffer[buffer_ind])):
            # find matches relative to the current (buffer_ind, char_ind) position

            for match_ref in possible_match_references:
                # calculate the buffer-absolute index from each relative reference
                ref_name = match_ref[0]
                abs_indices = [ (buffer_ind + x, char_ind + y) for x, y in match_ref[1:] ]

                resolved_match = None
                try:
                    resolved_match = "".join([buffer[x][y] for x, y in abs_indices])
                except IndexError:
                    # buffer or character index is out of range
                    pass

                if resolved_match == "XMAS":
                    print(f"found '{resolved_match}' for {ref_name} at (line, char) ({source_ind}, {char_ind})")

                    total += 1
                    line_matches += 1

        print(f"found {line_matches} matches against line {source_ind} {buffer[buffer_ind]}")

        # read next line from source and append to buffer, popping off the
        # topmost line. if StopIteration is raised, just increment buffer_ind.
        try:
            buffer.append(tuple(next(source).strip("\n")))
            buffer.pop(0)
        except StopIteration:
            buffer_ind += 1

    return total, source_ind
