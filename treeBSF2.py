#! /usr/bin/env python

"""
Search a binary tree broad first
"""

# Queue module name changed from Queue to queue
try:
    from Queue import Queue
except ImportError:
    from queue import Queue


class Node(object):

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def create_node(val):
    return Node(val, None, None)


def no_recurse_BSF(queue):
    """
    recurse walk through the binary tree
    :return: 
    """
    if queue.empty():
        return 
    while not queue.empty():
        # from left to right
        node = queue.get()
        print(node.value)
        if node.left:
            queue.put(node.left)
        if node.right:
            queue.put(node.right)


def recurse_BSF(queue):
    if queue.empty():
        return
    queue_ = Queue()
    while not queue.empty():
        # from right to left
        node = queue.get()
        print(node.value)
        if node.right:
            queue_.put(node.right)
        if node.left:
            queue_.put(node.left)
    recurse_BSF(queue_)


def build_tree():
    # root
    root = create_node(1)

    # level 1
    left = create_node(2)
    right = create_node(3)
    root.left = left
    root.right = right

    # level 2
    level2_node1 = create_node(4)
    level2_node2 = create_node(5)
    level2_node3 = create_node(6)
    level2_node4 = create_node(7)
    left.left = level2_node1
    left.right = level2_node2
    right.left = level2_node3
    right.right = level2_node4

    # level 3
    level3_node1 = create_node(8)
    level3_node2 = create_node(9)
    level3_node3 = create_node(10)
    level2_node1.left = level3_node1
    level2_node1.right = level3_node2
    level2_node3.left = level3_node3

    # level 4
    level4_node1 = create_node(11)
    level3_node1.left = level4_node1

    # level 5
    level5_node1 = create_node(12)
    level5_node2 = create_node(13)
    level4_node1.left = level5_node1
    level4_node1.right = level5_node2

    return root


if __name__ == "__main__":
    root = build_tree()
    queue_ = Queue()
    queue_.put(root)
    # no_recurse_BSF(queue_)
    recurse_BSF(queue_)





