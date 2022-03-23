'''
Balanced Split
Given an array of integers (which may include repeated integers), determine if there's a way to split the array into two subsequences A and B such that the sum of the integers in both arrays is the same, and all of the integers in A are strictly smaller than all of the integers in B.
Note: Strictly smaller denotes that every integer in A must be less than, and not equal to, every integer in B.

Signature
bool balancedSplitExists(int[] arr)

Input
All integers in array are in the range [0, 1,000,000,000].

Output
Return true if such a split is possible, and false otherwise.

Example 1
arr = [1, 5, 7, 1]
output = true
We can split the array into A = [1, 1, 5] and B = [7].

Example 2
arr = [12, 7, 6, 7, 6]
output = false
We can't split the array into A = [6, 6, 7] and B = [7, 12] since this doesn't satisfy the requirement that all integers in A are smaller than all integers in B.
'''


import random
import pytest


def balancedSplitExists(arr: list[int]) -> bool:
    '''
    Time O(n log n)

    Space O(1)
    '''
    summation = sum(arr)
    
    # odd sum cannot be split
    if summation % 2 == 1:
        return False
    
    # O(n log n)
    arr.sort()
    
    half_sum = 0
    # sum elements one at a time until
    # it equals half the total summation
    # and left elements are less than right
    # O(n)
    for i in range(len(arr)):
        half_sum += arr[i]
        if half_sum * 2 == summation and arr[i] < arr[i + 1]:
            return True
    
    return False


def can_split_quickselect(arr: list[int]) -> bool:
    '''
    Time O(n) average
    
    Space O(1)
    '''
    def partition(arr: list[int], left_sum: int) -> None:
        smallers = list()
        greaters = list()
        
        # temporary sum of elements less than pivot
        temp_sum = 0
        # O(n)
        for i in range(len(arr)):
            if arr[i] > pivot:
                greaters.append(arr[i])
                continue

            temp_sum += arr[i]
            if arr[i] < pivot:
                smallers.append(arr[i])
        
        # if left sum is greater than right
        if temp_sum + left_sum > half_sum:
            # partition smaller elements in next iteration
            arr = smallers
            return arr, left_sum

        # if right sum is greater,
        # update left sum with temporary sum
        left_sum += temp_sum
        # and partition greater elements in next iteration
        arr = greaters

        return arr, left_sum
    
    # O(n)
    summation = sum(arr)
    
    if summation % 2 == 1:
        return False
    
    half_sum = summation // 2
    left_sum = 0

    # while array is not empty
    while len(arr) > 0:
        # choose random pivot
        pivot = random.choice(arr)
        # apply quickselect on pivot using partition
        # and use whichever half has greater sum
        arr, left_sum = partition(arr, left_sum)

        if left_sum == half_sum:
            return True
    
    return False


@pytest.mark.parametrize(
    ('function'), [
        balancedSplitExists,
        can_split_quickselect
    ]
)
@pytest.mark.parametrize(
    ('arr', 'can_split'), [
        ([1, 5, 7, 1], True),
        ([12, 7, 6, 7, 6], False),
        ([2, 1, 2, 5], True),
        ([3, 6, 3, 4, 4], False)
    ]
)
def test(function, arr: list[int], can_split: bool) -> None:
    assert function(arr) == can_split
