'''
Reverse Operations
You are given a singly-linked list that contains N integers. A subpart of the list is a contiguous set of even elements, bordered either by either end of the list or an odd element. For example, if the list is [1, 2, 8, 9, 12, 16], the subparts of the list are [2, 8] and [12, 16].
Then, for each subpart, the order of the elements is reversed. In the example, this would result in the new list, [1, 8, 2, 9, 16, 12].
The goal of this question is: given a resulting list, determine the original order of the elements.

Constraints
1 <= N <= 1000, where N is the size of the list
1 <= Li <= 10^9, where Li is the ith element of the list

Example
Input:
N = 6
list = [1, 2, 8, 9, 12, 16]
Output:
[1, 8, 2, 9, 16, 12]
'''


class Node:
  def __init__(self, x):
    self.data = x
    self.next = None


def reverse(head: Node) -> Node:
    '''
    Reverses even sublists in place by changing the pointers of each even node at a time.
    
    Time O(n)
    
    Space O(n)
    '''
    # dummy node to save reference of first node of list
    dummy = Node(-1)
    dummy.next = head

    # previous odd node of current node,
    # default is dummy in case the list starts with an even node
    prev_odd = dummy
    # previous even node of current node
    prev_even = None
    
    current = head
    # O(n)
    while current is not None:
        # if current node is odd
        if current.data % 2 == 1:
            # set current as previous odd node
            prev_odd = current
            # erase track of previous even node, if there was any,
            # as that sublist is irrelevant now
            prev_even = None
            current = current.next
            continue

        # if current node is even and it's the first even of this sublist
        if prev_even is None:
            # set current as previous even node
            prev_even = current
            current = prev_even.next
            continue

        # save reference of first even in this sublist
        first_even = prev_odd.next
        # set previous odd to point to current node
        prev_odd.next = current
        # set previous even to point to next node
        prev_even.next = current.next
        # set current to point to first even node
        current.next = first_even

        current = prev_even.next

    # at the end, dummy points to original list,
    # with even sublists reversed
    return dummy.next
