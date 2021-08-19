"""
https://leetcode.com/problems/rotate-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head, k):
        if not head:
            return head

        length = 1
        fast = head
        slow = head
        while fast.next:
            length += 1
            fast = fast.next

        rotate = k % length
        i = 1
        while i < length - rotate:
            slow = slow.next
            i += 1

        fast.next = head
        head = slow.next
        slow.next = None

        return head


if __name__ == '__main__':
    solution = Solution()
    print solution.rotateRight([1, 2, 3, 4, 5], 2)
