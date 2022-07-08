"""
https://leetcode.com/problems/graph-valid-tree/ (premium)
https://leetcode.ca/2016-08-17-261-Graph-Valid-Tree/

build adjacency list, O(e)
do DFS, O(n)
    mark each node as visited
    visit each neighbor and send current as previous or parent,
    to avoid visiting previous node

    if a node is already visited, there's a cycle, no valid tree

total time O(e + n)

5, [[0, 1], [0, 2], [0, 3], [1, 4]]
a = [
    0: 1,
    1: 0, 2, 3, 4
    2: 1, 3
    3: 1, 2
    4: 1
]
v = {0, 1, 2, 3}
n = 0
p = -1
    n = 1
    p = 0
        n = 2
        p = 1
            n = 3
            p = 2
            
"""


import pytest


def is_valid_tree(n: int, edges: list[list[int]]) -> bool:
    """
    time O(e + n)

    space O(n)
    """
    # an empty graph or a single node are a valid tree
    if (n == 0 and not edges) or n == 1:
        return True

    # build adjacency list
    adjacencies = [[] for _ in range(n)]
    # O(e)
    for u, v in edges:
        adjacencies[u].append(v)
        adjacencies[v].append(u)

    visiteds = set()

    def is_acyclic(node, prev):
        """
        Recursive DFS, checks if graph is acyclic.
        """
        if node in visiteds:
            return False

        visiteds.add(node)

        for neighbor in adjacencies[node]:
            if neighbor != prev and not is_acyclic(neighbor, node):
                return False

        return True

    return (
        # a valid tree is acyclic
        is_acyclic(0, -1)
        # if the number of visited nodes doesn't match n,
        # then there are disconnected, unvisited nodes
        and len(visiteds) == n
    )


@pytest.mark.parametrize(
    ("n", "edges", "is_it"),
    [
        (5, [[0, 1], [0, 2], [0, 3], [1, 4]], True),
        (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], False),
    ],
)
def test(n, edges, is_it):
    assert is_valid_tree(n, edges) == is_it
