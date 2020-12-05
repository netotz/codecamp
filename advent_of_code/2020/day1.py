from itertools import combinations
from math import prod

def solve(entries, repeat):
    for comb in combinations(entries, repeat):
        if sum(comb) == 2020:
            return prod(comb)

def get_input():
    with open('inputs/input1.txt') as inputfile:
        return map(int, inputfile.read().splitlines())

answer1 = solve(get_input(), 2)
answer2 = solve(get_input(), 3)

def test():
    sample = [1721, 979, 366, 299, 675, 1456]
    assert solve(sample, 2) == 514579
    assert solve(sample, 3) == 241861950
