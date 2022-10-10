# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import merge

def get_list(l_nodes):
    node = l_nodes
    while node is not None:
        yield node.val
        node = node.next

def list_to_nodelist(l: List):
    head = ListNode()
    pos = head
    for i in l:
        pos.next = ListNode(i)
        pos = pos.next
    return head.next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Brute force implementation
        """
        solution = merge(
            *[list(get_list(l)) for l in lists if isinstance(l, ListNode)]
        )
        return list_to_nodelist(solution)