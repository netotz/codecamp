'''
https://leetcode.com/discuss/interview-question/922250/quora-oa-2020-diagonal-arranging
'''


from collections import defaultdict

import pytest


def arrange_diagonals(matrix: list[list[int]]) -> list[int]:
    '''
    Time O(n**2)

    Space O(n**2)
    '''
    n = len(matrix)
    diagonals = defaultdict(list)

    # iterate whole matrix to gather diagonals
    # O(n**2)
    for i in range(n):
        # O(n)
        for j in range(n):
            key = n + j - i
            diagonals[key].append(matrix[i][j])
    
    sorted_diagonals = []
    
    # all diagonals (except main) have length less than n,
    # so they must be cycled
    # O(n**2)
    for key in sorted(diagonals.keys()):
        diagonal_length = len(diagonals[key])
        if diagonal_length < n:
            # O(n)
            cycle = diagonals[key] * (n // diagonal_length)
            # O(n)
            diagonals[key].extend(cycle[:n - diagonal_length])
        
        sorted_diagonals.append((key, diagonals[key]))

    # sort diagonal strings
    # O(n log n)
    sorted_diagonals.sort(key=lambda d: d[1])
    return [sd[0] for sd in sorted_diagonals]


@pytest.mark.parametrize(
    ('matrix', 'output'), [
        (
            [["a", "c", "a", "b", "b"],
             ["c", "b", "a", "c", "b"],
             ["a", "a", "e", "c", "b"],
             ["b", "b", "d", "a", "g"],
             ["a", "b", "e", "b", "a"]],
            [1, 5, 3, 7, 2, 8, 9, 6, 4]
        )
    ]
)
def test(matrix, output):
    assert arrange_diagonals(matrix) == output
