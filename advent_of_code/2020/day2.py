def is_valid(line, part):
    line = line.split()
    policy = [int(_) for _ in line[0].split('-')]
    letter = line[1][0]
    password = line[2]

    if part == 1:
        return policy[0] <= password.count(letter) <= policy[1]

    return sum(password.find(letter, p - 1) == p - 1 for p in policy) == 1

def solve(lines, part):
    valids = (is_valid(l, part) for l in lines)
    return sum(valids)

with open('inputs/input2.txt') as inputfile:
    input2 = inputfile.read().splitlines()

answer1 = solve(input2, 1)
answer2 = solve(input2, 2)

def test():
    sample = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
    assert solve(sample, 1) == 2
    assert solve(sample, 2) == 1
