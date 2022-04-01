'''
Implement a function to merge 3 sorted integer arrays.
The output should be another sorted integer array consisting of all integers from the 3 input arrays.
The input arrays may have duplicates, but the output array shouldn't have any duplicate.

arrays can be empty
arrays can have different lengths

use 3 pointers in a list, one for each array
    for each pointer,
        if pointer >= lenght of its array, continue
        determine smallest element and its array
    if all pointers were skipped, return output
    add smallest to output, if it's not duplicated by checking last element
    advance pointer of smallest
return output
O(a + b + c)

              i
a = [1, 1, 2]
           j
b = [2, 3]
              k
c = [2, 5, 7]

p = [3, 2, 2]
o = [1, 2, 3, 5, 7]
'''


import sys

import pytest


def merge(a, b, c):
    out = []
    pointers = [0, 0, 0]
    arrays = [a, b, c]

    # O(a + b + c)
    while True:
        smallest = sys.maxsize
        smallest_index = -1

        for i in range(3):
            p = pointers[i]
            arr = arrays[i]
            if p >= len(arr):
                continue
            
            if arr[p] < smallest:
                smallest = arr[p]
                smallest_index = i
        
        if smallest_index == -1:
            break

        if len(out) == 0 or smallest > out[-1]:
            out.append(smallest)
        
        pointers[smallest_index] += 1
    
    return out


@pytest.mark.parametrize(
    ('a', 'b', 'c', 'out'), [
        ([1,1,2], [2,3], [2,5,7], [1,2,3,5,7]),
        ([], [], [], []),
        ([], [], [1], [1]),
        ([0,1,2], [0,1], [0], [0,1,2]),
        ([1,1,1], [1,1,1], [1,1,1], [1])
    ]
)
def test(a, b, c, out):
    assert merge(a, b, c) == out
