from typing import List

import pytest


def get_profit(prices: List[int]) -> int:
    max_price = max(prices)
    max_index = prices.index(max_price)

    min_price = min(prices)
    min_index = prices.index(min_price)
    return max_price - min_price if min_index < max_index else 0

@pytest.mark.parametrize(
    'prices, profit', [
        ([1, 2, 3, 4, 5], 4),
        ([4, 5, 2, 1, 6, 10, 4, 9, 11], 10),
        ([33, 18, 8, 2], 0),
        ([3, 3, 3, 3, 3], 0)
    ]
)
def test(prices: List[int], profit: int) -> None:
    assert get_profit(prices) == profit
