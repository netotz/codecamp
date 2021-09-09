import pytest


def reverse_string(string: str) -> str:
    return string[::-1]


@pytest.mark.parametrize(
    'string, reversed', [
        ("Cat", "taC"),
        ("The Daily Byte", "etyB yliaD ehT"),
        ("civic", "civic"),
        ("", "")
    ]
)
def test(string, reversed):
    assert reverse_string(string) == reversed
