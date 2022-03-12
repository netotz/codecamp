import pytest


def count_contiguous(arr: list[int], base_index: int, contiguous_range: range) -> int:
    count = 0
    # O(n)
    for j in contiguous_range:
        if arr[base_index] >= arr[j]:
            count += 1
        else:
            break
    
    return count


def count_subarrays(arr: list[int]) -> list[int]:
    subarrays_number = [0 for _ in arr]
    # O(n**2)
    for i in range(len(arr)):
        count = 1
        count += count_contiguous(arr, i, range(i + 1, len(arr)))
        count += count_contiguous(arr, i, range(i - 1, -1, -1))
        subarrays_number[i] = count
    
    return subarrays_number


@pytest.mark.parametrize(
    ('array', 'subarrays_number'), (
        ([3, 4, 1, 6, 2], [1, 3, 1, 5, 1]),
        ([2, 4, 7, 1, 5, 3], [1, 2, 6, 1, 3, 1])
    )
)
def test(array, subarrays_number):
    assert count_subarrays(array) == subarrays_number
