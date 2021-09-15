from typing import List, Union
from collections import deque

import pytest


def run_bapc(bapc: str, intslist: List[int]) -> Union[List[int], str]:
    R = 'R'
    D = 'D'

    newlist = list(intslist)
    same = 1
    i = 0
    while i < len(bapc):
        current = bapc[i]
        next = bapc[i + 1] if i < len(bapc) - 1 else ''
        if current != next or next == '':
            if current == R:
                if same % 2 == 1:
                    newlist.reverse()
            elif current == D:
                if same > len(newlist):
                    return 'error'
                newlist = newlist[same:]
            same = 1
        else:
            same += 1
        i += 1
    return newlist


def run_bapc_deque(bapc: str, intslist: List[int]) -> Union[List[int], str]:
    R = 'R'
    D = 'D'

    deq = deque(intslist)
    pophead = True
    for func in bapc:
        if func == R:
            pophead = not pophead
        else:
            if not deq:
                return 'error'
            if pophead:
                deq.popleft()
            else:
                deq.pop()
    if not pophead:
        deq.reverse()
    return list(deq)


@pytest.mark.parametrize(
    'func', (
        run_bapc,
        run_bapc_deque
    )
)
@pytest.mark.parametrize(
    ('bapc', 'intslist', 'result'), (
        ('RDD', [1, 2, 3, 4], [2, 1]),
        ('DD', [42], 'error'),
        ('RRD', [1, 1, 2, 3, 5, 8], [1, 2, 3, 5, 8]),
        ('D', [], 'error'),
        ('DRRRRRD', [4, 8, 9, 10], [9, 8]),
        ('RDRD', [1, 2, 3, 4, 5], [2, 3, 4]),
        ('DDRDRDRRD', [2, 3, 5, 7, 11, 13, 17, 23], [11, 13, 17])
    )
)
def test(func, bapc, intslist, result):
    assert func(bapc, intslist) == result
