import re
import math

def parse_input(raw):
    return sorted(int(n) for n in raw.splitlines())

with open('inputs/input10.txt') as file:
    input10 = parse_input(file.read())

def get_differences(joltages):
    return [
        j - current
        for j, current in zip(
            joltages + [joltages[-1] + 3],
            [0] + joltages
        )
    ]

def multiply_diffs(differences):
    return differences.count(1) * differences.count(3)

def count_arrangements(differences):
    return math.prod(
        (2 ** (len(m) - 1)) - (len(m) == 4)
        for m in re.findall(
            r'(1+)3',
            ''.join(map(str, differences))
        )
        if len(m) > 1
    )

differences = get_differences(input10)
answer1 = multiply_diffs(differences)
answer2 = count_arrangements(differences)

def test():
    raw = (
        '16\n'
        '10\n'
        '15\n'
        '5\n'
        '1\n'
        '11\n'
        '7\n'
        '19\n'
        '6\n'
        '12\n'
        '4\n'
    )
    sample = parse_input(raw)
    differences = get_differences(sample)
    # print(differences)
    assert multiply_diffs(differences) == 7 * 5
    assert count_arrangements(differences) == 8

    raw = (
        '28\n'
        '33\n'
        '18\n'
        '42\n'
        '31\n'
        '14\n'
        '46\n'
        '20\n'
        '48\n'
        '47\n'
        '24\n'
        '23\n'
        '49\n'
        '45\n'
        '19\n'
        '38\n'
        '39\n'
        '11\n'
        '1\n'
        '32\n'
        '25\n'
        '35\n'
        '8\n'
        '17\n'
        '7\n'
        '9\n'
        '4\n'
        '2\n'
        '34\n'
        '10\n'
        '3\n'
    )
    sample = parse_input(raw)
    differences = get_differences(sample)
    print(differences)
    assert multiply_diffs(differences) == 22 * 10
    assert count_arrangements(differences) == 19208
