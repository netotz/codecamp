'''
Minimizing Permutations
In this problem, you are given an integer N, and a permutation, P of the integers from 1 to N, denoted as (a_1, a_2, ..., a_N). You want to rearrange the elements of the permutation into increasing order, repeatedly making the following operation:
Select a sub-portion of the permutation, (a_i, ..., a_j), and reverse its order.
Your goal is to compute the minimum number of such operations required to return the permutation to increasing order.

Signature
int minOperations(int[] arr)

Input
Array arr is a permutation of all integers from 1 to N, N is between 1 and 8

Output
An integer denoting the minimum number of operations required to arrange the permutation in increasing order

Example
If N = 3, and P = (3, 1, 2), we can do the following operations:
Select (1, 2) and reverse it: P = (3, 2, 1).
Select (3, 2, 1) and reverse it: P = (1, 2, 3).
output = 2
'''


from collections import deque

import pytest


def minOperations(arr: list[int]) -> int:
    '''
    Use a tree where the root is `arr` and its children are its permutations
    which will have their permutations as their children, and so on.
    Do BFS to find the shortest path to the target.

    Time O(n!)

    Space O(n!)
    '''
    target = tuple(range(1, len(arr) + 1))
    
    current_level = deque([tuple(arr)])
    next_level = deque()
    
    visiteds = {tuple(arr)}
    
    level = 0
    # O(n!)
    while len(current_level) > 0:
        permutation = current_level.popleft()
        
        if permutation == target:
            return level
        
        # O(n**2)
        for i in range(len(permutation)):
            for j in range(i + 1, len(permutation)):
                flipped = permutation[:i] + permutation[i:j + 1][::-1] + permutation[j + 1:]
                
                if flipped not in visiteds:
                    visiteds.add(flipped)
                    next_level.append(flipped)
    
        if len(current_level) == 0:
            current_level = next_level
            print(len(next_level))
            next_level = deque()
            
            level += 1
    
    return -1


@pytest.mark.parametrize(
    ('arr', 'operations'), [
        ([3, 1, 2], 2),
        ([1, 2, 5, 4, 3], 1),
        ([8, 7, 6, 4, 5, 1, 2, 3], 3)
    ]
)
def test(arr, operations):
    assert minOperations(arr) == operations
