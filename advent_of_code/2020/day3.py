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

def ref_count_trees(mymap, right, down):
    '''
    Refactored solutions, all of them are slower.
    '''
    pos = 0
    trees = 0
    for line in mymap[down::down]:
        pos = (pos + right) % len(line)
        trees += line[pos] == '#'
    return trees

    trees = 0
    for i, line in enumerate(mymap[down::down]):
        pos = ((i + 1) * right) % len(line)
        trees += line[pos] == '#'
    return trees

    pos = 0
    return sum(
        # walrus operator (:=) in Python >= 3.8
        line[(pos := (pos + right) % len(line))] == '#'
        for line in mymap[down::down]
    )

    return sum(
        line[((i + 1) * right) % len(line)] == '#'
        for i, line in enumerate(mymap[down::down])
    )

def count_trees(mymap, right, down):
    '''
    Used to solve the puzzle.
    '''
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
