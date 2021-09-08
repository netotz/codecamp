from typing import List
import sys

import pytest


def get_profit(prices: List[int]) -> int:
    '''
    My first solution.

    It's just getting both max and min values in prices,
    then using them to get their indexes to ensure selling after buying.
    It works but it loops the list twice, plus searching for indexes.

    This takes ~42 ms with 1 million elements.
    '''
    max_price = max(prices)
    max_index = prices.index(max_price)

    min_price = min(prices)
    min_index = prices.index(min_price)
    return max_price - min_price if min_index < max_index else 0


def get_profit_for(prices: List[int]) -> int:
    '''
    Refactored solution from Daily Byte.

    They only use one loop and no need to do extra searching for indexes.

    But oh surprise, this takes ~340 ms with 1 million elements.
    I think this is due getting maxs and mins several times.
    '''
    min_price = sys.maxsize
    profit = 0
    for price in prices:
        if price > min_price:
            profit = max(profit, price - min_price)
        else:
            min_price = min(min_price, price)
    return profit


@pytest.mark.parametrize(
    'prices, profit', [
        ([1, 2, 3, 4, 5], 4),
        ([4, 5, 2, 1, 6, 10, 4, 9, 11], 10),
        ([33, 18, 8, 2], 0),
        ([3, 3, 3, 3, 3], 0)
    ]
)
class Test:
    def test(self, prices, profit):
        assert get_profit(prices) == profit

    def test_for(self, prices, profit):
        assert get_profit_for(prices) == profit
