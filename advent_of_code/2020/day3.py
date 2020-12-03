from math import prod

SLOPES = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

with open('input3.txt') as inputfile:
    input3 = inputfile.read().splitlines()

def count_trees(mymap, right, down):
    trees = 0
    pos = 0
    linelen = len(mymap[0])
    for line in mymap[down::down]:
        pos += right
        if pos > linelen - 1:
            pos -= linelen
        if line[pos] == '#':
            trees += 1
    return trees

def multiply_counts(mymap, slopes):
    return prod(count_trees(mymap, r, d) for r, d in slopes)

answer1 = count_trees(input3, 3, 1)
answer2 = multiply_counts(input3, SLOPES)

def test():
    sample = [
        '..##.......',
        '#...#...#..',
        '.#....#..#.',
        '..#.#...#.#',
        '.#...##..#.',
        '..#.##.....',
        '.#.#.#....#',
        '.#........#',
        '#.##...#...',
        '#...##....#',
        '.#..#...#.#'
    ]
    assert count_trees(sample, 3, 1) == 7
    assert multiply_counts(sample, SLOPES) == 336
