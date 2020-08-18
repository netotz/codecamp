# Given a string, find the first non-repeating character in it and return its index.
# If it doesn't exist, return -1. # Note: all the input strings are already lowercase.

def count_method(string):
    index = -1
    for char in string:
        if string.count(char) == 1:
            return string.find(char)

print(count_method(input()))

# using Counter

from collections import Counter

def counter_obj(string):
    index = -1
    for key, value in Counter(string).items():
        if value == 1:
            return string.find(key)

print(counter_obj(input()))
