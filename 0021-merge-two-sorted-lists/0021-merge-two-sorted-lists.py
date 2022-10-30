# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list2.val < list1.val:
            list1, list2 = list2, list1
        
        res = list1
        while (res is not None):
            while (res.next is not None) and res.next.val <= list2.val:
                res = res.next
            if res.next is None:
                res.next = list2
                res = None
            else:
                res.next, list2 = list2, res.next
        return list1