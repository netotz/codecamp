from collections import deque

import pytest


def get_beiju(string: str) -> str:
    HOME = '['
    END = ']'
    string += END

    i = 0
    homeindex = -1
    beiju = deque()
    while i < len(string):
        char = string[i]
        if char == HOME or char == END:
            if homeindex >= 0:
                beiju.rotate(i - homeindex - 1)
                homeindex = -1
            else:
                homeindex = i
            if char == HOME:
                homeindex = i
        else:
            beiju.append(char)
        i += 1
    return ''.join(beiju)


@pytest.mark.parametrize(
    ('string', 'beiju'), (
        ('This_is_a_[Beiju]_text', 'BeijuThis_is_a__text'),
        ('[[]][][]Happy_Birthday_to_Tsinghua_University', 'Happy_Birthday_to_Tsinghua_University'),
        ('Plain_text', 'Plain_text'),
        ('', ''),
        ('Go_[to_[head', 'headto_Go_'),
        ('Go_[to_[head_]then_to_tail_[back_to_head', 'back_to_headhead_to_Go_then_to_tail_')
    )
)
def test(string, beiju):
    assert get_beiju(string) == beiju
