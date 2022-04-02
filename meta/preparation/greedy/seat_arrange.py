'''
Seating Arrangements
There are n guests attending a dinner party, numbered from 1 to n. The ith guest has a height of arr[i-1] inches.
The guests will sit down at a circular table which has n seats, numbered from 1 to n in clockwise order around the table. As the host, you will choose how to arrange the guests, one per seat. Note that there are n! possible permutations of seat assignments.
Once the guests have sat down, the awkwardness between a pair of guests sitting in adjacent seats is defined as the absolute difference between their two heights. Note that, because the table is circular, seats 1 and n are considered to be adjacent to one another, and that there are therefore n pairs of adjacent guests.
The overall awkwardness of the seating arrangement is then defined as the maximum awkwardness of any pair of adjacent guests. Determine the minimum possible overall awkwardness of any seating arrangement.

Signature
int minOverallAwkwardness(int[] arr)

Input
n is in the range [3, 1000].
Each height arr[i] is in the range [1, 1000].

Output
Return the minimum achievable overall awkwardness of any seating arrangement.

Example
n = 4
arr = [5, 10, 6, 8]
output = 4
If the guests sit down in the permutation [3, 1, 4, 2] in clockwise order around the table (having heights [6, 5, 8, 10], in that order), then the four awkwardnesses between pairs of adjacent guests will be |6-5| = 1, |5-8| = 3, |8-10| = 2, and |10-6| = 4, yielding an overall awkwardness of 4. It's impossible to achieve a smaller overall awkwardness.
---

minimax problem

sort array, O(n log n)
max awk is between first and last guest, smallest and tallest, so it needs to be broken.
swap smallest for third tallest,
because the 3 tallest must sit together, tallest in the middle; and 3 smallest too, smallest in the middle - (1)
but what about the rest of guests, if any? how to group them?

one idea is to iteratively break the new max pair by swapping one of the guests, while also maintaining (1)
but how to keep track of maximums?
max and min heaps to swap elements?

to minimize the difference, one can arrange each guest such that its neighbors have the most similar height to it, satisfying (1):
put the smallest in the middle, then put the second smallest to its left and the third smallest to the right... and so on.
at the end, the tallest would have the second tallest to its right and the third tallest to its left.

[1 2 3 4 5 6 7 8 9] -> [8 6 4 2 1 3 5 7 9]

in a linear dimension this looks like a sliced normal distribution,
because the smallests are in the middle and the tallest in the edges:

    |           |
    |  |     |  |
... |  |  |  |  | ...

so we can create a list of guests at even indexes, then add the reversed list of guests at odd indexes in O(n),
or add them all directly to a deque, alternating sides, in O(n),
then calculate the difference between:
second and first, last and penultimate, (as in both cases they will be together), and each alternate pair;
and return the max in O(n).

this not only does unnecessary work by creating the actual arrangement of guests
which is not being asked (unnecessary extra space, we only need the max difference),
but also duplicated work because all the guests are visited multiple times.

we are alternating from even to odd indexes and so on.
this means that we can traverse the array every 2 indexes,
and at the same time calculating differences between adjacents, returning the max at the end.
still O(n) but more efficient and O(1) space.
'''


def minOverallAwkwardness(arr: list[int]) -> int:
    '''
    Time O(n log n)
    
    Space O(1)
    '''
    # O(n log n)
    arr.sort()

    maxdiff = max(arr[1] - arr[0], arr[-1] - arr[-2])
    # O(n)
    for i in range(2, len(arr)):
        maxdiff = max(maxdiff, arr[i] - arr[i - 2])
    
    return maxdiff
