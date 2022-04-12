'''
Median Stream
You're given a list of n integers arr[0..(n-1)]. You must compute a list output[0..(n-1)] such that, for each index i (between 0 and n-1, inclusive), output[i] is equal to the median of the elements arr[0..i] (rounded down to the nearest integer).
The median of a list of integers is defined as follows. If the integers were to be sorted, then:
If there are an odd number of integers, then the median is equal to the middle integer in the sorted order.
Otherwise, if there are an even number of integers, then the median is equal to the average of the two middle-most integers in the sorted order.

Signature
int[] findMedian(int[] arr)

Input
n is in the range [1, 1,000,000].
Each value arr[i] is in the range [1, 1,000,000].

Output
Return a list of n integers output[0..(n-1)], as described above.

Example 1
n = 4
arr = [5, 15, 1, 3]
output = [5, 10, 5, 4]
The median of [5] is 5, the median of [5, 15] is (5 + 15) / 2 = 10, the median of [5, 15, 1] is 5, and the median of [5, 15, 1, 3] is (3 + 5) / 2 = 4.
Example 2
n = 2
arr = [1, 2]
output = [1, 1]
The median of [1] is 1, the median of [1, 2] is (1 + 2) / 2 = 1.5 (which should be rounded down to 1).

---
input: array
output: array

a brute force approach is to sort all the numbers before the current index.
for each index, O(n)
    sort elements up to this index, O(n log n)
    get median
total O(n**2)

split the array in 2 (almost) equal halves,
using a max heap for the smaller numbers,
and a min heap for the greater numbers.
in this way, the root of the max heap will always be smaller than the root of the min heap,
and both roots can be used to get the median if both heaps have the same size,
otherwise the root of the largest heap is the median.

for each index, O(n)
    if index is even,
        push number to min heap, O(log n)
        pop min heap, O(log n)
        and push it to max heap, O(log n)
        
        get median = peek max heap
    if it's odd,
        push number to max heap, O(log n)
        pop max heap, O(log n)
        and push it to min heap, O(log n)
    
        median = peek both heaps, add numbers, divide by 2
total O(n log n)

 0  1   2  3
[5, 15, 1, 3]
           i
sh = [3, 1]
gh = [5, 15]
o = [5, 10, 5, 4]

 0  1  2  3  4  5
[2, 4, 7, 1, 5, 3]
                i
sh = [3, 2, 1]
gh = [4, 5, 7]
o = [2, 3, 4, 3, 4, 3]
'''


import heapq


def findMedian(arr):
    '''
    Time O(n log n)
    
    Space O(n)
    '''
    maxheap = []
    minheap = []
    
    out = []
    # O(n log n)
    for i in range(len(arr)):
        if i % 2 == 0:
            # O(log n)
            num = heapq.heappushpop(minheap, arr[i])
            # O(log n)
            heapq.heappush(maxheap, -num)
            
            median = -maxheap[0]
        else:
            # O(log n)
            num = -heapq.heappushpop(maxheap, -arr[i])
            # O(log n)
            heapq.heappush(minheap, num)
            
            median = (-maxheap[0] + minheap[0]) // 2

        out.append(median)
    
    return out
