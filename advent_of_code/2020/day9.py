def parse_input(raw):
    return [int(n) for n in raw.splitlines()]

with open('inputs/input9.txt') as file:
    input9 = parse_input(file.read())

def check_sum(preamble, number):
    for p in preamble:
        dif = number - p
        if dif != p and dif in preamble:
            return True

def get_first_invalid(data, length):
    i = 0
    while (j := i + length) < len(data):
        preamble = data[i:j]
        number = data[j]
        if not check_sum(set(preamble), number):
            return number
        i += 1

def get_weakness(data, invalid):
    contiguous = list()
    are_found = False
    i = 0
    while True:
        contiguous.append(data[i])
        csum = sum(contiguous)
        if csum == invalid:
            are_found = True
        elif csum > invalid:
            j = 1
            while True:
                contiguous = contiguous[j:]
                tsum = sum(contiguous)
                if tsum == invalid:
                    are_found = True
                    break
                if tsum < invalid:
                    break
                j += 1
        if are_found:
            return min(contiguous) + max(contiguous)
        i += 1

answer1 = get_first_invalid(input9, 25)
answer2 = get_weakness(input9, answer1)

def test():
    raw = (
        '35\n'
        '20\n'
        '15\n'
        '25\n'
        '47\n'
        '40\n'
        '62\n'
        '55\n'
        '65\n'
        '95\n'
        '102\n'
        '117\n'
        '150\n'
        '182\n'
        '127\n'
        '219\n'
        '299\n'
        '277\n'
        '309\n'
        '576'
    )
    sample = parse_input(raw)
    assert get_first_invalid(sample, 5) == 127
    assert get_weakness(sample, 127) == 62
