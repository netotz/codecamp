from dataclasses import dataclass
from typing import Optional

import pytest


@dataclass
class Node:
    value: int
    nxt: Optional['Node'] = None


def reverse(head: Optional[Node]) -> Optional[Node]:
    '''
    T = O(n)
    S = O(1)
    '''
    prev = None
    while head:
        current = head
        head = head.nxt
        current.nxt = prev
        prev = current
    return prev


def reverse_recursively(head: Optional[Node]) -> Optional[Node]:
    '''
    T = O(n)
    S = O(n)
    '''
    if not head or not head.nxt:
        return head
    newhead = reverse_recursively(head.nxt)
    head.nxt.nxt = head
    # new tail
    head.nxt = None
    return newhead
