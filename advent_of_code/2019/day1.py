def get_fuel(mass):
    return int(mass / 3) - 2

def get_total_fuel(fuel):
    adds = []
    append = adds.append
    while True:
        fuel = get_fuel(fuel)
        if fuel > 0:
            append(fuel)
        else:
            return sum(adds)

def solve1(modules):
    return sum(get_fuel(m) for m in modules)

def solve2(modules):
    return sum(get_total_fuel(m) for m in modules)

def get_input():
    with open('input1.txt') as file:
        return map(int, file.read().splitlines())

answer1 = solve1(get_input())
answer2 = solve2(get_input())

def test():
    mass1 = 1969
    mass2 = 100756
    assert get_fuel(mass1) == 654
    assert get_fuel(mass2) == 33583
    assert get_total_fuel(mass1) == 966
    assert get_total_fuel(mass2) == 50346
