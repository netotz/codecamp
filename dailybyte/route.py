import pytest


def is_original_position(route: str) -> bool:
    LEFT = 'L'
    RIGHT = 'R'
    DOWN = 'D'
    UP = 'U'

    vertical = 0
    horizontal = 0
    for move in route:
        if move == LEFT:
            horizontal -= 1
        elif move == RIGHT:
            horizontal += 1
        elif move == DOWN:
            vertical -= 1
        else:
            vertical += 1
    return vertical == horizontal == 0


@pytest.mark.parametrize(
    ('route', 'is_it'), (
        ('LR', True),
        ('URURD', False),
        ('RUULLDRD', True),
        ('', True)
    )
)
def test(route, is_it):
    assert is_original_position(route) == is_it
