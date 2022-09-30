
from codewards.ListNodeSum.code import ListNode, Solution


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

def compare_solution(pred: ListNode, target: ListNode):
    pos_err = 0
    while pred is not None and target is not None:
        assert pred.val == target.val, 'Error at %d' % pos_err
        pred = pred.next
        target = target.next
    assert (pred is None) and (target is None), "Still some elements"

def test_case0():
    l1 = list_to_list_node([2,4,3])
    l2 = list_to_list_node([5,6,4])

    result1 = Solution().addTwoNumbers(l1, l2)
    result2 = Solution().addTwoNumbers(l2, l1)

    expected_list = [7,0,8]
    compare_solution(result1, list_to_list_node(expected_list))
    compare_solution(result2, list_to_list_node(expected_list))

def test_case1():
    l1 = list_to_list_node([0])
    l2 = list_to_list_node([0])

    result1 = Solution().addTwoNumbers(l1, l2)
    result2 = Solution().addTwoNumbers(l2, l1)

    expected_list = [0]
    compare_solution(result1, list_to_list_node(expected_list))
    compare_solution(result2, list_to_list_node(expected_list))
    
def test_case2():
    l1 = list_to_list_node([9,9,9,9,9,9,9])
    l2 = list_to_list_node([9,9,9,9])

    result1 = Solution().addTwoNumbers(l1, l2)
    result2 = Solution().addTwoNumbers(l2, l1)

    expected_list = [8,9,9,9,0,0,0,1]
    compare_solution(result1, list_to_list_node(expected_list))
    compare_solution(result2, list_to_list_node(expected_list))