def is_hello(word: str) -> bool:
    HELLO = "hello"
    j = 0

    # O(n)
    for i in range(len(word)):
        if word[i] == HELLO[j]:
            j += 1
            if j == len(HELLO):
                return True

    return False


if __name__ == "__main__":
    word = input()

    answer = "YES" if is_hello(word) else "NO"
    print(answer)
