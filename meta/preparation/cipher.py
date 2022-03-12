'''
Rotational Cipher
One simple way to encrypt a string is to "rotate" every alphanumeric character by a certain amount. Rotating a character means replacing it with another character that is a certain number of steps away in normal alphabetic or numerical order.
For example, if the string "Zebra-493?" is rotated 3 places, the resulting string is "Cheud-726?". Every alphabetic character is replaced with the character 3 letters higher (wrapping around from Z to A), and every numeric character replaced with the character 3 digits higher (wrapping around from 9 to 0). Note that the non-alphanumeric characters remain unchanged.
Given a string and a rotation factor, return an encrypted string.

Input
1 <= |input| <= 1,000,000
0 <= rotationFactor <= 1,000,000

Output
Return the result of rotating input a number of times equal to rotationFactor.
'''


import pytest


def rotate_char(char_code: int, set_min: int, set_max: int, rotation_factor: int) -> str:
    '''
    Rotates an ASCII character given the set it belongs to (lowercase, uppercase, or digits).

    O(1)
    '''
    # code of character within its set
    set_code = char_code - set_min
    # lenght of set is the difference of max and min indexes, plus 1
    # because first index is 0 !!
    set_length = abs(set_max - set_min) + 1
    # rotated code of char but within its set
    set_rotated = (set_code + rotation_factor) % set_length
    # rotated code of char in ASCII !!
    rotated_code = set_rotated + set_min
    return chr(rotated_code)


def rotationalCipher(input: str, rotation_factor: int) -> str:
    '''
    O(n)
    '''
    # use list as a string builder
    output = list()
    # use dictionary to store ciphered chars and not having to rotate them again
    rotated_chars = dict()

    # O(n)
    for character in input:
        if character in rotated_chars:
            output.append(rotated_chars[character])
            continue

        char_code = ord(character)

        UPPERCASE_MIN = ord('A')
        UPPERCASE_MAX = ord('Z')

        LOWERCASE_MIN = ord('a')
        LOWERCASE_MAX = ord('z')

        DIGIT_MIN = ord('0')
        DIGIT_MAX = ord('9')

        set_min = 0
        set_max = 0
        if UPPERCASE_MIN <= char_code <= UPPERCASE_MAX:
            set_min = UPPERCASE_MIN
            set_max = UPPERCASE_MAX
        elif LOWERCASE_MIN <= char_code <= LOWERCASE_MAX:
            set_min = LOWERCASE_MIN
            set_max = LOWERCASE_MAX
        elif DIGIT_MIN <= char_code <= DIGIT_MAX:
            set_min = DIGIT_MIN
            set_max = DIGIT_MAX
        else:
            output.append(character)
            continue

        rotated_char = rotate_char(char_code, set_min, set_max, rotation_factor)
        rotated_chars[character] = rotated_char
        output.append(rotated_char)

    return ''.join(output)


@pytest.mark.parametrize(
    ('original', 'rotation', 'encrypted'), (
        ('Zebra-493?', 3, 'Cheud-726?'),
        ('abcdefghijklmNOPQRSTUVWXYZ0123456789', 39, 'nopqrstuvwxyzABCDEFGHIJKLM9012345678'),
        ("All-convoYs-9-be:Alert1.", 4, "Epp-gsrzsCw-3-fi:Epivx5."),
        ("abcdZXYzxy-999.@", 200, "stuvRPQrpq-999.@")
    )
)
def test(original, rotation, encrypted):
    assert rotationalCipher(original, rotation) == encrypted
