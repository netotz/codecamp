# Given an array containing None values fill in the None values with most recent 
# non None value in the array

from random import random

def generate_sample(n):
    rand = 0.9
    while n:
        yield int(rand * 10) if rand % 1 > 1 / 3 else None
        rand = random()
        n -= 1

def fill1(array):
    for i in range(len(array)):
        if array[i] is None:
            array[i] = array[i - 1]
    return array

def fill2(array):
    for i, num in enumerate(array):
        if num is None:
            array[i] = array[i - 1]
    return array

test = list(map(int, input().split()))
print(fill1(test))
print(fill2(test))
