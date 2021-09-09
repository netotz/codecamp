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


@pytest.mark.parametrize(
    'nums, target, indexes', [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, 2, -3, -5, 6, -7], -10, [2, 5]),
        ([0, 0], 0, [0, 1])
    ]
)
def test(nums, target, indexes):
    assert two_sum(nums, target) == indexes