"""
https://leetcode-cn.com/problems/add-two-numbers/submissions/
两个数相加
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        node = ListNode(-999)
        head = node
        flag = 0
        a = 0
        b = 0
        while l1 or l2 or flag:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0


            node.next = ListNode((a+b + flag) % 10)
            node = node.next
            if a + b + flag >= 10:
                flag = 1
            else:
                flag = 0
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return head.next



if __name__ == "__main__":
    pass