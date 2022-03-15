'''
Number of Visible Nodes
There is a binary tree with N nodes. You are viewing the tree from its left side and can see only the leftmost nodes at each level. Return the number of visible nodes.
Note: You can see only the leftmost nodes, but that doesn't mean they have to be left nodes. The leftmost node at a level could be a right node.

Input
The root node of a tree, where the number of nodes is between 1 and 1000, and the value of each node is between 0 and 1,000,000,000

Output
An int representing the number of visible nodes.

Example
            8  <------ root
           / \\
         3    10
        / \     \\
       1   6     14
          / \    /
         4   7  13            
output = 4
'''

# the problem is basically asking for the maximum depth of the tree.
# worst case it's a linked list where depth = n.


import collections
from dataclasses import dataclass

import pytest


@dataclass
class TreeNode:
    val: int
    left: 'TreeNode' = None
    right: 'TreeNode' = None


def level_order_traverse(root: TreeNode) -> int:
    '''
    Does an iterative BFS level-order traversal to `root` from right to left,
    and returns its depth.
    
    O(n) time

    O(n) space
    '''
    # queue of nodes in current level,
    # starting with the root
    current_level_queue = collections.deque([root])
    # queue of nodes in next level
    next_level_queue = collections.deque()

    depth = 0
    while len(current_level_queue) > 0:
        # current node is first from current queue
        node = current_level_queue.popleft()

        # enqueue node's children, if any, in this order
        if node.right:
            next_level_queue.append(node.right)
        if node.left:
            next_level_queue.append(node.left)

        # if there are no more nodes in current level
        # then current node is its last one,
        # in this case the left-most one too
        # because it's a right to left traversal
        if len(current_level_queue) == 0:
            # swap queues to start visiting next level
            current_level_queue = next_level_queue
            next_level_queue = collections.deque()
            
            depth += 1
    
    return depth


def get_max_depth(root: TreeNode) -> int:
    '''
    O(2n)? = O(n) time

    O(n) space
    '''
    if root is None:
        return 0
    
    return max(
        get_max_depth(root.left) + 1,
        get_max_depth(root.right) + 1
    )


def get_max_depth_2(root: TreeNode) -> int:
    '''
    O(2n) = O(n) time

    O(n) space
    '''
    if root is None:
        return 0
    
    depth = 0
    depth = max(depth, get_max_depth_2(root.left) + 1)
    depth = max(depth, get_max_depth_2(root.right) + 1)
    return depth


root_1 = TreeNode(8)
root_1.left = TreeNode(3)
root_1.right = TreeNode(10)
root_1.left.left = TreeNode(1)
root_1.left.right = TreeNode(6)
root_1.left.right.left = TreeNode(4)
root_1.left.right.right = TreeNode(7)
root_1.right.right = TreeNode(14)
root_1.right.right.left = TreeNode(13)

root_2 = TreeNode(10)
root_2.left = TreeNode(8)
root_2.right = TreeNode(15)
root_2.left.left = TreeNode(4)
root_2.left.left.right = TreeNode(5)
root_2.left.left.right.right = TreeNode(6)
root_2.right.left =TreeNode(14)
root_2.right.right = TreeNode(16)

root_3 = TreeNode(8)
root_3.left = TreeNode(3)
root_3.right = TreeNode(10)
root_3.left.left = TreeNode(1)
root_3.left.right = TreeNode(6)
root_3.left.right.left = TreeNode(4)
root_3.left.right.right = TreeNode(7)
root_3.right.right = TreeNode(14)
root_3.right.right.left = TreeNode(13)
root_3.right.right.left.right = TreeNode(21)

linked_list = TreeNode(0)
linked_list.right = TreeNode(1)
linked_list.right.right = TreeNode(2)


@pytest.mark.parametrize(
    ('method'), (
        level_order_traverse,
        get_max_depth,
        get_max_depth_2
    )
)
@pytest.mark.parametrize(
    ('root', 'count'), (
        (root_1, 4),
        (root_2, 5),
        (root_2, 5),
        (linked_list, 3)
    )
)
def test(method, root: TreeNode, count: int) -> None:
    assert method(root) == count
