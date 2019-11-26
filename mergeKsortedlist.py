#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import sys
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        temp = ListNode(-1)
        result = temp
        null_lists = 0
        while lists:
            while null_lists > 0:
                lists.remove(None)
                null_lists -= 1
            min_node = ListNode(sys.maxint)
            order = -1
            for index, node in enumerate(lists):
                if not node:
                    null_lists += 1
                    continue
                if node.val < min_node.val:
                    order, min_node = index, node
            if order != -1:
                temp.next = ListNode(min_node.val)
                temp = temp.next
                lists[order] = lists[order].next

        return result.next
