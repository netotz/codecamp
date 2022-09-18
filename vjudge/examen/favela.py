"""

"""


def get_shots(
    n: int, bottles: int, ml: int, lemons: int, slices: int, grams: int, x: int, y: int
) -> int:
    total_ml = bottles * ml
    ml_shots = total_ml / x

    total_slices = lemons * slices

    grams_shots = grams / y

    return min(ml_shots, total_slices, grams_shots) / n


if __name__ == "__main__":
    n, bottles, ml, lemons, slices, grams, x, y = map(int, input().split())

    shots = get_shots(n, bottles, ml, lemons, slices, grams, x, y)
    print(int(shots))
