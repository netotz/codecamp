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
  find subtree u, O(n)
  count nodes in subtree that are c, O(n)
'''


from collections import deque


class Node: 
  def __init__(self, data: int): 
    self.val: int = data
    self.children: list[Node] = []


def map_tree(root):
    '''
    O(n)
    '''
    treemap = dict()

    curr_lvl = deque([root])
    nxt_lvl = deque()

    while curr_lvl:
        node = curr_lvl.popleft()

        if node.val in treemap:
            continue
        treemap[node.val] = node

        for child in node.children:
            nxt_lvl.append(child)

        if not curr_lvl:
            curr_lvl = nxt_lvl
            nxt_lvl = deque()

    return treemap


def count_nodes(subtree, char, string):
    curr_lvl = deque([subtree])
    nxt_lvl = deque()

    count = 0

    while curr_lvl:
        node = curr_lvl.popleft()

        if string[node.val - 1] == char:
            count += 1

        for child in node.children:
            nxt_lvl.append(child)

        if not curr_lvl:
            curr_lvl = nxt_lvl
            nxt_lvl = deque()

    return count


def count_of_nodes(root, queries, s):    
    # O(n)
    treemap = map_tree(root)

    counts = []
    # O(qn)
    for u, c in queries:
        subtree = treemap[u]
        # O(n)
        count = count_nodes(subtree, c, s)
        counts.append(count)
    return counts

