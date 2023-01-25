import pytest

from ..a_power import power


@pytest.mark.parametrize(("a", "b", "result"), [(4, 3, 64), (5, 5, 3125), (8, 1, 8)])
def test(a, b, result):
    assert power(a, b) == result
