# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(root,left=float('-inf'),right=float('inf')):
            if not root:return True
            if root.val<=left or root.val>=right:return False
            return dfs(root.left,left,root.val) and dfs(root.right,root.val,right)
        return dfs(root)