# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = head
        low = head
        i = 0
        while fast and i < n + 1:
            fast = fast.next
            i += 1
        # there are totally less than n nodes
        if i < n:
            return head
        if i == n:
            return head.next
        while fast:
            fast = fast.next
            low = low.next
        print low.val
        if low.next and low.next.next:
            low.next = low.next.next
        else:
            low.next = None
        return head


if __name__ == "__main__":
    head = ListNode(1)
    cur = head
    nodes = [2, 3, 4, 5]
    for node in nodes:
        temp = ListNode(node)
        cur.next = temp
        cur = cur.next
    # while head:
    #     print head.val
    #     head = head.next

    solution = Solution()
    result = solution.removeNthFromEnd(head, 2)
    while result:
        print result.val
        result = result.next