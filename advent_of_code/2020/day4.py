from functools import reduce
from operator import xor
from string import hexdigits

# yes I need to learn regex
VALIDATIONS = {
    'byr': lambda y: 1920 <= int(y) <= 2002,
    'iyr': lambda y: 2010 <= int(y) <= 2020,
    'eyr': lambda y: 2020 <= int(y) <= 2030,
    'hgt': lambda h:
        150 <= int(h[:-2]) <= 193 if h[-2:] == 'cm'
        else (59 <= int(h[:-2]) <= 76 if h[-2:] == 'in' else False),
    'hcl': lambda c:
        len(c) == 7 and c[0] == '#' and all(
            x in hexdigits
            for x in c[1:]
        ),
    'ecl': lambda c:
        reduce(
            xor,
            (c == x for x in 'amb blu brn gry grn hzl oth'.split())
        ),
    'pid': lambda i: len(i) == 9 and i.isnumeric()
}

def parse_input(data):
    parsed_data  = []
    append = parsed_data.append
    passport = []
    for line in data:
        if line == '':
            append(passport)
            passport = []
            continue
        passport += line.split() if ' ' in set(line) else [line]
    return parsed_data

def is_complete(passport):
    pfields = ' '.join(pf[:3] for pf in passport)
    return all(pfields.find(f) >= 0 for f in VALIDATIONS)

def is_complete_valid(passport):
    fields_valid = [
        VALIDATIONS[pf[:3]](pf[4:])
        for pf in passport
        if pf[:3] != 'cid'
    ]
    return len(fields_valid) == 7 and all(fields_valid)

def count_completes(batchfile):
    return sum(is_complete(p) for p in batchfile)

def count_valids(batchfile):
    return sum(is_complete_valid(p) for p in batchfile)

with open('input4.txt') as inputfile:
    content = inputfile.read().splitlines()
    input4 = parse_input(content)

answer1 = count_completes(input4)
answer2 = count_valids(input4)

# problems:
# part 1: EOF blank line
# part 2: regex

def test():
    raw = '''
        ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
        byr:1937 iyr:2017 cid:147 hgt:183cm

        iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
        hcl:#cfa07d byr:1929

        hcl:#ae17e1 iyr:2013
        eyr:2024
        ecl:brn pid:760753108 byr:1931
        hgt:179cm

        hcl:#cfa07d eyr:2025 pid:166559648
        iyr:2011 ecl:brn hgt:59in


    '''
    sample = parse_input(raw.splitlines())
    assert count_completes(sample) == 2

    assert VALIDATIONS['byr'](2002)
    assert not VALIDATIONS['byr'](2003)

    assert VALIDATIONS['hgt']('60in')
    assert VALIDATIONS['hgt']('190cm')
    assert not VALIDATIONS['hgt']('190in')
    assert not VALIDATIONS['hgt']('190')

    assert VALIDATIONS['hcl']('#123abc')
    assert not VALIDATIONS['hcl']('#123abz')
    assert not VALIDATIONS['hcl']('123abc')

    assert VALIDATIONS['ecl']('brn')
    assert not VALIDATIONS['ecl']('wat')

    assert VALIDATIONS['pid']('000000001')
    assert not VALIDATIONS['pid']('0123456789')

    raw = '''
        eyr:1972 cid:100
        hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

        iyr:2019
        hcl:#602927 eyr:1967 hgt:170cm
        ecl:grn pid:012533040 byr:1946

        hcl:dab227 iyr:2012
        ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

        hgt:59cm ecl:zzz
        eyr:2038 hcl:74454a iyr:2023
        pid:3556412378 byr:2007


    '''
    invalids = parse_input(raw.splitlines())
    assert count_valids(invalids) == 0

    raw = '''
        pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
        hcl:#623a2f

        eyr:2029 ecl:blu cid:129 byr:1989
        iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

        hcl:#888785
        hgt:164cm byr:2001 iyr:2015 cid:88
        pid:545766238 ecl:hzl
        eyr:2022

        iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719


    '''
    valids = parse_input(raw.splitlines())
    assert count_valids(valids) == 4
