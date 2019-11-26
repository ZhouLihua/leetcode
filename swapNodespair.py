# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        first = head
        second = head.next
        result = ListNode(-1)
        temp = result
        while first and second:
            temp1 = ListNode(first.val)
            temp2 = ListNode(second.val)
            temp2.next = temp1
            temp.next = temp2
            temp = temp.next.next
            first = first.next.next
            if not first:
                break
            second = second.next.next
        if first:
            temp.next = first
        return result.next


if __name__ == "__main__":
    nodes = [1, 2, 3, 4]
    head = ListNode(nodes[0])
    temp = head
    for node in nodes[1:]:
        temp.next = ListNode(node)
        temp = temp.next

    solution = Solution()
    result = solution.swapPairs(head)
    while result:
        print result.val
        result = result.next