'''
https://leetcode.com/problems/binary-tree-right-side-view/
'''


import collections
from dataclasses import dataclass

import pytest


@dataclass
class TreeNode:
    val: int
    left: 'TreeNode' = None
    right: 'TreeNode' = None


def level_order_traverse(root: TreeNode) -> list[int]:
    '''
    Does an iterative BFS level-order traversal to `root` from left to right,
    and returns the visible nodes from the right.

    O(n) time

    O(n) space
    '''
    # edge case, if tree is empty
    if root is None:
        return []

    # queue of nodes in current level,
    # starting with the root
    current_level_queue = collections.deque([root])
    # queue of nodes in next level
    next_level_queue = collections.deque()

    visible_node_values = []

    while len(current_level_queue) > 0:
        # current node is first from current queue
        node = current_level_queue.popleft()

        # enqueue node's children, if any, in this order
        if node.left:
            next_level_queue.append(node.left)
        if node.right:
            next_level_queue.append(node.right)

        # if there are no more nodes in current level
        # then current node is its last one,
        # in this case the right-most one too
        # because it's a left to right traversal
        if len(current_level_queue) == 0:
            # swap queues to start visiting next level
            current_level_queue = next_level_queue
            next_level_queue = collections.deque()
            
            visible_node_values.append(node.val)
    
    return visible_node_values


def recursive_dfs(root: TreeNode) -> int:
    '''
    Does a recursive DFS starting with left child subtree.

    O(n) time

    O(n) space
    '''
    # edge case, if tree is empty
    if root is None:
        return []

    visible_node_values = []

    def add_rightmost(node: TreeNode, level: int) -> None:
        '''
        Adds `node` to `visible_node_values` list if it's the right-most node in `level`.
        '''
        # if level is greater than count of visible nodes from upper levels,
        # it means that current node is the first visited one of that level,
        # since the count of visible nodes is the depth of the tree
        if level > len(visible_node_values):
            visible_node_values.append(node.val)

        # explore right subtree first, if exists
        if node.right:
            add_rightmost(node.right, level + 1)
        # then left subtree, if exists
        if node.left:
            add_rightmost(node.left, level + 1)

    add_rightmost(root, 1)
    return visible_node_values


root_1 = TreeNode(1)
root_1.left = TreeNode(2)
root_1.right = TreeNode(3)
root_1.left.right = TreeNode(5)
root_1.right = TreeNode(3)
root_1.right.right = TreeNode(4)

root_2 = TreeNode(8)
root_2.left = TreeNode(3)
root_2.right = TreeNode(10)
root_2.left.left = TreeNode(1)
root_2.left.right = TreeNode(6)
root_2.left.right.left = TreeNode(4)
root_2.left.right.right = TreeNode(7)
root_2.right.right = TreeNode(14)
root_2.right.right.left = TreeNode(13)

root_3 = TreeNode(1)
root_3.right = TreeNode(3)

root_4 = None

@pytest.mark.parametrize(
    ('method'), (
        level_order_traverse,
        recursive_dfs
    )
)
@pytest.mark.parametrize(
    ('root', 'nodes'), (
        (root_1, [1, 3, 4]),
        (root_2, [8, 10, 14, 13]),
        (root_3, [1, 3]),
        (root_4, [])
    )
)
def test(method, root: TreeNode, nodes: list[int]) -> None:
    assert method(root) == nodes
