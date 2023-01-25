from asyncore import read


def read_input() -> list[list[int]]:
    return [list(map(int, input().split())) for _ in range(5)]


def beautify(matrix: list[list[int]]) -> int:
    n = len(matrix)

    row = col = -1
    # find coord of number
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                row = i
                col = j
                break

    return abs(row - 2) + abs(col - 2)


if __name__ == "__main__":
    matrix = read_input()
    print(beautify(matrix))
