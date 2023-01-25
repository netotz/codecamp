import pytest

from ..alichos import was_accident


@pytest.mark.parametrize(
    ("n", "array", "answer"),
    [
        (2, [1, 2], True),
        (3, [3, 2, 1], True),
        (4, [4, 3, 2, 1], False),
    ],
)
def test(n, array, answer):
    assert was_accident(n, array) == answer
