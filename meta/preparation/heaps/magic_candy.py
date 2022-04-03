'''
Magical Candy Bags
You have N bags of candy. The ith bag contains arr[i] pieces of candy, and each of the bags is magical!
It takes you 1 minute to eat all of the pieces of candy in a bag (irrespective of how many pieces of candy are inside), and as soon as you finish, the bag mysteriously refills. If there were x pieces of candy in the bag at the beginning of the minute, then after you've finished you'll find that floor(x/2) pieces are now inside.
You have k minutes to eat as much candy as possible. How many pieces of candy can you eat?

Signature
int maxCandies(int[] arr, int K)

Input
1 ≤ N ≤ 10,000
1 ≤ k ≤ 10,000
1 ≤ arr[i] ≤ 1,000,000,000

Output
A single integer, the maximum number of candies you can eat in k minutes.

Example 1
N = 5 
k = 3
arr = [2, 1, 7, 4, 2]
output = 14
In the first minute you can eat 7 pieces of candy. That bag will refill with floor(7/2) = 3 pieces.
In the second minute you can eat 4 pieces of candy from another bag. That bag will refill with floor(4/2) = 2 pieces.
In the third minute you can eat the 3 pieces of candy that have appeared in the first bag that you ate.
In total you can eat 7 + 4 + 3 = 14 pieces of candy.
---

kinda greedy algorithm, prioritize max bag

construct max heap, O(n log n)
for each minute, O(k)
  pop max bag from heap, O(log n)
  add it to total
  halve it and, if it's > 0, push it to heap, O(log n)
return total

k ~ n | n > k, O(n log n)
k > n, O(k log n)

a = [2, 1, 7, 4, 2]
h = [2, 1, 2, 2, 1]

s = 0
k = 0
  s = 7
k = 1
  s = 7 + 4 = 11
k = 2
  s = 11 + 3 = 14
'''


import heapq
from dataclasses import dataclass


@dataclass
class MaxHeap:
    _heap = list()
    
    def push(self, number):
        heapq.heappush(self._heap, -1 * number)
    
    def pop(self):
        return -1 * heapq.heappop(self._heap)

    def is_empty(self):
        return len(self._heap) == 0


def maxCandies(arr, k):
    heap = MaxHeap()
    
    # TODO: building a heap can be improved to O(n)
    # O(n log n)
    for bag in arr:
        heap.push(bag)
    
    candies = 0
    # O(k log n)
    while k > 0:
        if heap.is_empty():
            break
        
        # O(log n)
        maxbag = heap.pop()
        candies += maxbag
        
        refill = maxbag // 2
        if refill > 0:
            # O(log n)
            heap.push(refill)
        
        k -= 1
    
    return candies