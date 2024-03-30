# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        odd = head
        even_head = head.next
        even = head.next
        while even is not None and odd.next is not None:
            odd.next = even.next
            if odd.next is not None:
                odd = odd.next
                even.next = odd.next # check none
                even = even.next
        odd.next = even_head
        return head
        