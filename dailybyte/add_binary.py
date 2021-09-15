import pytest


def sum_binary_builtin(binary1: str, binary2: str) -> str:
    int1 = int(binary1, 2)
    int2 = int(binary2, 2)
    return f'{int1 + int2:b}'


def sum_binary_manual(binary1: str, binary2: str) -> str:
    maxlen = max(len(binary1), len(binary2))

    filled_b1 = binary1.zfill(maxlen)
    filled_b2 = binary2.zfill(maxlen)

    result = list()
    remainder = 0
    i = maxlen - 1
    while i >= 0:
        decimal = remainder
        decimal += int(filled_b1[i])
        decimal += int(filled_b2[i])
        result.append(decimal % 2)
        remainder = 0 if decimal < 2 else 1
        i -= 1
    if remainder > 0:
        result.append(1)
    return ''.join(map(str, result[::-1]))


@pytest.mark.parametrize(
    ('func'), (
        sum_binary_builtin,
        sum_binary_manual
    )
)
@pytest.mark.parametrize(
    ('binary1', 'binary2', 'result'), (
        ('100', '1', '101'),
        ('11', '1', '100'),
        ('1', '0', '1'),
        ('11', '11', '110'),
        ('111', '111', '1110')
    )
)
def test(func, binary1, binary2, result):
    assert func(binary1, binary2) == result
