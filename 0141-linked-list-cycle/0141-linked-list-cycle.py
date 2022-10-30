# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if (head is None) or head.next is None:
            return False
        
        behind = head
        front = head
        while (behind.next is not None) and (front.next.next is not None):
            behind = behind.next
            front = front.next.next
            if behind == front:
                return True
            if (front is None) or (front.next is None):
                return False
        return False