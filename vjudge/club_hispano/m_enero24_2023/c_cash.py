def count_keystrokes(target: str):
    total = len(target)

    i = 1
    # O(n)
    while i < len(target):
        if target[i] == "0" and target[i - 1] == "0":
            total -= 1
            i += 1

        i += 1

    return total


if __name__ == "__main__":
    target = input()
    answer = count_keystrokes(target)
    print(answer)
