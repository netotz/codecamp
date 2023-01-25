import pytest
from ..d_scope import can_complete


@pytest.mark.parametrize(
    ("string", "answer"),
    [
        ("((a)ba)", True),
        ("(a(ba))", False),
        ("(((())))", True),
        ("abca", False),
    ],
)
def test(string, answer):
    assert can_complete(string) == answer
