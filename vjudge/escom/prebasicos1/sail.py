def get_earliest(t: int, directions: str, xdiff: int, ydiff: int):
    EAST = "E"
    WEST = "W"
    SOUTH = "S"
    NORTH = "N"

    # O(t)
    for i in range(t):
        d = directions[i]

        if d == EAST and xdiff > 0:
            xdiff -= 1
        elif d == WEST and xdiff < 0:
            xdiff += 1

        if d == NORTH and ydiff > 0:
            ydiff -= 1
        elif d == SOUTH and ydiff < 0:
            ydiff += 1

        if xdiff == 0 and ydiff == 0:
            return i + 1

    return -1


if __name__ == "__main__":
    t, sx, sy, ex, ey = list(map(int, input().split()))
    dirs = input()

    xdiff = ex - sx
    ydiff = ey - sy

    answer = get_earliest(t, dirs, xdiff, ydiff)
    print(answer)
