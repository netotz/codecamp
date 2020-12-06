from functools import reduce

def parse_input(plane_answers):
    groups_answers = []
    append = groups_answers.append
    group = []
    for line in plane_answers:
        if line == '':
            append(group)
            group = []
        else:
            group += [line.strip()]
    return groups_answers

with open('inputs/input6.txt') as inputfile:
    content = inputfile.read().splitlines()
    input6 = parse_input(content)

def count_any_yeses(groups):
    return sum(
        len(set(''.join(g)))
        for g in groups
    )

def count_every_yeses(groups):
    return sum(
        len(reduce(lambda p1, p2: set(p1) & set(p2), g))
        for g in groups
        if g
    )

answer1 = count_any_yeses(input6)
answer2 = count_every_yeses(input6)

def test():
    raw = '''
        abc

        a
        b
        c

        ab
        ac

        a
        a
        a
        a

        b


    '''
    sample = parse_input(raw.splitlines())
    assert count_any_yeses(sample) == 11
    assert count_every_yeses(sample) == 6
