from typing import Iterable


def detect_repeated(array: Iterable, number_to_detect: int, min_repetitions: int) -> bool:
    return sum(n == number_to_detect for n in array) >= min_repetitions


def test():
    sample = [4, 5, 2, 4, 5, 9, 9, 4, 4]
    assert not detect_repeated(sample, 4, 5)
    assert detect_repeated(sample, 4, 4)
    assert detect_repeated(sample, 4, 3)
    assert detect_repeated(sample, 9, 2)