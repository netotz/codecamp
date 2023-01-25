import pytest
from ..c_cash import count_keystrokes


@pytest.mark.parametrize(
    ("target", "answer"),
    [
        ("40004", 4),
        ("1355506027", 10),
        ("10888869450418352160768000001", 27),
        ("100", 2),
        ("1000", 3),
        ("10000", 3),
    ],
)
def test(target, answer):
    assert count_keystrokes(target) == answer
