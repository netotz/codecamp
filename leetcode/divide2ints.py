'''
LeetCode 29
'''

import pytest


def divide(dividend: int, divisor: int) -> int:
    '''
    Substract the divisor, doubling it each step for large numbers.
    '''
    INT_MIN = -2 ** 31
    INT_MAX = 2 ** 31 - 1
    # edge case, result overflows INT_MAX by 1
    if dividend == INT_MIN and divisor == -1:
        return INT_MAX
    
    isNegative = (dividend < 0) != (divisor < 0)
    dividend = abs(dividend)
    divisor = doubled = abs(divisor)
    quotient = 0
    times = 1
    if divisor == 1:
        quotient = dividend
        dividend = 0
    while dividend >= divisor:
        dividend -= doubled
        quotient += times
        times += times
        doubled += doubled
        if dividend < doubled:
            times = 1
            doubled = divisor
    return -quotient if isNegative else quotient


@pytest.mark.parametrize(
    ('dividend', 'divisor', 'quotient'), (
        (10, 3, 3),
        (7, -3, -2),
        (0, 1, 0),
        (1, 1, 1),
        (-6, 2, -3),
        (2, 5, 0),
        (20, 1, 20),
        (-2147483648, -1, 2147483647),
    )
)
def test(dividend, divisor, quotient):
    assert divide(dividend, divisor) == quotient
