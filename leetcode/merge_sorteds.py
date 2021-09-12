from typing import Optional


class ListNode:
    '''
    Definition for singly-linked list.
    '''
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_sorted(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = current = ListNode()
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return dummy.next
