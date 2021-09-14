import pytest

def is_palindrome(string: str) -> bool:
    cleaned_str = string.lower()
    i = 0
    j = len(cleaned_str) - 1
    while i < j:
        if not cleaned_str[i].isalpha():
            i += 1
            continue
        if not cleaned_str[j].isalpha():
            j -= 1
            continue
        if cleaned_str[i] != cleaned_str[j]:
            return False
        i += 1
        j -= 1
    return True

@pytest.mark.parametrize(
    ('string', 'is_it'), (
        ('level', True),
        ('algorithm', False),
        ('A man, a plan, a canal: Panama.', True),
        ('Anita lava la tina.', True),
        ('palíndromo', False),
        # is an empty string a palindrome?
        # I'd say it is
        ('', True),
        (' ', True)
    )
)
def test(string, is_it):
    assert is_palindrome(string) == is_it
