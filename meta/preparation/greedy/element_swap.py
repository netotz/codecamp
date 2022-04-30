'''
Element Swapping
Given a sequence of n integers arr, determine the lexicographically smallest sequence which may be obtained from it after performing at most k element swaps, each involving a pair of consecutive elements in the sequence.
Note: A list x is lexicographically smaller than a different equal-length list y if and only if, for the earliest index at which the two lists differ, x's element at that index is smaller than y's element at that index.

Signature
int[] findMinArray(int[] arr, int k)

Input
n is in the range [1, 1000].
Each element of arr is in the range [1, 1,000,000].
k is in the range [1, 1000].

Output
Return an array of n integers output, the lexicographically smallest sequence achievable after at most k swaps.

Example 1
n = 3
k = 2
arr = [5, 3, 1]
output = [1, 5, 3]
We can swap the 2nd and 3rd elements, followed by the 1st and 2nd elements, to end up with the sequence [1, 5, 3]. This is the lexicographically smallest sequence achievable after at most 2 swaps.
Example 2
n = 5
k = 3
arr = [8, 9, 11, 2, 1]
output = [2, 8, 9, 11, 1]
We can swap [11, 2], followed by [9, 2], then [8, 2].
'''


import pytest


def findMinArray(arr, k):
    if len(arr) == 1:
        return arr

    if k >= (len(arr) * (len(arr) + 1)) / 2:
        return sorted(arr)
    
    # O(n ** 2)
    for i in range(len(arr)):
        minindex = i
        j = i
        # O(n)
        while j < len(arr) and j <= i + k:
            if arr[j] < arr[minindex]:
                minindex = j
            j += 1

        j = minindex
        # O(n)
        while j > i:
            temp = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = temp

            j -= 1

        k -= minindex - i
        if k == 0:
            break

    return arr


import heapq
def findMinArrayH(arr, k):
  # Write your code here
  if k == 0 or len(arr)<2:
    return arr
  
  arr = [(x,i) for i, x in enumerate(arr)]
  
  min_heap = arr[:k+1]
  heapq.heapify(min_heap)
  l = 0
  
  # O(n)
  while l<len(arr) and k:
    # remove unreachable indices
    # O(n)
    while min_heap[0][1]>l+k+1:
        # O(log k)
      heapq.heappop(min_heap)
      
    x,i = min_heap[0]
    arr[l+1:i+1] = arr[l:i]
    arr[l] = (x,i)
    if l+k+1 < len(arr):
      heapq.heapreplace(min_heap,arr[l+k+1])
    else:
      heapq.heappop(min_heap)     
    k-= i-l
    l+=1
    
  return [x  for x,i in arr]


@pytest.mark.parametrize(
    ('arr', 'k', 'out'), [
        ([5, 3, 1], 2, [1, 5, 3]),
        ([8, 9, 11, 2, 1], 3, [2, 8, 9, 11, 1]),
        ([8, 9, 11, 2, 1], 2, [8, 2, 9, 11, 1]),
        ([1, 2, 8, 7, 6], 3, [1, 2, 6, 7, 8]),
        ([1, 1, 8, 1, 11, 2, 1], 4, [1, 1, 1, 1, 8, 11, 2]),
        ([1, 2, 3, 4, 5, 7, 6], 1, [1, 2, 3, 4, 5, 6, 7]),
        ([1, 2, 3, 4, 5, 7, 6], 2, [1, 2, 3, 4, 5, 6, 7]),
        ([5, 4, 3, 2, 1], 18, [1, 2, 3, 4, 5]),
        ([1, 2], 3, [1, 2]),
        ([1], 1, [1]),
    ]
)
def test(arr, k, out):
    assert findMinArrayH(arr, k) == out
