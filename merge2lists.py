# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        cur1 = l1
        cur2 = l2
        result = None
        temp = None
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                if not result:
                    result = ListNode(cur1.val)
                    temp = result
                else:
                    result.next = ListNode(cur1.val)
                    result = result.next
                cur1 = cur1.next
            else:
                if not result:
                    result = ListNode(cur2.val)
                    temp = result
                else:
                    result.next = ListNode(cur2.val)
                    result = result.next
                cur2 = cur2.next
        if cur1:
            result.next = cur1
        if cur2:
            result.next = cur2
        return temp



if __name__ == "__main__":
    l1 = [1, 2, 4]
    l2 = [1, 3, 4]
    head1 = ListNode(l1[0])
    cur1 = head1
    for node in l1[1:]:
        temp = ListNode(node)
        cur1.next = temp
        cur1 = cur1.next
    head2 = ListNode(l2[0])
    cur2 = head2
    for node in l2[1:]:
        temp = ListNode(node)
        cur2.next = temp
        cur2 = cur2.next

    # p1 = head1
    # while p1:
    #     print p1.val
    #     p1 = p1.next
    #
    # p2 = head2
    # while p2:
    #     print p2.val
    #     p2 = p2.next

    solution = Solution()
    l3 = solution.mergeTwoLists(head1, head2)
    while l3:
        print l3.val
        l3 = l3.next
