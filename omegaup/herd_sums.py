"""
sliding window

            l
1 2 3 4 5 6 7 8
              r

s = 15
c = 4
"""


def count_sums(n: int) -> int:
    half = (n // 2) + 1
    curr_sum = sums = 1

    l = r = 1
    # O(n/2)
    while r <= half:
        if curr_sum == n:
            sums += 1

        if curr_sum >= n:
            curr_sum -= l
            l += 1
        else:
            r += 1
            curr_sum += r

    return sums


if __name__ == "__main__":
    n = int(input())

    sums = count_sums(n)
    print(sums)
