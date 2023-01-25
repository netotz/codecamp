def can_complete(string: str) -> bool:
    box = set()
    stack = []

    # O(n)
    for i in range(len(string)):
        if string[i] == "(":
            stack.append(i)
            continue

        if string[i] == ")":
            j = stack.pop()
            box = update_box(box, string, j, i)
            continue

        # faints
        if string[i] in box:
            return False

        box.add(string[i])

    return True


def update_box(box: set[int], string: str, j: int, i: int) -> set[int]:
    for k in range(j, i + 1):
        box.discard(string[k])

    return box


if __name__ == "__main__":
    string = input()
    answer = "Yes" if can_complete(string) else "No"
    print(answer)
