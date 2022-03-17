'''
Reverse to Make Equal
Given two arrays A and B of length N, determine if there is a way to make A equal to B by reversing any subarrays from array B any number of times.

Input
All integers in array are in the range [0, 1,000,000,000].

Output
Return true if B can be made equal to A, return false otherwise.

Example
A = [1, 2, 3, 4]
B = [1, 4, 3, 2]
output = true
After reversing the subarray of B from indices 1 to 3, array B will equal array A.
'''

# do I must reverse subarrays?
# swapping is reversing subarrays of size 2, is sorting allowed?


from collections import Counter

import pytest


def reverse_subarray(array: list[int], start: int, end: int) -> list[int]:
    '''
    O(n/2) = O(n)
    '''
    i = start
    j = end
    while i < j:
        temp = array[i]
        array[i] = array[j]
        array[j] = temp

        i += 1
        j -= 1
    
    return array


def are_they_equal_brute(array_a: list[int], array_b: list[int]) -> bool:
    '''
    O(n ** 3)
    '''
    are_equal = True
    # iterate each element of both arrays at same time
    # O(n ** 3)
    for i in range(len(array_a)):
        if array_a[i] != array_b[i]:
            are_equal = False
            # when elements at same index are different,
            # loop rest of B until element is found
            # O(n ** 2 )
            for j in range(i + 1, len(array_b)):
                if array_b[j] == array_a[i]:
                    # when element is found, reverse subarray B[i:j + 1] in-place
                    # O(n)
                    array_b = reverse_subarray(array_b, i, j)
                    # now elements at same index i are equal
                    are_equal = True
                    break
            # if element wasn't found, A cannot be equal to B

    return are_equal


def are_they_equal_sorted(array_a: list[int], array_b: list[int]) -> bool:
    '''
    O(n log n)
    '''
    # O(n log n)
    array_a.sort()
    # O(n log n)
    array_b.sort()

    # O(n)
    for i in range(len(array_a)):
        if array_a[i] != array_b[i]:
            return False
    
    return True


def are_they_equal_counters(array_a: list[int], array_b: list[int]) -> bool:
    '''
    O(n)
    '''
    # hash map of counts of each element
    # O(n)
    a_counter = Counter(array_a)
    # O(n)
    b_counter = Counter(array_b)
    # O(n)
    return a_counter == b_counter


@pytest.mark.parametrize(
    'function', (
        are_they_equal_brute,
        are_they_equal_sorted,
        are_they_equal_counters
    )
)
@pytest.mark.parametrize(
    ('array_a', 'array_b', 'are_equal'), (
        ([1, 2, 3, 4], [1, 4, 3, 2], True),
        ([1, 2, 3, 4], [1, 2, 3, 5], False)
    )
)
def test(function, array_a, array_b, are_equal):
    assert function(array_a, array_b) == are_equal
