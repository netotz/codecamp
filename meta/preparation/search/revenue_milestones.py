'''
Revenue Milestones
We keep track of the revenue Facebook makes every day, and we want to know on what days Facebook hits certain revenue milestones. Given an array of the revenue on each day, and an array of milestones Facebook wants to reach, return an array containing the days on which Facebook reached every milestone.

Input
revenues is a length-N array representing how much revenue FB made on each day (from day 1 to day N). milestones is a length-K array of total revenue milestones.

Output
Return a length-K array where K_i is the day on which FB first had milestones[i] total revenue. If the milestone is never met, return -1.

Example
revenues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
milestones = [100, 200, 500]
output = [4, 6, 10]
Explanation
On days 4, 5, and 6, FB has total revenue of $100, $150, and $210 respectively. Day 6 is the first time that FB has >= $200 of total revenue.
'''

import bisect

import pytest


def getMilestoneDays(revenues: list[int], milestones: list[int]) -> list[int]:
    '''
    Time O(n + m log n)
    
    Space O(1)
    '''
    # cumulative sum of revenues, it'll end sorted
    # O(n)
    for day in range(1, len(revenues)):
        revenues[day] += revenues[day - 1]
    
    output = list()
    
    # (m log n)
    for i in range(len(milestones)):
        # use binary search to locate the day where current milestone was reached
        # O(log n)
        position = bisect.bisect_left(revenues, milestones[i])
        day_reached = position + 1 if position < len(revenues) else -1
        output.append(day_reached)
    
    return output


@pytest.mark.parametrize(
    ('revenues', 'milestones', 'output'), (
        ([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [100, 200, 500], [4, 6, 10]),
        ([100, 200, 300, 400, 500], [300, 800, 1000, 1400], [2, 4, 4, 5]),
        ([700, 800, 600, 400, 600, 700], [3100, 2200, 800, 2100, 1000], [5, 4, 2, 3, 2])
    )
)
def test(revenues: list[int], milestones: list[int], output: list[int]) -> None:
    assert getMilestoneDays(revenues, milestones) == output
