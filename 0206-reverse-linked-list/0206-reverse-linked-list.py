# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        s = head
        n = head.next
        while n is not None:
            tmp, n.next = n.next, s
            s, n = n, tmp
        head.next = None
        return s
        