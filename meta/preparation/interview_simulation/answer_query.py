'''
Answer a Query
Imagine a length-N array of booleans, initially all false. Over time, some values are set to true, and at various points in time you would like to find the location of the nearest true to the right of given indices.
You will receive Q queries, each of which has a type and a value. SET queries have type = 1 and GET queries have type = 2.
When you receive a SET query, the value of the query denotes an index in the array that is set to true. Note that these indices start at 1. When you receive a GET query, you must return the smallest index that contains a true value that is greater than or equal to the given index, or -1 if no such index exists.

Input
A list of Q queries, formatted as [type, index] where type is either 1 or 2, and index is < N
1 <= N <= 1,000,000,000
1 <= Q <= 500,000

Output
Return an array containing the results of all GET queries. The result of queries[i] is the smallest index that contains a true value that is greater than or equal to i, or -1 if no index satisfies those conditions.

Example
N = 5
Q = 5
queries = [[2, 3], [1, 2], [2, 1], [2, 3], [2, 2]]
output = [-1, 2, -1, 2]
The initial state of the array is [false, false, false, false, false].
The first query is GET 3, but no values in the array are true, so the answer is -1.
The second query is SET 2, so the value at index 2 is set to true.
The new state of the array is [false, true, false, false, false].
The third query is GET 1, and the index of the true value nearest to 1 (to the right) is 2.
The fourth query is GET 3, but no values to the right of index 3 are true.
The fifth query is GET 2, and the value at index 2 is true.
'''


import bisect
import heapq
import pytest


def answer_queries_heaps(queries: list[list[int]], n: int) -> list[int]:
    '''
    Worst case for GET is O(n log n) because you'd need to pop all elements minus 1.
    Popping from heap is O(log n), and since you're popping them all,
    you're "destructing" the heap which has the same complexity as constructing it:
    O(n log n), because you're visiting each element.

    The size of the heap can be up to n, the size of the boolean array
    as it stores its indices, not the size of queries array Q.
    
    Time: O(qn log n)
    
    Space: O(n)
    '''
    SET = 1
    GET = 2

    output = []

    # min heap to keep track of minimum True index,
    # worst case |heap| = n
    heap = []

    # O(qn log n)
    for query, index in queries:
        if query == SET:
            # push True index to heap
            # O(log n)
            heapq.heappush(heap, index)
            continue

        if query == GET:
            backup = []
            # if target index is greater than heap root,
            # which is the minimum index that is True,
            # pop it and check next root,
            # which is new minimum but greater than previous minimum
            # O(n log n)
            while len(heap) > 0 and index > heap[0]:
                # backup popped root for future GETs
                # O(log n)
                min_true = heapq.heappop(heap)
                backup.append(min_true)
            
            # if heap is empty,
            # there's no True value at the right of index
            if len(heap) == 0:  
                output.append(-1)
            # heap root is closest right True index from target,
            # it's the first greater True index than target
            else:
                output.append(heap[0])
            
            # restore popped heap roots from backup
            # O(n log n)
            for b in backup:
                # O(log n)
                heapq.heappush(heap, b)

    return output


def answer_queries_bisect(queries: list[list[int]], n: int) -> list[int]:
    '''
    Using a "binary search list",
    which is a list that's always sorted even after inserting,
    the runtime of GET is reduced to O(log n),
    while runtime of SET is increased to O(n).
    However the overall complexity is still reduced by a factor of log n.

    Time: O(qn)

    Space: O(n)
    '''
    SET = 1
    GET = 2

    # binary search list (BSL),
    # its indexes will be called "positions",
    # which are 0-based too
    bsl = []
    output = []

    # O(qn)
    for query, index in queries:
        # O(log n + n) = O(n)
        if query == SET:
            # find position to insert target index
            # as to keep the list sorted
            # O(log n)
            position = bisect.bisect_left(bsl, index)
            # O(n)
            bsl.insert(position, index)
        # O(log n)
        elif query == GET:
            # get position where target index would be inserted
            # as if it were a SET query
            # O(log n)
            position = bisect.bisect_left(bsl, index)

            # if the position is less than BSL size,
            # it's within the range of BSL elements,
            # meaning that the index at the position
            # is the smallest of the indexes
            # that are greater than or equal to target index
            min_true = bsl[position] if position < len(bsl) else -1
            output.append(min_true)
    
    return output


@pytest.mark.parametrize(
    ('queries', 'n', 'output'), (
        (
            [[2, 3], [1, 2], [2, 1], [2, 3], [2, 2]],
            5,
            [-1, 2, -1, 2]
        )
    )
)
def test(queries: list[list[int]], n: int, output: list[int]) -> None:
    assert answer_queries_heaps(queries, n) == output
