from lib import process_memory


def test_mul_from_corrupted():
    input_str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    assert process_memory(input_str) == 161
