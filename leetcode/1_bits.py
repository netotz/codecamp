'''
LeetCode 191
'''


import pytest


def count_ones(number: int) -> int:
    '''
    This solution works if number is an actual integer consisting only of
    ones and zeros, not a real binary,
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


def change_last_one(number: int) -> int:
    '''
    Input can be any integer or binary,

    e.g. `5` or `0b101`
    
    Any binary minus one changes the position of the right-most one,

    e.g. `0b100 - 0b1 = 0b011`

    So a bitwise AND removes the last ones,

    e.g. `0b100 & 0b011 = 0b000`,

    just 1 one.
    '''
    ones = 0
    n = number
    while n > 0:
        n &= n - 1
        ones += 1
    return ones


def check_parity(number: int) -> int:
    '''
    Odd integers in their binary form end with a one.
    By shifting the number 1 bit to the right, which is the same as
    dividing it by 2, the last digit is removed.
    '''
    ones = 0
    n = number
    while n > 0:
        if n & 1 == 1:
            ones += 1
        n >>= 1
        # n //= 2
    return ones


@pytest.mark.parametrize(
    'func', (
        change_last_one,
        check_parity
    )
)
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
def test(func, number, ones):
    assert func(number) == ones
