'''
Pair Sums
Given a list of n integers arr[0..(n-1)], determine the number of different pairs of elements within it which sum to k.
If an integer appears in the list multiple times, each copy is considered to be different; that is, two pairs are considered different if one pair includes at least one array index which the other doesn't, even if they include the same values.

Input
n is in the range [1, 100,000].
Each value arr[i] is in the range [1, 1,000,000,000].
k is in the range [1, 1,000,000,000].

Output
Return the number of different pairs of elements which sum to k.

Example 1
n = 5
k = 6
arr = [1, 2, 3, 4, 3]
output = 2
The valid pairs are 2+4 and 3+3.

Example 2
n = 5
k = 6
arr = [1, 5, 3, 3, 3]
output = 4
There's one valid pair 1+5, and three different valid pairs 3+3 (the 3rd and 4th elements, 3rd and 5th elements, and 4th and 5th elements).
'''


import pytest


def numberOfWays_brute(arr: list[int], k: int) -> int:
    '''
    O(n ** 2)
    '''
    pairs_count = 0
    # O(n ** 2)
    for i in range(len(arr)):
        diff = k - arr[i]
        # O(n)
        for j in range(i + 1, len(arr)):
            if arr[j] == diff:
                pairs_count += 1

    return pairs_count


def count_pairs_combs(arr: list[int], k: int) -> int:
    '''
    O(n)
    '''
    frequencies = dict()

    # O(n)
    for i in range(len(arr)):
        if arr[i] in frequencies:
            frequencies[arr[i]] += 1
        else:
            frequencies[arr[i]] = 1

    pairs_count = 0
    # O(n)
    for key in frequencies:
        if frequencies[key] == 0:
            continue

        diff = k - key
        if diff == key:
            pairs_count += frequencies[key] * (frequencies[key] - 1) / 2
        elif diff in frequencies:
            pairs_count += frequencies[key] * frequencies[diff]
            frequencies[diff] = 0
    
    return pairs_count


@pytest.mark.parametrize(
    'function', (
        numberOfWays_brute,
        count_pairs_combs
    )
)
@pytest.mark.parametrize(
    ('array', 'k', 'pairs'), (
        ([1, 2, 3, 4, 3], 6, 2),
        ([1, 5, 3, 3, 3], 6, 4),
        ([2], 10, 0),
        ([1, 2, 2, 2, 3, 4, 4], 6, 6)
    )
)
def test(function, array, k, pairs):
    assert function(array, k) == pairs
