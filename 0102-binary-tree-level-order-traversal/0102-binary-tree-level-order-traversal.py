# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrderRec(self, root: TreeNode, l, result):
        if root is None:
            return
        line = (root.left is None) and (root.right is None)
        if root.left is not None:
            result[l].append(root.left.val)
        if root.right is not None:
            result[l].append(root.right.val)
        if not line:
            self.levelOrderRec(root.left, l+1, result)
            self.levelOrderRec(root.right, l+1, result)
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return
        result = collections.defaultdict(list)
        result[0].append(root.val)
        self.levelOrderRec(root, 1, result)
        return [
            result[i] for i in range(len(result))
        ]