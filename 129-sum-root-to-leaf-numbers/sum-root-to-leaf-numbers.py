# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def compute_score(root, curr):
    if root.left is None and root.right is None:
        return int(curr + str(root.val))
    curr += str(root.val)
    score = 0
    if root.left is not None:
        score += compute_score(root.left, curr)
    if root.right is not None:
        score += compute_score(root.right, curr)
    return score

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return compute_score(root, "")
        