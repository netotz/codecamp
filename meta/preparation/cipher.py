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


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
  print('[\"', string, '\"]', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  input_1 = "All-convoYs-9-be:Alert1."
  rotation_factor_1 = 4
  expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
  output_1 = rotationalCipher(input_1, rotation_factor_1)
  check(expected_1, output_1)

  input_2 = "abcdZXYzxy-999.@"
  rotation_factor_2 = 200
  expected_2 = "stuvRPQrpq-999.@"
  output_2 = rotationalCipher(input_2, rotation_factor_2)
  check(expected_2, output_2)


import pytest


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
