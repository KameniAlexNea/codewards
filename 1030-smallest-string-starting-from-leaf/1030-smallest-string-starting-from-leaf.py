# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def smallest(root, curr):
    curr = chr(ord('a') + root.val) + curr
    if root.left is None and root.right is None:
        return curr
    left, right = None, None
    if root.left is not None:
        left = smallest(root.left, curr)
        if root.right is None:
            return left
    if root.right is not None:
        right = smallest(root.right, curr)
        if root.left is None:
            return right
    return min(left, right)


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        return smallest(root, "")
