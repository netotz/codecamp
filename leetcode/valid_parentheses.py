import pytest


def is_valid(string: str) -> bool:
    '''
    For what I know:
    Time complexity O(n) worst case,
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
            # push last opened
            stack.append(char)
        else:
            # if there's no opened or
            # first closed doesn't match with last opened
            if not stack or parentheses[stack.pop()] != char:
                return False
    return not stack


@pytest.mark.parametrize(
    ('string', 'is_it'), (
        ('[', False),
        ('{{{', False),
        (')', False),
        (']]]', False),
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
