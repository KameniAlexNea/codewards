# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        start = head
        last = head.next.next
        while last is not None:
            last = last.next
            if last is not None:
                last = last.next
                start = start.next
        start.next = start.next.next
        return head