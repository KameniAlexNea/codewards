# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSymmetricRec(left, right):
    if left is None and right is None:
        return True
    if (left is None and right is not None) or (left is not None and right is None):
        return False
    left_check = (left.val == right.val) and isSymmetricRec(left.left, right.right)
    if not left_check:
        return False
    return isSymmetricRec(left.right, right.left)

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return isSymmetricRec(root.left, root.right)