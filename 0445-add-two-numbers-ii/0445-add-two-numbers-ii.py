# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    r = 1
    s = head
    n = head.next
    while n is not None:
        tmp, n.next = n.next, s
        s, n = n, tmp
        r += 1
    head.next = None
    return s, r

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None or l2 is None:
            return
        l1, r1 = reverseList(l1)
        l2, r2 = reverseList(l2)

        if r2 > r1:
            l1, l2 = l2, l1

        head = l1
        r = 0
        while l2 is not None:
            v = head.val + l2.val + r
            head.val, r = v % 10, v // 10
            head, l2 = head.next, l2.next
        if r:
            while r and head is not None:
                v = head.val + r
                head.val, r, head = v % 10, v // 10, head.next
            if head is None and r:
                head = ListNode(r)
                head.next = reverseList(l1)[0]
                return head
        return reverseList(l1)[0]
