def parse_input(raw):
    return raw.splitlines()

with open('inputs/input11.txt') as file:
    input11 = parse_input(file.read())


def check_adjacent_occupieds(seats, i, j):
    occupieds = 0
    indexes = range(-1, 2, 1)
    for r in indexes:
        for c in indexes:
            if r == c == 0:
                continue
            try:
                if (x := i + r) >= 0 and (y := j + c) >= 0 and seats[x][y] == '#':
                    occupieds += 1
            except IndexError:
                continue
    return occupieds


def move_people(seats):
    newseats = list(seats)
    for i in range(len(seats)):
        for j in range(len(seats[0])):
            occupieds = check_adjacent_occupieds(seats, i, j)
            if seats[i][j] == 'L' and occupieds == 0:
                newseats[i] = newseats[i][:j] + '#' + newseats[i][j + 1:]
            elif seats[i][j] == '#' and occupieds >= 4:
                newseats[i] = newseats[i][:j] + 'L' + newseats[i][j + 1:]
    return newseats


def count_occupieds(seats):
    return sum(seat == '#' for seat in ''.join(seats))


def solve1(seats):
    while True:
        prev = list(seats)
        seats = move_people(seats)
        if seats == prev:
            return count_occupieds(seats)


answer1 = solve1(input11)


def test():
    raw = (
        'L.LL.LL.LL\n'
        'LLLLLLL.LL\n'
        'L.L.L..L..\n'
        'LLLL.LL.LL\n'
        'L.LL.LL.LL\n'
        'L.LLLLL.LL\n'
        '..L.L.....\n'
        'LLLLLLLLLL\n'
        'L.LLLLLL.L\n'
        'L.LLLLL.LL\n'
    )
    sample = parse_input(raw)
    assert solve1(sample) == 37
