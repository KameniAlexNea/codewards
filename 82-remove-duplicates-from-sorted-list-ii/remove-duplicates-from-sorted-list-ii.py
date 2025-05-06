# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        result = head

        while head is not None and head.next is not None and head.next.val == head.val:
            curr = head.next
            while curr is not None and curr.val == head.val:
                curr = curr.next
            head = curr
        
        result = head
        if result is None:
            return

        prev = head
        head = head.next
        while head is not None:
            curr = head.next
            flag = False
            while curr is not None and curr.val == head.val:
                curr = curr.next
                flag = True
            if flag:
                head = curr
                prev.next = curr
                flag = False
            else:
                head.next = curr
                prev = head
                head = head.next
        return result