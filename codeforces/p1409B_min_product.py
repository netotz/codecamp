"""
minimize a*b = minimize a and/or b by decrementing any or both at most n times
if at least 1 decrement, a >= x & b >= y
"""


def get_min_product(a: int, b: int, x: int, y: int, n: int) -> int:
    # cannot decrement
    if a == x and b == y:
        return a * b

    max_var = max(a, b)
    max_lim = x if max_var == a else y
    min_var = min(a, b)
    min_lim = x if min_var == a else y

    diff = min(max_var - min_var, max_var - max_lim, n)
    max_var -= diff
    n -= diff


if __name__ == "__main__":
    pass
