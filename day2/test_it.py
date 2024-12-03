import pytest
from lib import is_ordered, is_adjacent_enough, is_safe, is_safe_damped


@pytest.mark.parametrize(
    "input_set, expected", (
        ("7 6 4 2 1", True), # Safe because the levels are all decreasing by 1 or 2.
        ("1 3 6 7 9", True), # Safe because the levels are all increasing by 1, 2, or 3.
        ("1 3 2 4 5", False), # Unsafe because 1 3 is increasing but 3 2 is decreasing.
    )
)
def test_is_ordered(input_set: str, expected: bool):
    assert is_ordered(input_set) is expected


@pytest.mark.parametrize(
    "input_set, expected", (
        ("7 6 4 2 1", True), # Safe because the levels are all decreasing by 1 or 2.
        ("1 3 6 7 9", True), # Safe because the levels are all increasing by 1, 2, or 3.
        ("1 2 7 8 9", False), # Unsafe because 2 7 is an increase of 5.
        ("9 7 6 2 1", False), # Unsafe because 6 2 is a decrease of 4.
        ("8 6 4 4 1", False), # Unsafe because 4 4 is neither an increase or a decrease.
    )
)
def test_adjacency(input_set: str, expected: bool):
    assert is_adjacent_enough(input_set) is expected


@pytest.mark.parametrize(
    "input_set, safe", (
        ("7 6 4 2 1", True), # Safe because the levels are all decreasing by 1 or 2.
        ("1 2 7 8 9", False), # Unsafe because 2 7 is an increase of 5.
        ("9 7 6 2 1", False), # Unsafe because 6 2 is a decrease of 4.
        ("1 3 2 4 5", False), # Unsafe because 1 3 is increasing but 3 2 is decreasing.
        ("8 6 4 4 1", False), # Unsafe because 4 4 is neither an increase or a decrease.
        ("1 3 6 7 9", True), # Safe because the levels are all increasing by 1, 2, or 3.
    )
)
def test_is_safe(input_set: str, safe: bool):
    assert is_safe(input_set) is safe


## part 2
@pytest.mark.parametrize(
    "report, safe", (
        ("7 6 4 2 1", True), # Safe without removing any level.
        ("1 2 7 8 9", False), # Unsafe regardless of which level is removed.
        ("9 7 6 2 1", False), # Unsafe regardless of which level is removed.
        ("1 3 2 4 5", True), # Safe by removing the second level, 3.
        ("8 6 4 4 1", True), # Safe by removing the third level, 4.
        ("1 3 6 7 9", True), # Safe without removing any level.
    )
)
def test_is_safe_damped(report: str, safe: bool):
    assert is_safe_damped(report) is safe
