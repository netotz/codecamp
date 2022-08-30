"""
https://codeforces.com/problemset/problem/1294/A
"""


def can_distribute(a: int, b: int, c: int, n: int) -> bool:
    """
    time O(1)

    space O(1)
    """
    max_coins = max(a, b, c)

    # differences to match amounts to max amount
    a_diff = max_coins - a
    b_diff = max_coins - b
    c_diff = max_coins - c

    remainder = n - a_diff - b_diff - c_diff
    return remainder >= 0 and remainder % 3 == 0


def main():
    cases = int(input())

    while cases > 0:
        a, b, c, n = map(int, input().split())

        answer = "YES" if can_distribute(a, b, c, n) else "NO"
        print(answer)

        cases -= 1


if __name__ == "__main__":
    main()
