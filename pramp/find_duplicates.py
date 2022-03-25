'''
https://www.pramp.com/challenge/15oxrQx6LjtQj9JK9XlA

Find The Duplicates
Given two sorted arrays arr1 and arr2 of passport numbers, implement a function findDuplicates that returns an array of all passport numbers that are both in arr1 and arr2. Note that the output array should be sorted in an ascending order.

Let N and M be the lengths of arr1 and arr2, respectively. Solve for two cases and analyze the time & space complexities of your solutions: M ≈ N - the array lengths are approximately the same M ≫ N - arr2 is much bigger than arr1.

Example:

input:  arr1 = [1, 2, 3, 5, 6, 7], arr2 = [3, 6, 7, 8, 20]

output: [3, 6, 7] # since only these three values are both in arr1 and arr2
Constraints:

[time limit] 5000ms

[input] array.integer arr1

1 ≤ arr1.length ≤ 100
[input] array.integer arr2

1 ≤ arr2.length ≤ 100
[output] array.integer
'''

# are numbers unique in each array?


from bisect import bisect_left
import pytest


def solve_iter_skip(arr1: list[int], arr2: list[int]) -> list[int]:
    '''
    Best solution when n ~= m.
    
    Time O(n + m)

    Space O(n) or O(m), whichever is smaller
    '''
    # base cases where arrays start and end at different ranges
    if arr2[0] > arr1[-1] or arr1[0] > arr2[-1]:
        return []

    output = []

    i = 0
    j = 0
    # O(n + m)
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            output.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    return output


def solve_sets(arr1: list[int], arr2: list[int]) -> list[int]:
    # O(n)
    set1 = set(arr1)
    # O(m)
    set2 = set(arr2)
    # O(n log n) or O(m log m), whichever is smaller
    return sorted(set1 & set2)


def solve_binary(arr1: list[int], arr2: list[int]) -> list[int]:
    '''
    Best solution when m >> n

    Time O(n log m)

    Space O(n)
    '''
    if arr2[0] > arr1[-1] or arr1[0] > arr2[-1]:
        return []

    output = []
    j = 0

    # O(n)
    for i in range(len(arr1)):
        # O(log m)
        j = bisect_left(arr2, arr1[i], lo=j)
        if j < len(arr2) and arr2[j] == arr1[i]:
            output.append(arr1[i])
    
    return output


@pytest.mark.parametrize(
    'function', [
        solve_iter_skip,
        solve_sets,
        solve_binary
    ]
)
@pytest.mark.parametrize(
    ('arr1', 'arr2', 'output'), [
        ([1, 2, 3, 9], [3, 6, 7, 8, 9, 20], [3, 9]),
        ([10,20,30,40,50,60,70,80], [10,20,30,40,50,60], [10,20,30,40,50,60]),
        ([1, 2, 3, 5, 6, 7], [3, 6, 7, 8, 20], [3, 6, 7]),
        ([1, 2, 3], [4, 5, 6], []),
        ([4, 5, 6], [1, 2, 3], []),
        ([2, 3], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3], [2, 3])
    ]
)
def test(function, arr1, arr2, output):
    assert function(arr1, arr2) == output
