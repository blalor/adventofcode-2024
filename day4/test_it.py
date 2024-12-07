import pytest
import textwrap

import io
from lib import find_xmasses


def test_find_xmasses_dots():
    buf = io.StringIO(textwrap.dedent("""
        ..X...
        .SAMX.
        .A..A.
        XMAS.S
        .X....
    """)[1:])

    assert find_xmasses(buf) == (4, 5)


def test_find_xmasses_dots_bigger():
    buf = io.StringIO(textwrap.dedent("""
        ....XXMAS.
        .SAMXMS...
        ...S..A...
        ..A.A.MS.X
        XMASAMX.MM
        X.....XA.A
        S.S.S.S.SS
        .A.A.A.A.A
        ..M.M.M.MM
        .X.X.XMASX
    """)[1:])

    assert find_xmasses(buf) == (18, 10)


# @pytest.mark.xfail
def test_find_xmasses():
    buf = io.StringIO(textwrap.dedent("""
        MMMSXXMASM
        MSAMXMSMSA
        AMXSXMAAMM
        MSAMASMSMX
        XMASAMXAMM
        XXAMMXXAMA
        SMSMSASXSS
        SAXAMASAAA
        MAMMMXMMMM
        MXMXAXMASX
    """)[1:])

    assert find_xmasses(buf) == (18, 10)


@pytest.mark.parametrize(
    "input_buf, expected",
    [
        # no matches
        (
            """
            ....
            ....
            ....
            ....
            """,
            0,
        ),

        # east
        (
            """
            XMAS
            ....
            ....
            ....
            """,
            1,
        ),

        # west
        (
            """
            SAMX
            ....
            ....
            ....
            """,
            1,
        ),

        # south
        (
            """
            X...
            M...
            A...
            S...
            """,
            1,
        ),

        # north
        (
            """
            S...
            A...
            M...
            X...
            """,
            1,
        ),

        # southeast
        (
            """
            X...
            .M..
            ..A.
            ...S
            """,
            1,
        ),

        # southwest
        (
            """
            ...X
            ..M.
            .A..
            S...
            """,
            1,
        ),

        # northwest
        (
            """
            S...
            .A..
            ..M.
            ...X
            """,
            1,
        ),

        # northeast
        (
            """
            ...S
            ..A.
            .M..
            X...
            """,
            1,
        ),
    ]
)
def test_find_one(input_buf: str, expected: int):
    assert find_xmasses(io.StringIO(textwrap.dedent(input_buf)[1:])) == (expected, 4)
