'''
Encrypted Words
You've devised a simple encryption method for alphabetic strings that shuffles the characters in such a way that the resulting string is hard to quickly read, but is easy to convert back into the original string.
When you encrypt a string S, you start with an initially-empty resulting string R and append characters to it as follows:
Append the middle character of S (if S has even length, then we define the middle character as the left-most of the two central characters)
Append the encrypted version of the substring of S that's to the left of the middle character (if non-empty)
Append the encrypted version of the substring of S that's to the right of the middle character (if non-empty)
For example, to encrypt the string "abc", we first take "b", and then append the encrypted version of "a" (which is just "a") and the encrypted version of "c" (which is just "c") to get "bac".
If we encrypt "abcxcba" we'll get "xbacbca". That is, we take "x" and then append the encrypted version "abc" and then append the encrypted version of "cba".

Input
S contains only lower-case alphabetic characters
1 <= |S| <= 10,000

Output
Return string R, the encrypted version of S.

Example 1
S = "abc"
R = "bac"

Example 2
S = "abcd"
R = "bacd"

Example 3
S = "abcxcba"
R = "xbacbca"

Example 4
S = "facebook"
R = "eafcobok"
'''


import pytest


def encrypt(string: str, start: int, end: int) -> list[str]:
    '''
    Encrypts the substring of `string` between indexes `start` and `end`,
    `substring = string[start:end + 1]`.

    O(n), not sure how
    '''
    # if starting index is greater than ending,
    # substring is an empty string,
    # len(substring) == 0
    if start > end:
        return []
    
    # if indexes are equal,
    # substring is just character at start index,
    # len(substring) == 1
    if start == end:
        return [string[start]]

    # encrypted string is list of strings to act as string builder
    encrypted = []
    # midpoint of substring
    midpoint = ((end - start) // 2) + start
    encrypted.append(string[midpoint])

    # add encrypted substring left to midpoint
    encrypted.extend(encrypt(string, start, midpoint - 1))
    # add encrypted substring right to midpoint
    encrypted.extend(encrypt(string, midpoint + 1, end))

    return encrypted


def findEncryptedWord(s: str) -> str:
    return ''.join(encrypt(s, 0, len(s) - 1))


@pytest.mark.parametrize(
    ('string', 'encrypted'), (
        ('abc', 'bac'),
        ('abcd', 'bacd'),
        ('abcxcba', 'xbacbca'),
        ('facebook', 'eafcobok')
    )
)
def test(string, encrypted):
    assert findEncryptedWord(string) == encrypted
