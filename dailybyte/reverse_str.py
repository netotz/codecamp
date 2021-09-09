import pytest


def reverse_string(string: str) -> str:
    return string[::-1]


@pytest.mark.parametrize(
    'string, reversed', [
        ("Cat", "taC"),
        ("The Daily Byte", "etyB yliaD ehT"),
        ("civic", "civic"),
        ("", ""),
        ("\x18\u8000", "\u8000\x18")
    ]
)
def test(string, reversed):
    assert reverse_string(string) == reversed
