import pytest

from codeforces.p1409B_min_product import get_min_product


@pytest.mark.parametrize(
    ("a", "b", "x", "y", "n", "prod"),
    [
        (10, 10, 8, 5, 3, 70),
        (12, 8, 8, 7, 2, 77),
        (12343, 43, 4543, 39, 123212, 177177),
        (1000000000, 1000000000, 1, 1, 1, 999999999000000000),
        (1000000000, 1000000000, 1, 1, 1000000000, 999999999),
        (10, 11, 2, 1, 5, 55),
        (10, 11, 9, 1, 10, 10),
    ],
)
def test(a, b, x, y, n, prod):
    assert get_min_product(a, b, x, y, n) == prod
