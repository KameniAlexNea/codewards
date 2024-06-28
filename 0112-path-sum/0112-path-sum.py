# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def sumTarget(node, curr, target):
    curr += node.val
    if node.left is None and node.right is None:
        return curr == target
    left = sumTarget(node.left, curr, target) if node.left is not None else False
    if not left:
        left = sumTarget(node.right, curr, target) if node.right is not None else False
    return left

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ltr = root
        if root is None:
            return False
        return sumTarget(ltr, 0, targetSum)