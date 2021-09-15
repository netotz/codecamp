import pytest


def is_capitalized(string: str) -> bool:
    return string.islower() or string.isupper() or (
        len(string) > 1 and string[0].isupper() and string[1:].islower()
    )


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