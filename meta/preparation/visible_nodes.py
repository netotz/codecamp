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


from dataclasses import dataclass
import pytest


@dataclass
class TreeNode:
    val: int
    left: 'TreeNode' = None
    right: 'TreeNode' = None


def explore_tree(
        node: TreeNode,
        explored_nodes: list[TreeNode],
        explored_levels: list[int],
        max_level: int,
        level: int,
        count: int,
        is_back: bool) -> int:
    '''
    Explores one of the subtrees of `node` to count
    the left-most node of each level.

    O(n) because it halves the current tree each time,
    so it "visits" each node once.
    '''
    # if node has left child and it's first time
    if node.left and not is_back:
        # add only right child to stacks so node won't be visited again
        if node.right:
            explored_nodes.append(node.right)
            explored_levels.append(level + 1)

        node = node.left
        level += 1
        is_back = False
    # if node has right child
    elif node.right:
        node = node.right
        level += 1
        is_back = False
    # if node don't have children
    else:
        # if stack is empty
        if len(explored_nodes) == 0:
            # then tree has been fully explored
            return count
        
        # go back to last node to explore right subtree
        node = explored_nodes.pop()
        level = explored_levels.pop()
        is_back = True
    
    # if current level is maximum depth yet
    if not is_back and level > max_level:
        max_level = level
        count += 1
    
    return explore_tree(
        node,
        explored_nodes,
        explored_levels,
        max_level,
        level,
        count,
        is_back
    )


def visible_nodes(root) -> int:
    return explore_tree(root, [], [], 0, 0, 1, False)


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


@pytest.mark.parametrize(
    ('root', 'count'), (
        (root_1, 4),
        (root_2, 5),
        (root_2, 5)
    )
)
def test(root, count):
    assert visible_nodes(root) == count
