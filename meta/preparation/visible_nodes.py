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
# worst case it's a linked list where max depth = n.


from dataclasses import dataclass
import pytest


@dataclass
class TreeNode:
    val: int
    left: 'TreeNode' = None
    right: 'TreeNode' = None


def explore_tree(
        node: TreeNode,
        right_nodes: list[TreeNode],
        right_levels: list[int],
        max_level: int,
        level: int,
        is_back: bool) -> int:
    '''
    Explores one of the subtrees of `node` to count
    the left-most node of each level.

    O(n) because it halves the current tree each time,
    so it "visits" each node once.
    '''
    # if node has left child and it's first time
    if node.left and not is_back:
        # push only the right child of node to the stack,
        # to jump directly to it after its sibling subtree is explored
        if node.right:
            right_nodes.append(node.right)
            # push level of right node too to another stack
            # to keep track of its depth
            right_levels.append(level + 1)

        node = node.left
        level += 1
        is_back = False
    # if node has right child
    elif node.right:
        node = node.right
        level += 1
        is_back = False
    # if node doesn't have children
    else:
        # if there's no right node to explore,
        if len(right_nodes) == 0:
            # then tree has been fully explored,
            # visible nodes from left equal the tree's depth
            return max_level + 1
        
        # jump to last right node to explore its subtree
        node = right_nodes.pop()
        level = right_levels.pop()
        is_back = True

    if not is_back and level > max_level:
        max_level = level
    
    # explore left subtree of node
    return explore_tree(
        node,
        right_nodes,
        right_levels,
        max_level,
        level,
        is_back
    )


def visible_nodes(root: TreeNode) -> int:
    return explore_tree(root, [], [], 0, 0, False)


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
    ('root', 'count'), (
        (root_1, 4),
        (root_2, 5),
        (root_2, 5),
        (linked_list, 3)
    )
)
def test(root: TreeNode, count: int) -> None:
    assert visible_nodes(root) == count
