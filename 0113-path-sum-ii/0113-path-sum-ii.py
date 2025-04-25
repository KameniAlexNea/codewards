# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def pathSumRecursive(root, targetSum, start, curr):
    if root.left is None and root.right is None and root.val + start == targetSum:
        yield curr + [root.val]
    curr = curr + [root.val]
    if root.left is not None:
        yield from pathSumRecursive(root.left, targetSum, start + root.val, curr )
    if root.right is not None:
        yield from pathSumRecursive(root.right, targetSum, start + root.val, curr )
    

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        return list(pathSumRecursive(root, targetSum, 0, []))