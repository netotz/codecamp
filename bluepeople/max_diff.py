from typing import Iterable


def get_max_difference(array: Iterable[int]) -> int:
    return max(array) - min(array)


def test():
    assert get_max_difference( [ 1, 1, 4 ]) == 3
    assert get_max_difference( [ 9, 8 ]) == 1
    assert get_max_difference( [ 6, 22, 16, 29, 23 ]) == 23
    assert get_max_difference( [ 28, 16, 28, 11, 14, 26, 23, 25, 17, 3, 22, 23, 23, 10 ]) == 25