from typing import List, Union

import pytest


def run_bapc(bapc: str, intslist: List[int]) -> Union[List[int], str]:
    R = 'R'
    D = 'D'

    same = 1
    i = 0
    while i < len(bapc):
        current = bapc[i]
        next = bapc[i + 1] if i < len(bapc) - 1 else ''
        if current != next or next == '':
            if current == R:
                if same % 2 == 1:
                    intslist.reverse()
            elif current == D:
                if same > len(intslist):
                    return 'error'
                intslist = intslist[same:]
            same = 1
        else:
            same += 1
        i += 1
    return intslist


@pytest.mark.parametrize(
    ('bapc', 'intslist', 'result'), (
        ('RDD', [1, 2, 3, 4], [2, 1]),
        ('DD', [42], 'error'),
        ('RRD', [1,1,2,3,5,8], [1,2,3,5,8]),
        ('D', [], 'error'),
        ('DRRRRRD', [4, 8, 10], [8])
    )
)
def test(bapc, intslist, result):
    assert run_bapc(bapc, intslist) == result
