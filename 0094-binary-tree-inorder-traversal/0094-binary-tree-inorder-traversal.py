# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorderTraversalRec(node: TreeNode):
            if node is not None:
                ab = []
                if node.left is not None:
                    ab += inorderTraversalRec(node.left)
                ab += [node.val]
                if node.right is not None:
                    ab += inorderTraversalRec(node.right)
                return ab
            return []
        
        def inorderTraversalRecV2(node: TreeNode, res = []):
            if node is None:
                return res
            if node.left is not None:
                inorderTraversalRecV2(node.left, res)
            res.append(node.val)
            if node.right is not None:
                inorderTraversalRecV2(node.right, res)
            return res
        return inorderTraversalRecV2(root)