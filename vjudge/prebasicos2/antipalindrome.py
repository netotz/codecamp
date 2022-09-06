"""
first check if s is palindrome
if it's not, return len(s)
if it is, remove any of the 2 edge chars

when checking if s is palindrome, also check if it's same char
if it is, return 0
"""


def is_palindrome(string: str) -> tuple[bool, bool]:
    n = len(string)
    l = 0
    r = n - 1

    is_same_char = True
    char = string[0]
    # O(n)
    while l <= r:
        if string[l] != char or string[r] != char:
            is_same_char = False

        if string[l] != string[r]:
            return (False, False)

        l += 1
        r -= 1

    return (True, is_same_char)


def count_max_substring(string: str) -> int:
    is_p, is_same_char = is_palindrome(string)

    if not is_p:
        return len(string)

    if is_same_char:
        return 0

    return len(string) - 1


if __name__ == "__main__":
    s = input()

    answer = count_max_substring(s)
    print(answer)
