# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not isinstance(head, ListNode):
            return head
        first_a = head
        first_b = head.next
        if first_b is not None:
            return head
        first_a.next = first_b.next
        first_b.next = first_a
        head = first_b
        first_b = first_a
        if first_b.next is None:
            return head
        second_a = first_b.next
        if second_a.next is None:
            return head
        second_b = second_a.next
        while second_b is not None:
            second_a.next = second_b.next
            second_b.next = second_a

            first_b.next = second_b
            first_b = second_a

            # move to next next second_a and second_b
            second_a = second_a.next
            if second_a is not None:
                second_b = second_a.next
            else:
                second_b = None
        return head
        
def list_to_list_node(l: list):
    result = ListNode()
    head = result
    for i in l:
        head.next = ListNode(i)
        head = head.next
    return result.next

def list_node_to_list(l: ListNode):
    result=[]
    while l is not None:
        result.append(l.val)
        l = l.next
    return result

if __name__ == "__main__":
    head = list_to_list_node([1, 2, 3, 4, 5, 6])
    print(list_node_to_list(Solution().swapPairs(head)))