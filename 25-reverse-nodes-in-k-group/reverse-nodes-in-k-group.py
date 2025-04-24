# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse_nodes(prev: ListNode, head: ListNode, k):
	i = 1
	n1 = head
	n2 = head.next
	while i < k:
		temp = n2
		n2 = n2.next if n2 is not None else None
		temp.next = n1
		n1 = temp
		i += 1
	head.next = n2
	prev.next = n1
	return head, n2

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        start = ListNode(0, head)
        prev = start
        curr = head
        while curr:
            i = 0
            h = curr
            while i < k and h is not None:
                i += 1
                h = h.next
            if i < k:
                return start.next
            prev, curr = reverse_nodes(prev, curr, k)
        return start.next
