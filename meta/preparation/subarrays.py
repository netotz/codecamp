'''
Contiguous Subarrays
You are given an array arr of N integers. For each index i, you are required to determine the number of contiguous subarrays that fulfill the following conditions:
- The value at index i must be the maximum element in the contiguous subarrays, and
- These contiguous subarrays must either start from or end on index i.

Input
Array arr is a non-empty list of unique integers that range between 1 to 1,000,000,000
Size N is between 1 and 1,000,000

Output
An array where each index i contains an integer denoting the maximum number of contiguous subarrays of arr[i]

Example:
arr = [3, 4, 1, 6, 2]
output = [1, 3, 1, 5, 1]
Explanation:
For index 0 - [3] is the only contiguous subarray that starts (or ends) with 3, and the maximum value in this subarray is 3.
For index 1 - [4], [3, 4], [4, 1]
For index 2 - [1]
For index 3 - [6], [6, 2], [1, 6], [4, 1, 6], [3, 4, 1, 6]
For index 4 - [2]
So, the answer for the above input is [1, 3, 1, 5, 1]
'''

# let lefts[i] be the number of valid subarrays ending with arr[i],
# and rights[i] the ones beginning with arr[i],
# then subarrays[i] = lefts[i] + rights[i] + 1,
# plus one because a subarray that contains only arr[i] is valid too.
# Now, calculating rights[i] is the same as calculating lefts[i] of arr.reverse().


import pytest


def count_subarrays(arr: list[int]) -> list[int]:
    # stack to store indexes of arr to compare against current.
    # bottom of stack, if any, is index of max(arr[:i]), the greatest yet
    stack = []

    # count subarrays that end with arr[i]
    # by checking valid subarrays from left of arr
    lefts = [0 for _ in arr]
    for i in range(len(arr)):
        # if top of stack (decreasing previous indexes) is less than current,
        # discard it as it's useless against current, and check next
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()
        
        # if stack is not empty, top is index of left-most greater number than current arr[i]
        if stack:
            lefts[i] += i - stack[-1] - 1
        # if stack is empty, current arr[i] is max(arr[:i + 1]), the greatest yet
        else:
            lefts[i] += i

        # push current index to stack to be compared against next
        stack.append(i)
    
    # reset stack
    stack = []

    # now count subarrays that begin with arr[i]
    # by checking valid subarrays from right of arr by reversing indexes
    rights = [0 for _ in arr]
    for i in range(len(arr) - 1, -1, -1):
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()

        if stack:
            rights[i] += stack[-1] - i - 1
        else:
            rights[i] += len(arr) - 1 - i
        
        stack.append(i)
    
    return [lefts[i] + rights[i] + 1 for i in range(len(arr))]


@pytest.mark.parametrize(
    ('array', 'subarrays_number'), (
        ([3, 4, 1, 6, 2], [1, 3, 1, 5, 1]),
        ([2, 4, 7, 1, 5, 3], [1, 2, 6, 1, 3, 1])
    )
)
def test(array, subarrays_number):
    assert count_subarrays(array) == subarrays_number
