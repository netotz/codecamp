"""
there are 9 special numbers for every 100 numbers

1-9 -> 9 specials
10-99 -> 9 specials
100-999 -> 90 specials
1000-9999 -> 900 specials
"""


def count_specials(l: int, r: int) -> int:
    """
    TODO: use pattern
    """
    count = 0

    # O(r - l)
    for i in range(l, r + 1):
        string = str(i)
        if string[0] == string[-1]:
            count += 1

    return count


if __name__ == "__main__":
    l, r = map(int, input().split())

    count = count_specials(l, r)
    print(count)
