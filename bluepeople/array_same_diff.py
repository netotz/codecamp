from functools import reduce
from typing import Sequence, Union


def is_same_difference(array: Sequence[Union[int, float]]) -> bool:
    return reduce(
        lambda a, b: a if a == b else None,
        (float(f'{abs(x - y):g}') for x, y in zip(array[:-1], array[1:]))
    ) is not None


def test():
    assert is_same_difference([ 1, 3, 5 ])
    assert not is_same_difference([ 194, 54, 23, 7, 3, 6, 8 ])
    assert is_same_difference([44, 37, 30, 23 ])
    assert is_same_difference([ -2.3, -1.1, 0.1, 1.3, 2.5, 3.7 ])
    assert is_same_difference([ 1, 8 ])
    assert is_same_difference([ 3, 2, 1, 2, 3, 4, 3])
