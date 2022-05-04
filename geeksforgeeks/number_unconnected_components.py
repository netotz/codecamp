"""
https://www.geeksforgeeks.org/number-of-connected-components-of-a-graph-using-disjoint-set-union/

do BFS for each node,
mark visited nodes,
for each BFS run increment count
"""


from collections import deque
import pytest


def unionfind(nodes: int, edges: list[list[int]]) -> int:
    """
    time O(e + log n)?
    """

    def find(v: int) -> int:
        curr = v

        # while current it's not parent of itself
        while curr != parents[curr]:
            grandpa = parents[parents[curr]]
            # set grandpa of current to be its new parent
            # path compression
            parents[curr] = grandpa

            curr = parents[curr]

        return curr

    def try_union(u: int, v: int) -> bool:
        # find parents
        up = find(u)
        vp = find(v)

        # if both nodes are in same group
        if up == vp:
            return False

        # add shorter group as child of bigger group
        if sizes[up] > sizes[vp]:
            parents[vp] = up
            sizes[up] += sizes[vp]
        else:
            parents[up] = vp
            sizes[vp] += sizes[up]

        return True

    # O(n)
    parents = [v for v in range(nodes)]
    # O(n)
    sizes = [1] * nodes

    count = nodes
    # O(e)
    for u, v in edges:
        if try_union(u, v):
            count -= 1

    return count


def count_components(nodes: int, edges: list[list[int]]) -> int:
    """
    time O(n + e)

    space O(ne)
    """
    # O(n)
    adjacencies = [[] for _ in range(nodes)]

    # O(e)
    for u, v in edges:
        adjacencies[u].append(v)
        adjacencies[v].append(u)

    visiteds = set()

    def bfs(node: int) -> None:
        queue = deque([node])

        while queue:
            node = queue.popleft()

            # O(n)
            for neighbor in adjacencies[node]:
                if neighbor not in visiteds:
                    queue.append(neighbor)
                    visiteds.add(neighbor)

    count = 0
    # O(n)
    for v in range(nodes):
        if v not in visiteds:
            visiteds.add(v)
            # explore all neighbors, the whole component
            bfs(v)
            count += 1

    return count


@pytest.mark.parametrize("function", [count_components, unionfind])
@pytest.mark.parametrize(
    ("nodes", "edges", "count"),
    [
        (5, [[1, 0], [2, 3], [3, 4]], 2),
        (8, [[1, 0], [0, 2], [3, 5], [3, 4], [6, 7]], 3),
    ],
)
def test(function, nodes, edges, count):
    assert function(nodes, edges) == count
