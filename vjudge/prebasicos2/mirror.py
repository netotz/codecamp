"""
minimum number of flips to make the square 

1 1 0 0 1
0 0 0 0 0
1 1 1 1 1
1 0 1 1 0
0 1 1 1 1

1 1 1 0 1
0 0 1 0 1
1 1 1 1 1
1 0 1 0 0
1 0 1 1 1
d = 6
"""


def read_matrix() -> list[list[int]]:
    n = int(input())
    return [[int(c) for c in input()] for _ in range(n)]


def get_min_flips(matrix: list[list[int]]) -> int:
    """
    Compare groups of 4 cells from the outer layer and go inwards.
    """
    n = len(matrix)
    flips = 0

    left = 0
    right = n - 1

    while left <= right:
        top = left
        bottom = right

        # the first group is the corners so offset must start as 0,
        # the number of offsets is the number of columns in a row except the last one
        for offset in range(right - left):
            # difference of ones and zeroes,
            # a positive diff means there are more 1s,
            # a negative diff means there are more 0s
            diff = 0

            topleft = matrix[top][left + offset]
            diff += 1 if topleft == 1 else -1

            topright = matrix[top + offset][right]
            diff += 1 if topright == 1 else -1

            bottomleft = matrix[bottom - offset][left]
            diff += 1 if bottomleft == 1 else -1

            bottomright = matrix[bottom][right - offset]
            diff += 1 if bottomright == 1 else -1

            diff = abs(diff)
            # if all cells are the same number, flips remains the same
            # if 3 cells are the same
            if diff == 2:
                flips += 1
            # if 2 cells are the same
            elif diff == 0:
                flips += 2

        left += 1
        right -= 1

    return flips


if __name__ == "__main__":
    t = int(input())
    while t > 0:
        matrix = read_matrix()
        answer = get_min_flips(matrix)
        print(answer)

        t -= 1
