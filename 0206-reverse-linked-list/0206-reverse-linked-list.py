# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        if node is None:
            return head
        if node.next is None:
            return head
        
        node_n = node.next
        node.next = None
        while node_n is not None:
            tmp = node_n.next
            node_n.next = node
            node = node_n
            node_n = tmp
        return node