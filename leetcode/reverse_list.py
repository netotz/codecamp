from dataclasses import dataclass
from typing import Optional

import pytest


@dataclass
class Node:
    value: int
    nxt: Optional['Node'] = None


def reverse(head: Optional[Node]) -> Optional[Node]:
    prev = None
    while head:
        current = head
        head = head.nxt
        current.nxt = prev
        prev = current
    return prev
