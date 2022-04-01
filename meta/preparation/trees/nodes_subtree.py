'''
Nodes in a Subtree
You are given a tree that contains N nodes, each containing an integer u which corresponds to a lowercase character c in the string s using 1-based indexing.
You are required to answer Q queries of type [u, c], where u is an integer and c is a lowercase letter. The query result is the number of nodes in the subtree of node u containing c.
Signature
int[] countOfNodes(Node root, ArrayList<Query> queries, String s)
Input
A pointer to the root node, an array list containing Q queries of type [u, c], and a string s
Constraints
N and Q are the integers between 1 and 1,000,000
u is a unique integer between 1 and N
s is of the length of N, containing only lowercase letters
c is a lowercase letter contained in string s
Node 1 is the root of the tree
Output
An integer array containing the response to each query
Example
        1(a)
        /   \
      2(b)  3(a)
s = "aba"
RootNode = 1
query = [[1, 'a']]
Note: Node 1 corresponds to first letter 'a', Node 2 corresponds to second letter of the string 'b', Node 3 corresponds to third letter of the string 'a'.
output = [2]
Both Node 1 and Node 3 contain 'a', so the number of nodes within the subtree of Node 1 containing 'a' is 2.
---

n nodes,
each node contains index of a char in s, 1-based
no empty tree, queries

no repeated chars?

for every query (u,c), O(q)
    find subtree u using BFS, O(n)
    count nodes in subtree that are c using BFS, O(n)
total of O(qn)

every query, 2 traversals of the tree is done.
this is repeated work because several nodes would be visited several times,
in both finding a subtree and counting nodes.
to improve this we can use a hashmap to store tree's data by traversing it once before processing the queries.
the key would be the node's index and the value the string of that subtree:
e.g. hashmap = {
    1: "aba",
    2: "b",
    3: "a"
}

map tree using DFS, O(n)
for every query (u, c), O(q)
    count char c in hashmap[u], O(n)

still worst case of O(qn).
this is still doing duplicated work because when counting nodes, the string of the subtree is being traversed.
we can take advantage of the pre-exploration of the tree and store the characters count of the subtree, instead of its string.
the value of the hashmap would be then another hashmap whose keys are the characters and values are their count:
e.g. hashmap = {
    1: {
        a: 2,
        b: 1
    },
    2: {b: 1},
    3: {a: 1},
}

map tree and count chars using DFS, O(n)
for every query (u, c), O(q)
    access count of char c in hashmap[u], O(1)
reducing the time complexity to O(n + q), but adding space complexity of O(n)
'''


from collections import defaultdict

import pytest


class Node: 
  def __init__(self, data: int): 
    self.val: int = data
    self.children: list[Node] = []


def count_of_nodes(root, queries, s):
    '''
    Time O(n + q)

    Space O(n)
    '''

    def map_subtree(node: Node, treemap, string: str):
        '''
        Recursive DFS.

        Time O(n)
        '''
        index = node.val - 1
        char = string[index]
        charsmap = defaultdict(int)
        charsmap[char] = 1
        
        for child in node.children:
            treemap = map_subtree(child, treemap, string)
            
            # O(26) = O(1)
            for char in treemap[child.val]:
                charsmap[char] += treemap[child.val][char]
        
        treemap[node.val] = charsmap
        return treemap

    # O(n)
    treemap = map_subtree(root, dict(), s)

    # O(q)
    return [treemap[u][c] for u, c in queries]

'''
n = 1
tm = {}
cm = {a: 1}
    n = 2
    tm = {}
    cm = {b: 1}
    tm = {2: {b: 1}}
cm = {a: 1, b: 1}
    n = 3
    tm = {2: {b: 1}}
    cm = {a: 1}
    tm = {2: {b: 1}, 3: {a: 1}}
cm = {a: 2, b: 1}
tm = {2: {b: 1}, 3: {a: 1}, 1: {a: 2, b: 1}}

u, c = 1, a
count = tm[1][a] = 2
'''


s_1 = "aba"
root_1 = Node(1) 
root_1.children.append(Node(2)) 
root_1.children.append(Node(3)) 
queries_1 = [(1, 'a')]
expected_1 = [2]

s_2 = "abaacab"
root_2 = Node(1)
root_2.children.append(Node(2))
root_2.children.append(Node(3))
root_2.children.append(Node(7))
root_2.children[0].children.append(Node(4))
root_2.children[0].children.append(Node(5))
root_2.children[1].children.append(Node(6))
queries_2 = [[1, 'a'],[2, 'b'],[3, 'a']]
expected_2 = [4, 1, 2]


@pytest.mark.parametrize(
    ('root', 'queries', 'string', 'counts'), [
        (root_1, queries_1, s_1, expected_1),
        (root_2, queries_2, s_2, expected_2)
    ]
)
def test(root, queries, string, counts):
    assert count_of_nodes(root, queries, string) == counts
