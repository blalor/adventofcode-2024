from lib import process_memory, process_memory_with_conditionals


def test_mul_from_corrupted():
    input_str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    assert process_memory(input_str) == 161


def test_mul_from_corrupted_with_conditionals():
    input_str = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    # breakpoint()
    assert process_memory_with_conditionals(input_str) == 48
