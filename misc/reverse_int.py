# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.

x = input()
rev = f'-{x[:0:-1]}' if x[0] == '-' else x[::-1]
print(rev)
