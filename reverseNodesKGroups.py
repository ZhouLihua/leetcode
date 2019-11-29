"""
https://leetcode.com/problems/reverse-nodes-in-k-group/
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        result = ListNode(-1)
        temp = result
        n = 0
        k_nodes = []
        while head:
            k_nodes.append(head)
            head = head.next
            n += 1
            if n % k == 0:
                for node in k_nodes[-1::-1]:
                    node.next = None
                    temp.next = node
                    temp = temp.next
                k_nodes = []
        if k_nodes:
            for node in k_nodes:
                temp.next = node
                temp = temp.next

        return result.next



if __name__ == "__main__":
    solution = Solution()
    # fake assert
    assert solution.reverseKGroup([1, 2, 3, 4, 5], 2) == [2, 1, 4, 3, 5]
    assert solution.reverseKGroup([1, 2, 3, 4, 5], 3) == [3, 2, 1, 4, 5]


