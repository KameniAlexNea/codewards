# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode()
        res_pos = result

        h1 = l1
        h2 = l2

        retenu = 0
        while (h1 is not None) and (h2 is not None):
            value = h1.val+h2.val+retenu
            retenu = value // 10

            res_pos.next = ListNode(value%10)
            res_pos = res_pos.next

            h1 = h1.next
            h2 = h2.next
        
        h = h1 if h2 is None else h2
        if h is not None:
            while (h is not None):
                value = h.val+retenu
                retenu = value // 10
                res_pos.next = ListNode(value%10)
                
                res_pos = res_pos.next
                h = h.next
        if retenu != 0:
            res_pos.next = ListNode(retenu)

        result = result.next
        return result
