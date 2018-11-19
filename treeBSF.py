#! /usr/bin/env python

"""

Interview question:
There is a binary tree, and a parallel beam of light from right
Find all nodes can be lighted.
"""


class Node(object):

    def __init__(self, value, lchld, rchld):
        self.value = value
        self.lchld = lchld
        self.rchld = rchld


def find_lighted_nodes(nodes):
    if len(nodes) == 0:
        return

    print(nodes[0].value)

    nodes_ = list()
    for node in nodes:
        if node.rchld:
            nodes_.append(node.rchld)
        if node.lchld:
            nodes_.append(node.lchld)

    find_lighted_nodes(nodes_)


def create_node(val):
    return Node(val, None, None)


def build_tree():
    # root
    root = create_node(1)

    # level 1
    left = create_node(2)
    right = create_node(3)
    root.lchld = left
    root.rchld = right

    # level 2
    level2_node1 = create_node(4)
    level2_node2 = create_node(5)
    level2_node3 = create_node(6)
    level2_node4 = create_node(7)
    left.lchld = level2_node1
    left.rchld = level2_node2
    right.lchld = level2_node3
    right.rchld = level2_node4

    # level 3
    level3_node1 = create_node(8)
    level3_node2 = create_node(9)
    level3_node3 = create_node(10)
    level2_node1.lchld = level3_node1
    level2_node1.rchld = level3_node2
    level2_node3.lchld = level3_node3

    # level 4
    level4_node1 = create_node(11)
    level3_node1.lchld = level4_node1

    # level 5
    level5_node1 = create_node(12)
    level5_node2 = create_node(13)
    level4_node1.lchld = level5_node1
    level4_node1.rchld = level5_node2

    return root


if __name__ == "__main__":
    rt = build_tree()
    nodes = [rt]
    find_lighted_nodes(nodes)
