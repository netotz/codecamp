def parse_input(raw_input):
    return [
        # strip multiline strings when testing
        [line.strip() for line in group.split('\n')]
        for group in raw_input.split('\n\n')
    ]

with open('inputs/input6.txt') as file:
    input6 = parse_input(file.read())

def count_any_yeses(groups):
    return sum(
        len(set(''.join(g)))
        for g in groups
    )

def count_every_yeses(groups):
    return sum(
        len(set.intersection(*(set(p) for p in g)))
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
    sample = parse_input(raw)
    assert count_any_yeses(sample) == 11
    assert count_every_yeses(sample) == 6
