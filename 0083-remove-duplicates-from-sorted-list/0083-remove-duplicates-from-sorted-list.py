# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node is not None:
            node_n = node.next
            while (node_n is not None) and node_n.val == node.val:
                node_n = node_n.next
            node.next = node_n
            node = node.next
        return head