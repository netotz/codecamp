"""
sort array and count the differences against unsorted,
if there are more than 2 differences, it wasn't an accident
"""


def was_accident(n: int, array: list[int]) -> bool:
    """
    time O(n log n)

    space O(n)
    """
    # O(n log n)
    sorted_array = sorted(array)

    diffs = 0
    # O(n)
    for i in range(n):
        if array[i] != sorted_array[i]:
            diffs += 1

        if diffs > 2:
            return False

    return True


if __name__ == "__main__":
    n = int(input())
    # O(n)
    array = list(map(int, input().split()))

    answer = "YES" if was_accident(n, array) else "NO"
    print(answer)
