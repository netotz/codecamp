def can_distribute(a: int, b: int, c: int, n: int) -> bool:
    """
    time O(1)

    space O(1)
    """
    max_coins = max(a, b, c)
    x = max_coins - a
    y = max_coins - b
    z = max_coins - c

    remainder = n - x - y - z
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
