'''
Given a  string, write a method that returns true if the string is a valid number or false otherwise. Only integers and decimals should be considered as valid. In other words, only characters allowed are digits, "-" and ".". The string can be very long (think millions of characters) and no built-in function/class can handle it without overflowing or losing precision.

a '-' can only be at the beginning
expect digits,
    if there's a 0 at beginning,
        expect end of string,
            if '-', false
        or dot,
        or false
if no digits, false

expect one optional dot,
    if end of string, false
after dot,
    if there's a 0 at beginning,
        if there are zeroes after and end of string, false
    expect digits,
        if 0 and end of string, false

if is other char, false

s = "-13.5", true
s = "-.", false
s = "8.1000", false
s = "001", false

O(n)
'''


import pytest


def is_valid(string: str) -> bool:
    if not string:
        return False
    
    minus_seen = False
    dot_seen = False
    nums_seen = False
    decimals_seen = False
    is_first_zero = False
    is_last_zero = False
    # O(n)
    for i in range(len(string)):
        if string[i] == '-':
            if i > 0:
                return False
            minus_seen = True
        elif string[i] == '.':
            if dot_seen or not nums_seen:
                return False
            dot_seen = True
        elif '0' <= string[i] <= '9':
            if is_first_zero and not dot_seen:
                return False

            if string[i] == '0':
                if not nums_seen:
                    is_first_zero = True
                elif decimals_seen:
                    is_last_zero = True
            else:
                if is_last_zero:
                    is_last_zero = False

            if dot_seen:
                decimals_seen = True
            else:
                nums_seen = True
        else:
            return False
    
    if (is_first_zero and minus_seen) or is_last_zero:
        return False

    if minus_seen and not nums_seen:
        return False
    
    if dot_seen and not decimals_seen:
        return False

    return True


@pytest.mark.parametrize(
    ('string', 'valid'), [
        ("13", True),
        ("3.0", True),
        ("-7.4", True),
        ("-13.5", True),
        ("abc", False),
        ("123a", False),
        ("-.", False),
        ("-", False),
        (".", False),
        ("001", False),
        ("00", False),
        (".8", False),
        ("8.", False),
        ("8.0", True),
        ("8.000", False),
        ("8.001", True),
        ("8.1000", False),
        ("-..--", False),
        ("1.0.0.1", False),
        ("-0", False),
        ("", False),
        ("   ", False),
        ("---", False),
        ("123.321", True)
    ]
)
def test(string, valid):
    assert is_valid(string) == valid
