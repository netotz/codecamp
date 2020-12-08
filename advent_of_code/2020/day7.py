import re

def parse_input(rawrules):
    return {
        fl[0]: {} if fl[1] == ''
        else {
            s[2:]: int(s[0])
            for s in fl[1].split(' , ')
        }
        for line in rawrules.splitlines()
        if (fl := [
            s.strip()
            for s in
                re.sub(
                    r'(no other)*|bag(s*)|[.]', '', line
                ).split('contain')
        ])
    }

with open('inputs/input7.txt') as file:
    input7 = parse_input(file.read())

MYBAG = 'shiny gold'

def get_containers(rules):
    containers = set()
    def is_container(bag):
        subbags = set(b for b in rules[bag])
        if containers & subbags or MYBAG in subbags:
            containers.add(bag)
            return True
        for b in subbags:
            if is_container(b):
                containers.add(b)
                return True

    for bag in rules:
        if bag in containers:
            continue
        if is_container(bag):
            containers.add(bag)

    return containers

def count_required(rules):
    def count_subbags(bag):
        subbags = rules[bag].items()
        if not subbags:
            return 0
        local_count = 0
        for b, c in subbags:
            accumulated = count_subbags(b)
            if accumulated == 0:
                local_count += c
            else:
                local_count += accumulated * c
        return local_count + 1

    total_bags = 0
    for bag, count in rules[MYBAG].items():
        total_bags += count_subbags(bag) * count
    return total_bags

answer1 = len(get_containers(input7))
answer2 = count_required(input7)

def test():
    raw = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
        dark orange bags contain 3 bright white bags, 4 muted yellow bags.
        bright white bags contain 1 shiny gold bag.
        muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
        shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
        dark olive bags contain 3 faded blue bags, 4 dotted black bags.
        vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
        faded blue bags contain no other bags.
        dotted black bags contain no other bags.'''
    sample = parse_input(raw)
    assert len(get_containers(sample)) == 4

    assert count_required(sample) == 32
    raw = '''shiny gold bags contain 2 dark red bags.
        dark red bags contain 2 dark orange bags.
        dark orange bags contain 2 dark yellow bags.
        dark yellow bags contain 2 dark green bags.
        dark green bags contain 2 dark blue bags.
        dark blue bags contain 2 dark violet bags.
        dark violet bags contain no other bags.'''
    sample = parse_input(raw)
    assert count_required(sample) == 126
