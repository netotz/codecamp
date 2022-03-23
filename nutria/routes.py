'''
given a list of routes:

animal/reptile/lizard
plant/tree/cherry
animal/feline/tiger
animal/canine/wolf
animal/lizard
plant/tree/pine
human/paul

provide the best data structure to parse and store these routes.
'''

from dataclasses import dataclass, field


@dataclass
class TreeNode:
    label: str
    children: dict[str, 'TreeNode'] = field(init=False, default_factory=dict)


def add_node(node: TreeNode, labels: list[str], index: int) -> None:
    if index == len(labels):
        return
    
    current_label = labels[index]

    child = None
    if current_label in node.children:
        child = node.children[current_label]
    else:
        child = TreeNode(current_label)
        node.children[current_label] = child

    add_node(child, labels, index + 1)


def build_trees(routes: list[str]) -> TreeNode:
    '''
    Time O(n), where n is the total number of labels.
    '''
    trees = TreeNode('')
    
    # O(r)
    for route in routes:
        labels = route.split('/')
        # O(l)
        add_node(trees, labels, 0)
    
    return trees


# each row is a route, each word is a label
inputs = [
    'animal/reptile/lizard',
    'plant/tree/cherry',
    'animal/feline/tiger',
    'animal/canine/wolf',
    'animal/lizard',
    'plant/tree/pine',
    'human/paul',
]
