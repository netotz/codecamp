import pytest


def correct(string: str) -> str:
    stack = list()
    i = 0
    while i < len(string):
        char = string[i]
        if char == '<':
            if stack:
                stack.pop()
        else:
            stack.append(char)
        i += 1
    return ''.join(stack)


@pytest.mark.parametrize(
    ('string', 'corrected'), (
        ('a<bc<', 'b'),
        ('foss<<rritun', 'forritun'),
        ('a<a<a<aa<<', '')
    )
)
def test(string, corrected):
    assert correct(string) == corrected
