"""
at least 1 taxi would always be needed.
in the worst case, t = n where t is the number of taxis

use a bucket of group sizes
first fill the groups of 4 by using 1 taxi for each group,
then the groups of 3 by using 1 for each and fill their gaps by subtracting them to the groups of 1,
then the groups of 2 by using 1 for every 2 group, adding 1 extra if it's an odd amount and subtracting 2 to groups of 1,
and the groups of 1 by using 1 for every 4 groups, adding 1 extra if the amount is not divisible by 4
"""


TAXI_CAPACITY = 4


def get_min_taxis(friends: list[int]) -> int:
    """
    time O(n)

    space O(1)
    """
    # create a bucket to count amount of each size, from 1 to 4
    bucket = {capacity: 0 for capacity in range(1, 5)}

    # O(n)
    for f in friends:
        bucket[f] += 1

    # 1 taxi for each group of 4
    taxis = bucket[4]
    # 1 taxi for each group of 3
    taxis += bucket[3]
    # fit groups of 1, if any
    bucket[1] = max(bucket[1] - bucket[3], 0)

    # 1 taxi for every 2 groups of 2
    taxis += bucket[2] // 2
    # if there is an extra group of 2
    if bucket[2] % 2 != 0:
        # request another taxi for the extra group
        taxis += 1
        # fit 2 groups of 1, if any
        bucket[1] = max(bucket[1] - 2, 0)

    # 1 taxi for every 4 groups of 1
    taxis += bucket[1] // 4
    # if there are extra groups of 4
    if bucket[1] % 4 != 0:
        # all the remaining (max 3) fit in 1 taxi
        taxis += 1

    return taxis


if __name__ == "__main__":
    n = int(input())
    # O(n)
    friends_n = list(map(int, input().split()))

    taxis = get_min_taxis(friends_n)
    print(taxis)
