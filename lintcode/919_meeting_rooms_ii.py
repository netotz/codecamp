"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required to host all the meetings.

sort intervals, O(n log n)
for each interval,
    for each room,
        if start time > last meeting of current room,
            fit it in
            break
    
    if no available room, add new room
time O(n**2)

sort intervals by start time, O(n log n)
use min heap for rooms, storing the end times of previous meetings
for each interval, O(n)
    if no heap,
        add end
    elif start > min of heap,
        pop heap, push end, O(log n)
    else,
        push end, O(log n)
return length of heap

                                                          i
..., (17, 20), (25, 30), (30, 35), (36, 37), (37, 40), (38, 41)

s = [37, 40, 35]
"""

import heapq
import pytest


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def get_min_rooms_heap(intervals: list[Interval]) -> int:
    """
    time O(n log n)

    space O(n)
    """
    if not intervals:
        return 0

    # O(n log n)
    intervals.sort(key=lambda i: i.start)

    rooms = []

    ## O(n log n)
    # O(n)
    for interval in intervals:
        if not rooms or interval.start < rooms[0]:
            # O(log n)
            heapq.heappush(rooms, interval.end)
        else:
            # O(log n)
            heapq.heapreplace(rooms, interval.end)

    return len(rooms)


@pytest.mark.parametrize(
    ("intervals", "answer"),
    [([Interval(0, 30), Interval(5, 10), Interval(15, 20)], 2), ([Interval(2, 7)], 1)],
)
def test(intervals, answer):
    assert get_min_rooms_heap(intervals) == answer
