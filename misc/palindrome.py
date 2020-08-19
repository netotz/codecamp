# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
# The string will only contain lowercase characters a-z.

def valid_palindrome(string):
    for i in range(len(string)):
        p = string[:i] + string[i+1:]
        if p == p[::-1]:
            return True
    return string == string[::-1]

print(valid_palindrome(input()))
