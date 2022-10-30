# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node = head
        if node is None:
            return head
        while (node is not None) and node.val == val:
            node = node.next
        head = node
        
        while node is not None:
            while (node.next is not None) and node.next.val != val:
                node = node.next
            
            node_n = node.next
            while (node_n is not None) and node_n.val == val:
                node_n = node_n.next
            
            if node_n is None:
                node.next = None
                node = None
            else:
                node.next = node_n
                node = node.next
                node_n = node
        return head