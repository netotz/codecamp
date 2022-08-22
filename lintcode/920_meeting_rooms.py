"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
determine if a person could attend all meetings.

(0,8),(8,10) is not conflict at 8
---

is the input sorted and using what as reference (si or ei)? I'm assuming it's not
what if the list if empty?

A person can't go to a meeting that starts at the same time or before the previous one.
All start times must be greater than the end time of the previous meeting, except the first one.

sort intervals by start time, O(n log n)
check from 2nd interval if s_i > e_(i-1) for all intervals, O(n)
"""

import pytest


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def can_attend(intervals: list[Interval]) -> bool:
    """
    time O(n log n)

    space O(1)
    """
    if not intervals or len(intervals) == 1:
        return True

    # O(n log n)
    intervals.sort(key=lambda i: i.start)

    # O(n)
    for i in range(1, len(intervals)):
        if intervals[i].start < intervals[i - 1].end:
            return False

    return True


@pytest.mark.parametrize(
    ("intervals", "answer"),
    [
        ([Interval(0, 30), Interval(5, 10), Interval(15, 20)], False),
        ([Interval(5, 8), Interval(9, 15)], True),
    ],
)
def test(intervals, answer):
    assert can_attend(intervals) == answer
