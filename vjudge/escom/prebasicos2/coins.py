"""
12 4 1
12 6 3 1
24 12 6 3 1
9 
"""


def get_denoms(n: int) -> list[int]:
    if n == 1:
        return [1]

    denom = n
    denoms = []
    fraction = 2
    while denom > 1:
        if denom % fraction != 0:
            fraction += 1

            if fraction > n:
                break

            continue

        denoms.append(denom)
        denom //= fraction

    denoms.append(1)
    return denoms


if __name__ == "__main__":
    n = int(input())
    denoms = get_denoms(n)

    answer = " ".join(map(str, denoms))
    print(answer)
