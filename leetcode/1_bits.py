import pytest


def count_ones(number: int) -> int:
    '''
    This solution works if number is an actual integer
    consisting only of ones and zeros, not a real binary,
    e.g. 101, not 0b101,
    but that's not the input of the problem
    '''
    ones = 0
    n = number
    while n > 0:
        last_digit = n % 10
        if last_digit == 1:
            ones += 1
        n //= 10
    return ones


def get_hamming_weight(number: int) -> int:
    '''
    Input can be any integer or binary,
    e.g. 5 or 0b101
    '''
    ones = 0
    n = number
    while n > 0:
        n &= n - 1
        ones += 1
    return ones


@pytest.mark.parametrize(
    ('number', 'ones'), (
        (0b101, 2),
        (0b11011, 4),
        (0b0, 0),
        (0b1, 1),
        (0b00000000000000000000000000001011, 3),
        (0b00000000000000000000000010000000, 1),
        (0b11111111111111111111111111111101, 31)
    )
)
def test(number, ones):
    assert get_hamming_weight(number) == ones
