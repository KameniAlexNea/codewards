# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorderTraversalRec(node: TreeNode):
            if node is not None:
                ab = []
                if node.left is not None:
                    ab += postorderTraversalRec(node.left)
                if node.right is not None:
                    ab += postorderTraversalRec(node.right)
                ab += [node.val]
                return ab
            return []
        return postorderTraversalRec(root)