'''
Slow Sums
Suppose we have a list of N numbers, and repeat the following operation until we're left with only a single number: Choose any two numbers and replace them with their sum. Moreover, we associate a penalty with each operation equal to the value of the new number, and call the penalty for the entire list as the sum of the penalties of each operation.
For example, given the list [1, 2, 3, 4, 5], we could choose 2 and 3 for the first operation, which would transform the list into [1, 5, 4, 5] and incur a penalty of 5. The goal in this problem is to find the highest possible penalty for a given input.

Input:
An array arr containing N integers, denoting the numbers in the list.

Output format:
An int representing the highest possible total penalty.

Constraints:
1 ≤ N ≤ 10^6
1 ≤ Ai ≤ 10^7, where *Ai denotes the ith initial element of an array.
The sum of values of N over all test cases will not exceed 5 * 10^6.

Example
arr = [4, 2, 1, 3]
output = 26
First, add 4 + 3 for a penalty of 7. Now the array is [7, 2, 1]
Add 7 + 2 for a penalty of 9. Now the array is [9, 1]
Add 9 + 1 for a penalty of 10. The penalties sum to 26.
'''


import pytest


def getTotalTime(arr: list[int]) -> int:
    '''
    O(n log n)
    '''
    if len(arr) < 2:
        return 0

    # by sorting the array in descending order,
    # the greatest numbers will be added first
    # O(n log n)
    sorted_arr = sorted(arr, reverse=True)
    
    operation = sorted_arr[0] + sorted_arr[1]
    penalty = operation
    # O(n)
    for i in range(2, len(sorted_arr)):
        operation += sorted_arr[i]
        penalty += operation
    
    return penalty


@pytest.mark.parametrize(
    ('array', 'penalty'), (
        ([4, 2, 1, 3], 26),
        ([2, 3, 9, 8, 4], 88)
    )
)
def test(array, penalty):
    assert getTotalTime(array) == penalty
