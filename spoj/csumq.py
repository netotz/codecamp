def solve_query(sums: list[int], query: tuple[int, int]) -> int:
    i, j = query

    return sums[j] - (sums[i - 1] if i > 0 else 0)


def get_cumulative_sum(array: list[int]) -> list[int]:
    sums = []
    curr_sum = 0

    # O(n)
    for i in range(len(array)):
        curr_sum += array[i]
        sums.append(curr_sum)

    return sums


# O(n + q)
if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))

    # O(n)
    sums = get_cumulative_sum(array)

    q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(q)]

    # O(q)
    for query in queries:
        cum_sum = solve_query(sums, query)
        print(cum_sum)
