#/usr/bin/env python

"Print nodes in a tree in Inorder, don't use recursion"
"""
            1
        2       3
      4    5  7    8
          6
"""

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def walk(root):
    stack = []
    _push_left_nodes(root,stack)
    while stack:
        node = stack.pop()
        print node.value
        if node.right:
            _push_left_nodes(node.right, stack)


def _push_left_nodes(root, stack):
    while root:
        stack.append(root)
        root = root.left


def build_data():
    root = Node(1)
    left = Node(2)
    right = Node(3)
    root.left = left
    root.right = right

    left1 = Node(4)
    right1 = Node(5)
    left.left = left1
    left.right = right1

    left2 = Node(7)
    right2 = Node(8)
    right.left = left2
    right.right = right2

    left3 = Node(6)
    right1.left = left3

    return root


if __name__ == "__main__":
    root = build_data()
    walk(root)
