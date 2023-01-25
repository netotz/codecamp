def power(a: int, b: int):
    result = 1

    for _ in range(b):
        result *= a

    return result


if __name__ == "__main__":
    a, b = map(int, input().split(" "))
    answer = power(a, b)
    print(answer)
