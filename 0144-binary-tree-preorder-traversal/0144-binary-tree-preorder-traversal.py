# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorderTraversalRec(node: TreeNode):
            if node is not None:
                ab = [node.val]
                if node.left is not None:
                    ab += preorderTraversalRec(node.left)
                if node.right is not None:
                    ab += preorderTraversalRec(node.right)
                return ab
            return []
        return preorderTraversalRec(root)
        