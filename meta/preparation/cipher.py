import string
import pytest


def get_rotated_char(original_char: str, collection: str, rotation_factor: int) -> str:
    # O(c)
    position = collection.find(original_char)
    rotated_position = (position + rotation_factor) % len(collection)
    return collection[rotated_position]


def rotationalCipher(input: str, rotation_factor: int) -> str:
    output = ''
    rotated_chars = dict()
    # O(nc)
    for character in input:
        if character in rotated_chars:
            output += rotated_chars[character]
            continue

        collection = ''
        if character in string.ascii_lowercase:
            collection = string.ascii_lowercase
        elif character in string.ascii_uppercase:
            collection = string.ascii_uppercase
        elif character in string.digits:
            collection = string.digits
        # character is not alphanumeric
        else:
            output += character
            continue

        rotated_char = get_rotated_char(character, collection, rotation_factor)
        rotated_chars[character] = rotated_char
        output += rotated_char

    return output


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