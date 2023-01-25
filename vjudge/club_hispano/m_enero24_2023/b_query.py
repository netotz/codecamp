def read_sequence():
    # read N
    input()
    # O(n)
    return [int(_) for _ in input().split()]


def read_queries():
    # read Q
    total = int(input())

    queries = []
    # O(q)
    for _ in range(total):
        raw = [int(_) for _ in input().split()]

        if len(raw) == 2:
            # x >= 0
            raw.append(-1)

        queries.append(raw)

    return queries


WRITE_QUERY = 1
READ_QUERY = 2


def process_queries(queries, sequence):
    # O(q)
    for query in queries:
        query_type = query[0]
        index = query[1] - 1

        if query_type == WRITE_QUERY:
            value = query[2]
            sequence[index] = value
        elif query_type == READ_QUERY:
            print(sequence[index])


if __name__ == "__main__":
    sequence = read_sequence()
    queries = read_queries()
    process_queries(queries, sequence)
