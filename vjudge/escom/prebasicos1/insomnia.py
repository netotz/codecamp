def read_series():
    return {int(input()) for _ in range(4)}


def read_total():
    return int(input())


def count_harmed(series: set[int], total: int) -> int:
    count = 0
    # O(n)
    for i in range(1, total + 1):
        if any(i % s == 0 for s in series):
            count += 1

    return count


if __name__ == "__main__":
    series = read_series()
    total = read_total()

    if 1 in series:
        harmed = total
    else:
        harmed = count_harmed(series, total)
    print(harmed)
