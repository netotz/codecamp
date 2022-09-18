def get_longest_steak(n: int, moneys: list[int]) -> int:
    longest = curr = 1

    # O(n)
    for i in range(1, n):
        if moneys[i] >= moneys[i - 1]:
            curr += 1
            longest = max(longest, curr)
        else:
            curr = 1

    return longest


if __name__ == "__main__":
    n = int(input())
    # O(n)
    moneys = list(map(int, input().split()))

    longest = get_longest_steak(n, moneys)
    print(longest)
