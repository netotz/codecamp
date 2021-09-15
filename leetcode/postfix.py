import pytest


def eval_postfix(string: str) -> int:
    stack = list()
    for item in string.split():
        if item.isdigit():
            stack.append(item)
        else:
            result = int(eval(item.join(stack)))
            stack = [str(result)]
    return int(stack[0])


@pytest.mark.parametrize(
    ('string', 'result'), (
        ('1 2 + 4 *', 12)
    )
)
def test(string, result):
    assert eval_postfix(string) == result
