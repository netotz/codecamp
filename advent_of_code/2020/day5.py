with open('inputs/input5.txt') as inputfile:
    input5 = inputfile.read().splitlines()

def get_half_diff(lower, upper):
    return (upper - lower) / 2

def get_seat_id(seat):
    '''
    Used to solve the puzzle.
    '''
    bottomrow, toprow = 0, 127
    for r in seat[:7]:
        delta = get_half_diff(bottomrow, toprow)
        if r == 'F':
            toprow -= delta
        elif r == 'B':
            bottomrow += delta

    left, right = 0, 7
    for c in seat[7:]:
        delta = get_half_diff(left, right)
        if c == 'L':
            right -= delta
        elif c == 'R':
            left += delta

    return (int(toprow) * 8) + int(right)

def ref_get_seat_id(seat):
    '''
    Refactored, faster, and better solution.
    This is my understanding:

    Every seat ID is determined by a unique string of FBLR.
    There are 128 rows (2 ** 7) and the first 7 characters specify the row.
    There are 8 columns (2 ** 3) and the last 3 characters specify the column.
    There are 1024 total seats (2 ** 10) and the string length is 10.
    If F and L are replaced with 0, because they represent the lower halfs,
    and B and R with 1, because they represent the upper halfs,
    then each seat ID is given by one of the binary numbers from 0 to 1023.
    That's why the formula is (8 * row) + column.
    '''
    return int(
        seat.translate(seat.maketrans('FBLR', '0101')),
        base=2
    )

def get_max_id(passes):
    return max(get_seat_id(s) for s in passes)

def get_missing_id(passes):
    '''
    Used to solve puzzle.
    '''
    prev = 0
    for seat_id in sorted((get_seat_id(s) for s in passes)):
        if seat_id == prev + 2:
            return seat_id - 1
        prev = seat_id

def ref_get_missing_id(passes):
    '''
    Refactored, faster and better solution.

    The sum of IDs as if they were all occupied,
    minus the sum of actual occupied IDs,
    will result in the one missing ID.
    '''
    ids = [ref_get_seat_id(s) for s in passes]
    min_id, max_id = min(ids), max(ids)
    return ((len(ids) + 1) * (min_id + max_id)) // 2 - sum(ids)

answer1 = get_max_id(input5)
answer2 = get_missing_id(input5)

def test():
    sample = 'FBFBBFFRLR'
    assert get_seat_id(sample) == 357
    assert ref_get_seat_id(sample) == 357
    sample = 'BFFFBBFRRR'
    assert get_seat_id(sample) == 567
    assert ref_get_seat_id(sample) == 567
    sample = 'FFFBBBFRRR'
    assert get_seat_id(sample) == 119
    assert ref_get_seat_id(sample) == 119
    sample = 'BBFFBBFRLL'
    assert get_seat_id(sample) == 820
    assert ref_get_seat_id(sample) == 820
