# https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
    When geting a new node, the key point is keeping a pre_node to link the
    pre_node.next = cur_node.
    And this dummyhead helps to avoid setting the first pre_node to None.
    """
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not (l1 and l2):
            if l1:
                return l1
            elif l2:
                return l2
            else:
                return []

        c = 0
        n1 = l1
        n2 = l2
        dummyhead = ListNode(0)
        pn = dummyhead
        while n1 or n2:
            v1 = n1.val if n1 else 0
            v2 = n2.val if n2 else 0
            s = v1 + v2 + c
            c = s / 10
            pn.next = ListNode(s % 10)
            pn = pn.next
            n1 = n1.next if n1 else None
        if c:
            pn.next = ListNode(c)
        return dummyhead.next
