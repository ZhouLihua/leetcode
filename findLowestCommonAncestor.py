#! /usr/bin/env python

"""
microsoft interview question, find the lowest common ancesstor of two nodes in
a binary tree.
"""

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def find_path_to_node(root, node, path):
    if not root:
        return False

    path.append(root.value)
    if root.value == node.value:
        return True
    
    found = False
    if not found and root.left:
        # find from left child
        found = find_path_to_node(root.left, node, path)

    if  not found and root.right:
        # find from right child
        found = find_path_to_node(root.right, node, path)

    if not found:
        path.pop()
    return found


def min(x, y):
    if x >= y:
        return y
    return x


def find_lowest_common_ancestor(root, node1, node2):
    path_node1 = []
    path_node2 = []
    find_path_to_node(root, node1, path_node1)
    find_path_to_node(root, node2, path_node2)
    print path_node1
    print path_node2
    index = 0
    for i in range(0, min(len(path_node1), len(path_node2))):
        if path_node1[i] != path_node2[i]:
            index = i-1
            break
        else:
            index = i

    return path_node1[index]

def create_tree():
    root = Node(1)
    left1 = Node(3)
    right1 = Node(2)
    root.left = left1
    root.right = right1

    left21 = Node(4)
    right21 = Node(5)
    left1.left = left21
    left1.right = right21

    left22 = Node(6)
    right22 = Node(8)
    right1.left = left22
    right1.right = right22

    left31 = Node(7)
    right21.left = left31
    return root


if __name__ == "__main__":
    root = create_tree()
    node1 = Node(4)
    node2 = Node(1)
    print find_lowest_common_ancestor(root, node1, node2)
