from typing import List

import pytest


def two_sum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        n = nums[0]
        nums.pop(0)
        if (dif := target - n) in nums:
            i_dif = nums.index(dif) + i + 1
            if i != i_dif:
                return [i, i_dif]


def two_sum_reverse(nums: List[int], target: int) -> List[int]:
    '''
    `.pop()` now takes O(1) and there's no need to use `in` operator,
    but I don't like how the try block looks
    '''
    i = len(nums) - 1
    while i >= 0:
        n = nums[-1]
        nums.pop()
        try:
            i_dif = nums.index(target - n)
            if i != i_dif:
                return [i_dif, i]
        except ValueError:
            pass
        i -= 1


def with_buffer(nums: List[int], target: int) -> List[int]:
    past = {}
    for i, num in enumerate(nums):
        if (dif := target - num) in past:
            return [past[dif], i]
        past[num] = i


@pytest.mark.parametrize(
    'func', [
        two_sum,
        two_sum_reverse,
        with_buffer
    ]
)
@pytest.mark.parametrize(
    ('nums', 'target', 'indexes'), (
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, 2, -3, -5, 6, -7], -10, [2, 5]),
        ([0, 0], 0, [0, 1])
    )
)
def test(func, nums, target, indexes):
    assert func(nums, target) == indexes