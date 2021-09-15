import pytest


def is_capitalized(string: str) -> bool:
    return len(string) == 1 or string[1:].islower() or string.isupper()


@pytest.mark.parametrize(
    ('string', 'is_it'), (
        ('USA', True),
        ('Calvin', True),
        ('compUter', False),
        ('coding', True),
        ('', False),
        ('U', True),
        ('l', True),
        ('Ab', True),
        ('cd', True)
    )
)
def test(string, is_it):
    assert is_capitalized(string) == is_it