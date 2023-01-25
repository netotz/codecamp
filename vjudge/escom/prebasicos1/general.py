"""
n = 7
0   1  2  3  4  5  6   i

10 10 58 31 63 40 76
10 10 58 31 63 76 40
10 10 58 31 76 63 40
...
10 76 10 58 31 63 40
76 10 10 58 31 63 40
"""

import math


def get_min_moves(heights: list[int], n: int):
    max_height = -math.inf
    min_height = math.inf
    imax = imin = -1

    # O(n)
    for i in range(n):
        if heights[i] > max_height:
            max_height = heights[i]
            imax = i
        if heights[i] <= min_height:
            min_height = heights[i]
            imin = i

    # if heights are all the same
    if imax == imin:
        return 0

    moves = imax + (n - 1 - imin)
    if imin < imax:
        moves -= 1
    return moves


if __name__ == "__main__":
    n = int(input())
    heights = list(map(int, input().split()))

    answer = get_min_moves(heights, n)
    print(answer)
