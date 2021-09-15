import pytest


def is_valid(string: str) -> bool:
    '''
    For what I know:
    Time complexity O(n),
    as operations of both dictionary and stack are O(1)
    '''
    parentheses = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    stack = list()
    for char in string:
        if char in parentheses.keys():
            stack.append(char)
        else:
            last_opened = stack.pop()
            if parentheses[last_opened] != char:
                return False
    return True


@pytest.mark.parametrize(
    ('string', 'is_it'), (
        ('()', True),
        ('()[]{}', True),
        ('(]', False),
        ('([)]', False),
        ('{[]}', True),
        ('([[]()]{{}{()}})', True),
        ('([]{{([][](())}[])}})', False)
    )
)
def test(string, is_it):
    assert is_valid(string) == is_it
