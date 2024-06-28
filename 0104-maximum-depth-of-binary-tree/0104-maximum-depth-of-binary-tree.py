# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def maxDepthRec(node, curr):
    res = maxDepthRec(node.left, curr + 1) if (node.left is not None) else curr
    res = max(res, maxDepthRec(node.right, curr + 1) if (node.right is not None) else curr)
    return res

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        res = 1
        ltr = root
        return maxDepthRec(ltr, res)