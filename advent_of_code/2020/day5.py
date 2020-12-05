with open('inputs/input5.txt') as inputfile:
    input5 = inputfile.read().splitlines()

def get_half_diff(lower, upper):
    return (upper - lower) // 2

def get_seat_id(seat):
    bottomrow, toprow = 0, 127
    for r in seat[:7]:
        if r == 'F':
            toprow = bottomrow + get_half_diff(bottomrow, toprow)
        elif r == 'B':
            bottomrow = toprow - get_half_diff(bottomrow, toprow)

    left, right = 0, 7
    for c in seat[7:]:
        if c == 'L':
            right = left + get_half_diff(left, right)
        elif c == 'R':
            left = right - get_half_diff(left, right)

    return (toprow * 8) + right

def get_max_id(passes):
    return max(get_seat_id(s) for s in passes)

def get_missing_id(passes):
    prev = 0
    for seat_id in sorted((get_seat_id(s) for s in passes)):
        if seat_id == prev + 2:
            return seat_id - 1
        prev = seat_id

answer1 = get_max_id(input5)
answer2 = get_missing_id(input5)

def test():
    sample = 'FBFBBFFRLR'
    assert get_seat_id(sample) == 357
    sample = 'BFFFBBFRRR'
    assert get_seat_id(sample) == 567
    sample = 'FFFBBBFRRR'
    assert get_seat_id(sample) == 119
    sample = 'BBFFBBFRLL'
    assert get_seat_id(sample) == 820
