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

# TODO: review solution


from dataclasses import dataclass


@dataclass
class TreeNode:
    label: str
    children: list['TreeNode'] = None

roots = []

def add_node(node: TreeNode, labels: list[str]) -> None:
    if len(labels) == 0:
        return
    
    current_label = labels[0]
    # was_found = False
    # O(c) -> O(1)
    for child in node.children:
        if child.label == current_label:
            # was_found = True
            add_node(child, labels[1:])

    # if not was_found:
    new_child = TreeNode(current_label)
    node.children.append(new_child)
    add_node(new_child, labels[1:])


def build_tree(route: str) -> None:
    routes = route.split('/')
    current_node = None
    for root in roots:
        if root.label == routes[0]:
            current_node = root
    if current_node is None:
        current_node = TreeNode(routes[0])
        roots.append(current_node)

    labels = routes[1:]
    add_node(current_node, labels)
    
    # for r in routes:
        
# list of n strings
# each string is a route, r labels
# O(nrc)
