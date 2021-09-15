import pytest


def is_original_position(route: str) -> bool:
    LEFT = 'L'
    RIGHT = 'R'
    DOWN = 'D'
    UP = 'U'

    position = 0
    for move in route:
        if move == RIGHT or move == UP:
            position += 1
        else:
            position -= 1
    return position == 0


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
