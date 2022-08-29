from ..p1294A_coins import can_distribute

import pytest


@pytest.mark.parametrize(
    ("a", "b", "c", "n", "answer"),
    [
        (5, 3, 2, 8, True),
        (100, 101, 102, 105, True),
        (3, 2, 1, 100000000, False),
        (10, 20, 15, 14, False),
        (101, 101, 101, 3, True),
    ],
)
def test(a, b, c, n, answer):
    assert can_distribute(a, b, c, n) == answer
